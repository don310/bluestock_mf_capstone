# 📊 BlueStock Mutual Fund Analytics Project

## 📌 Overview
This project is a data engineering + analytics pipeline for Mutual Fund analysis using Python, Pandas, and MFAPI data.

It includes:
- Data ingestion of 10 mutual fund datasets
- Live NAV data extraction using MFAPI
- Data validation using AMFI scheme codes
- Exploratory analysis of fund master data
- Structured project pipeline with Git version control

---

## ⚙️ Tech Stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn, Plotly
- Requests
- SQLAlchemy
- Jupyter Notebook
- Git & GitHub

---

## 📁 Project Structure
data/
├── raw/
├── processed/
├── db/

scripts/
notebooks/
sql/
dashboard/
reports/

---

## 🔄 Data Pipeline
1. Load 10 CSV datasets
2. Validate schema (.shape, .dtypes, .head)
3. Fetch live NAV data from MFAPI
4. Store cleaned datasets
5. Validate AMFI codes
6. Generate insights-ready data

---

## 🌐 API Used
MFAPI:
https://api.mfapi.in/mf/125497

Used for fetching real-time NAV data of mutual funds.

---

## 📊 Key Insights
- Fund houses and categories analyzed
- Risk classification explored
- NAV trends extracted from live API
- Data consistency validated using AMFI codes

---

## ✅ Data Quality Checks
- Missing AMFI codes checked
- Schema validation performed
- API response validation completed
- CSV integrity verified

---

## 🚀 Outcome
A complete ETL pipeline for mutual fund analytics with real-world data integration.

---

## 👨‍💻 Author
Your Name