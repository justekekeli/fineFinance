-- db creation
CREATE DATABASE fine_finance_db;
-- snowflake user creation and grant read-only right
-- 1. Create the user
CREATE USER my_user WITH PASSWORD 'mypassword';

-- 2. Allow them to see the schema (but not read objects by default)
GRANT USAGE ON SCHEMA crm TO my_user;
GRANT USAGE ON SCHEMA banking TO my_user;
GRANT USAGE ON SCHEMA product TO my_user;

-- 3. Grant read access ONLY on base tables (not views)
-- This must be done manually for each table:
GRANT SELECT ON crm.customer TO my_user;
GRANT SELECT ON crm.advisor TO my_user;

GRANT SELECT ON banking.account TO my_user;
GRANT SELECT ON banking.transaction TO my_user;
GRANT SELECT ON banking.balance TO my_user;

GRANT SELECT ON product.loan TO my_user;
GRANT SELECT ON product.investment TO my_user;
GRANT SELECT ON product.credit_card TO my_user;