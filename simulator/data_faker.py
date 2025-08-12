
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()



def generate_advisor():
    return (
        fake.uuid4(),
        fake.first_name(),
        fake.last_name(),
        fake.city(),
        datetime.now().date()
)

def generate_customer(advisor_id):
    return (
        fake.uuid4(),
        fake.first_name(),
        fake.last_name(),
        datetime.now().date(),
        random.choice(['bronze', 'gold']),
        advisor_id
    )

def generate_account(customer_id):
    return (
        fake.uuid4(),
        customer_id,
        random.choice(['normal', 'LJ','LA']),
        datetime.now().date(),
    )

def generate_balance(account_id):
    return (
        account_id,
        datetime.now().date(),
        random.randrange(-1000, 30000),
        fake.currency_code()
    )

def generate_transaction(accounts):
    sender = random.choice(accounts)
    receiver = random.choice(accounts)
    while receiver == sender:
        receiver = random.choice(accounts)

    return (
        fake.uuid4(),
        sender,
        receiver,
        datetime.now(),
        round(random.uniform(5, 2000), 2),
        random.choice(['subscription', 'salary','loan_payment','reimboursement','transfer']),
        random.choice(['subscription', 'salary','loan_payment','reimboursement','transfer']),
        random.choice(['IN', 'OUT']),
        random.choice(['completed', 'pending', 'failed']),
        datetime.now(),
        datetime.now(),
        fake.currency_code()
    )


def generate_credit_card(customer_id):
    return (
        fake.uuid4(),
        customer_id,
        random.choice([10000, 50000, 1000000]),
        random.randrange(5, 10),
        datetime.now().date(),
        datetime.now() + timedelta(weeks=156) ,
        'active'
    )


def generate_loan(customer_id):
    return (
        fake.uuid4(),
        customer_id,
        random.randrange(3000, 500000),
        round(random.uniform(0.02, 0.08),2),
        datetime.now().date(),
        datetime.now() + timedelta(weeks=random.randrange(52, 156)) ,
        'active'
    )

def generate_investment(customer_id):
    return (
        fake.uuid4(),
        customer_id,
        random.choice(['PEA', 'life insurance']),
        random.randrange(100, 50000),
        datetime.now().date(),
        random.choice(['active', 'closed']),
    )