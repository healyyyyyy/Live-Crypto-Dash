# Live Cryptocurrency Dashboard (v1.1 - Cloud Enhancement)

Previous Release: [Version 1.0 - Local SQLite Version](https://github.com/healyyyyyy/Live-Crypto-Dashboard-local)

[Streamlit Dashboard](https://live-crypto-dashboard.streamlit.app)

This upgraded version builds on the foundational project by replacing the local database with a cloud-based solution. It was created to simulate the kind of distributed, production-friendly workflows used in real data engineering environments.

Learning objectives:

- Secure handling of cloud credentials
- Using Google Sheets as a lightweight cloud-based data store
- Deploying a public-facing dashboard via Streamlit Cloud
- Automating updates and integrations in a cloud context
- Managing API and Google Cloud authentication

## Overview

The project is a live cryptocurrency ETL pipeline focusing on:

- Bitcoin  
- Ethereum  
- Tron  
- Additional coins can be added dynamically

---

## Features

- **Data Extraction:** Pulls live market data via the CoinGecko API  
- **Data Cleaning & Transformation:** Deduplicates, timestamps, and pivots data  
- **Cloud Storage:** Writes directly to Google Sheets for easy access and collaboration  
- **Live Dashboard:** Deploys to Streamlit Community Cloud for live visualization

---

## Usage

1. Set up your Google Cloud credentials and store them securely in `secrets.toml` or Streamlit Cloud secrets  
2. Run the ETL pipeline to update data in Google Sheets  
3. Launch the Streamlit dashboard in the cloud or locally to view real-time crypto trends

---

## Technologies

- Python  
- CoinGecko API  
- Google Sheets API (via `gspread` and `oauth2client`)  
- Visualization: Streamlit dashboard (deployed via Streamlit Community Cloud)

---

## Security Notice

- API credentials and GCP service keys are handled securely via Streamlit's secrets management  
- Private keys are never exposed in the source code

---

## Deployment

The dashboard is hosted via [Streamlit Community Cloud](https://streamlit.io/cloud), allowing real-time access without local setup.

---

## Next Steps

The project can be further enhanced with:

- Scheduled automation (e.g., GitHub Actions or Streamlit Cloud jobs)  
- Data warehousing (e.g., BigQuery)  
- More robust error handling and logging  
- Historical trend analysis and alerts

---

## License

MIT License. Built for learning and demonstration purposes.
