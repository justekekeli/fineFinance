
import time
from getDBconnection import connectToSourceDB
from datetime import datetime, timedelta
from data_faker import *


def get_random_advisor_id():
    conn = connectToSourceDB()
    cursor = conn.cursor()
    cursor.execute("SELECT advisor_id FROM crm.advisor ORDER BY RANDOM() LIMIT 1")
    advisor = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return advisor[0]

def get_random_account_ids():
    conn = connectToSourceDB()
    cursor = conn.cursor()
    cursor.execute("SELECT account_id FROM banking.account where open_date=(SELECT MAX(open_date) FROM banking.account)")
    accounts = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return accounts

def get_random_customer_id():
    conn = connectToSourceDB()
    cursor = conn.cursor()
    cursor.execute("SELECT customer_id FROM crm.customer ORDER BY RANDOM() LIMIT 1")
    account = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return account[0]


def insert_advisor():
    conn = connectToSourceDB()
    cursor = conn.cursor()

    advisor  = generate_advisor()

    cursor.execute("""
        INSERT INTO crm.advisor
        (advisor_id, firstname, surname, city)
        VALUES (%s, %s, %s, %s) ON CONFLICT (advisor_id) DO NOTHING;
    """, advisor)

    conn.commit()
    cursor.close()
    conn.close()
    print(f"[{datetime.now()}] Created advisor {advisor[1]} {advisor[2]}.")

def insert_customer_and_account_and_balance():
    conn = connectToSourceDB()
    cursor = conn.cursor()

    advisor  = get_random_advisor_id()

    customer = generate_customer(advisor)
    print(advisor)
    cursor.execute("""
        INSERT INTO crm.customer
        (customer_id, firstname, surname, signup_date, profile_level, advisor_id)
        VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (customer_id) DO NOTHING;
    """, customer)

    account = generate_account(customer[0])
    cursor.execute("""
        INSERT INTO banking.account
        (account_id, customer_id, account_type, open_date)
        VALUES (%s, %s, %s, %s) ON CONFLICT (account_id) DO NOTHING;
    """, account)

    balance = generate_balance(account[0])
    
    cursor.execute("""
        INSERT INTO banking.balance
        (account_id, balance_date, balance, currency)
        VALUES (%s, %s, %s, %s) ON CONFLICT (account_id,balance_date) DO NOTHING;
    """, balance)


    conn.commit()
    cursor.close()
    conn.close()
    print(f"[{datetime.now()}] Created customer {customer[1]} {customer[2]} with account with balance details.")


def insert_transaction(transaction):
    conn = connectToSourceDB()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO banking.transaction
        (transaction_id,receiver_account_id, sender_account_id ,transaction_date, amount, description, category , transaction_direction, status,created_at,updated_at,currency)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (transaction_id) DO NOTHING;
    """, transaction)
    conn.commit()
    cursor.close()
    conn.close()

def insert_credit_card(customer_id):
    conn = connectToSourceDB()
    cursor = conn.cursor()
    credit_card = generate_credit_card(customer_id)
    cursor.execute("""
        INSERT INTO product.credit_card
        (card_id,customer_id, amount_limit , fee, start_date, end_date , status)
        VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (card_id) DO NOTHING;
    """, credit_card)
    conn.commit()
    cursor.close()
    conn.close()

def insert_loan(customer_id):
    conn = connectToSourceDB()
    cursor = conn.cursor()
    loan = generate_loan(customer_id)
    cursor.execute("""
        INSERT INTO product.loan
        (loan_id,customer_id, amount, interest_rate,start_date,end_date,status)
        VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (loan_id) DO NOTHING;
    """, loan)
    conn.commit()
    cursor.close()
    conn.close()

def insert_investment(customer_id):
    conn = connectToSourceDB()
    cursor = conn.cursor()
    investment = generate_investment(customer_id)
    cursor.execute("""
        INSERT INTO product.investment
        (investment_id,customer_id, product_name ,amount,opened_at,status)
        VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (investment_id) DO NOTHING;
    """, investment)
    conn.commit()
    cursor.close()
    conn.close()

def run_generator():
    accounts = get_random_account_ids()
    # Force create on first run
    last_customer_gen = datetime.now() - timedelta(days=1)  
    last_advison_gen = datetime.now() - timedelta(days=90)
    last_credit_card_gen = datetime.now() - timedelta(days=7)
    last_investment_gen = datetime.now() - timedelta(days=7)
    last_loan_gen = datetime.now() - timedelta(days=7)

    transactions_per_hour = 10000
    delay_between_tx = 3600 / transactions_per_hour  # ~0.36 seconds

    while True:
        now = datetime.now()

        if (now - last_advison_gen).days >= 90:
            for _ in range(2):
                insert_advisor()
            last_advison_gen = now

        # Create 5 new customers per day
        if (now - last_customer_gen).days >= 1:
            for _ in range(5):
                insert_customer_and_account_and_balance()
            accounts = get_random_account_ids()
            last_customer_gen = now

        # create credits cards
        if (now - last_credit_card_gen).days >= 7:
            for _ in range(5):
                customer_id = get_random_customer_id()
                insert_credit_card(customer_id)
            last_credit_card_gen = now

        # create loans
        if (now - last_loan_gen).days >= 7:
            for _ in range(5):
                customer_id = get_random_customer_id()
                insert_loan(customer_id)
            last_loan_gen = now
        # create investments
        if (now - last_investment_gen).days >= 7:
            for _ in range(5):
                customer_id = get_random_customer_id()
                insert_investment(customer_id)
            last_investment_gen = now

        # Create a transaction
        if accounts:
            tx = generate_transaction(accounts)
            insert_transaction(tx)
            print(f"[{datetime.now()}] Inserted transaction {tx[0]}")

        time.sleep(delay_between_tx)  # wait before next transaction

if __name__ == "__main__":
    run_generator()
