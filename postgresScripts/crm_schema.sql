-- Schema creation
CREATE SCHEMA IF NOT EXISTS crm;
COMMENT ON SCHEMA crm IS 'Customer data and profiles';
-- Tables creation
CREATE TABLE crm.customer (
    customer_id UUID PRIMARY KEY,
    firstname VARCHAR(30),
    surname VARCHAR(30),
    signup_date DATE,
    profile_level VARCHAR(8) CHECK (profile_level IN ('bronze', 'gold', 'diamant')),
    advisor_id UUID
);

CREATE TABLE crm.advisor (
    advisor_id UUID PRIMARY KEY,
    firstname VARCHAR(30),
    surname VARCHAR(30),
    city VARCHAR(30)
);