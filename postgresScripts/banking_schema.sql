-- Schema creation
CREATE SCHEMA IF NOT EXISTS banking;
COMMENT ON SCHEMA banking IS 'Holds transactional data such as accounts, balances, and transactions';
--- tables creation 

CREATE TABLE banking.account (
    account_id UUID PRIMARY KEY,
    customer_id UUID NOT NULL,
    account_type VARCHAR(10) CHECK (account_type IN ('normal', 'LJ','LA')),
    open_date DATE
);

CREATE TABLE banking.transaction (
    transaction_id UUID PRIMARY KEY,
    receiver_account_id UUID NOT NULL ,
    sender_account_id UUID NOT NULL ,
    transaction_date TIMESTAMP(3) NOT NULL,
    amount NUMERIC(12, 2) NOT NULL,
    description VARCHAR(100),
    category VARCHAR(15) CHECK (category IN ('subscription', 'salary','loan_payment','reimboursement','transfer')),
    transaction_direction VARCHAR(15) CHECK (transaction_direction IN ('IN', 'OUT')),
    status  VARCHAR(20) NOT NULL DEFAULT 'pending', -- e.g. pending, success, failed
    created_at TIMESTAMP(3) DEFAULT NOW(),
    updated_at TIMESTAMP(3) DEFAULT NOW(),
    currency VARCHAR(3)
);
CREATE INDEX transaction_date_indx ON banking.transaction(transaction_date);

CREATE TABLE banking.balance (
    account_id UUID NOT NULL,
    balance_date DATE NOT NULL,
    balance NUMERIC(12, 2),
    currency VARCHAR(3),
    PRIMARY KEY (account_id, balance_date)
);