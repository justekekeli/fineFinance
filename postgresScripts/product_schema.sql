-- Schema creation
CREATE SCHEMA IF NOT EXISTS product;
COMMENT ON SCHEMA crm IS 'Create product schema for account and service definitions';
-- Tables creation
CREATE TABLE product.loan (
    loan_id UUID PRIMARY KEY,
    customer_id UUID NOT NULL,
    amount NUMERIC(12, 2),
    interest_rate FLOAT,
    start_date DATE,
    end_date DATE,
    status TEXT CHECK (status IN ('active', 'closed'))
);

CREATE TABLE product.investment (
    investment_id UUID PRIMARY KEY,
    customer_id UUID NOT NULL,
    product_name VARCHAR(20) CHECK (product_name IN ('PEA', 'life insurance')) ,
    amount NUMERIC(12, 2),
    opened_at DATE,
    status TEXT CHECK (status IN ('active', 'closed'))
);

CREATE TABLE product.credit_card (
    card_id UUID PRIMARY KEY,
    customer_id UUID NOT NULL,
    amount_limit NUMERIC(12, 2),
    fee FLOAT,
    start_date DATE,
    end_date DATE,
    status TEXT CHECK (status IN ('active', 'expired'))
);