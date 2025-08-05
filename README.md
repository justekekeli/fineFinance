# FineFinance Data Platform Project

## 📊 Business Context Overview

**FineFinance** is a customer-to-customer (C2C) fintech platform providing digital banking services, including peer-to-peer transfers, investment planning, and credit services. As a new and growing company, FineFinance aims to build a modern data platform that supports real-time insights, customer value segmentation, and strategic business decisions.

To enable personalized customer experiences and support data-driven decision-making across teams, we are building a robust **data stack** using:

- **PostgreSQL** as the operational data source
- **Airbyte** for data ingestion
- **Snowflake** as the cloud data warehouse
- **dbt** for data transformation and modeling
- **Apache Airflow** for orchestration and scheduling

This project is designed both as a **learning experience in data engineering** and a functional prototype for a scalable fintech data stack.

---

## 👥 User Stories & Data Needs

### 🔹 Customers
| As a... | I want to... | So that... |
|--------|---------------|-------------|
| Customer | View the **current balance** of my account | I can understand my financial status |
| Customer | View **upcoming transactions** | I can anticipate changes to my balance |
| Customer | Download my **monthly account statement** | I can track spending and maintain records |

---

### 🔹 Bank Advisors
| As a... | I want to... | So that... |
|--------|---------------|-------------|
| Advisor | See customers with **high withdrawals, loans, or investments** | I can offer them upgraded services |
| Advisor | See customers who were **in the red** for 3+ months | I can offer budgeting support or financial products |

---

### 🔹 Bank Direction / Business Intelligence
| As a... | I want to know... | So that... |
|--------|--------------------|-------------|
| Bank Director | **Monthly growth metrics** (revenue, transaction volume, new customers) | I can evaluate overall business performance |
| Bank Director | The **number of customers per profile** (Bronze, Gold, Diamond) | I can assess customer segmentation |
| Bank Director | The **evolution of transactions per month** | I can track customer engagement and activity |

---

## 📁 Project Structure (coming soon)

