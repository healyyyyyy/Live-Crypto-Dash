# Live Cryptocurrency Dashboard

Previous Release: 
[Version 1.0](https://github.com/healyyyyyy/Live-Crypto-Dashboard-local)

**Version 2.0**

---

## Overview

This project is a basic cryptocurrency ETL (Extract, Transform, Load) pipeline focused on three popular cryptocurrencies:

- Bitcoin
- Ethereum
- Tron

This is a personal project I took on to help me understand and pivot towards data engineering, from a data analysis background.

Learning objectives:
-Writing scripts
-Understanding ETL v/s ELT
-Deploying a dashboard
-Interact with cloubd based tools
-Hands-on approach to data freshness, duplication, and structure

---

## Features

- **Data Extraction:** Fetches live cryptocurrency data directly from the CoinGecko API.  
- **Data Cleaning:** Formats timestamps and prices to ensure consistency and usability.  
- **Live Dashboard:** Displays real-time updates through a Streamlit dashboard.

---

## Usage

1. Run the ETL pipeline to extract and clean data.  
2. Launch the Streamlit app to view live cryptocurrency prices and trends.

Note: You will have to use your own Google Cloud Platform credentials. I have provided a template .TOML file for this purpose.

---

## Technologies

- Python  
- CoinGecko API  
- Streamlit  
