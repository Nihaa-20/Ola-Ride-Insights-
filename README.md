# OLA Rider Project Dashboard

Analyze OLA ride-sharing data to gain insights on ride volume, revenue, vehicle performance, cancellations, and customer behavior using SQL, Power BI, and Streamlit.

## Problem Statement

OLA generates vast ride data. This project processes and analyzes it to optimize operations, improve customer satisfaction, and inform business strategies through data cleaning, EDA, SQL queries, Power BI dashboards, and a Streamlit app.

### Business Use Cases
- Identify peak demand hours for driver allocation
- Analyze customer behavior for marketing
- Evaluate pricing and surge pricing effectiveness
- Detect anomalies or fraud in ride data

## Features
- **SQL Queries**: Run Beginner, Intermediate, Advanced queries for ride trends, cancellations, ratings
- **Power BI Dashboard**: Visualizations for ride volume, revenue, cancellations with filters
- **Streamlit App**: Tabs for Home, SQL Queries, Dashboard, About
- **Views**:
  - Overall: Ride volume over time, booking status
  - Vehicle Type: Top 5 vehicles by distance
  - Revenue: By payment method, top customers, daily distance
  - Cancellation: Reasons by customers and drivers
  - Ratings: Driver and customer ratings

## Folder Structure
OLA_Rider_Project/
├── app.py                    # Streamlit app
├── queries.py                # SQL queries
├── database/
│   └── OLA_DataSet.db        # SQLite database
├── requirements.txt          # Dependencies
└── README.md                 # Documentation

## Prerequisites
- Python 3.8+
- SQLite database (`OLA_DataSet.db`)
- Power BI account (optional)
- ODBC driver (if using `pyodbc`)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd OLA_Rider_Project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place `OLA_DataSet.db` in `database/` or update path in `app.py`.

## Requirements
streamlit
pandas
matplotlib
pyodbc
sqlalchemy
sqlite3

## How to Run
1. Navigate to project directory:
   ```bash
   cd OLA_Rider_Project
   ```
2. Run Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Open `http://localhost:8501` in browser.

## Approach
1. **Data Exploration**: Load dataset, perform EDA with `pandas`, `matplotlib`
2. **Data Cleaning**: Handle missing values, standardize formats
3. **SQL Queries**: Write optimized queries in `queries.py` using `sqlite3` or `sqlalchemy`
4. **Power BI Dashboard**: Create visualizations for trends, revenue, cancellations
5. **Streamlit App**: Build UI with tabs, embed Power BI visuals
6. **Documentation**: Document insights and queries

## Database
- SQLite database (`OLA_DataSet.db`) in `database/`
- Supports `sqlite3`, `sqlalchemy`, `pyodbc`
- Update path in `app.py`:
  db_path = "database/OLA_DataSet.db"
 

## Power BI Integration
- Embeds Power BI report via iframe
- Update URL in `app.py`:
  power_bi_url = "https://app.powerbi.com/view?r=<your-report-id>"
  

## Notes
- Ensure database accessibility
- Test connectivity before running
- Power BI requires internet
- Deploy on Streamlit Cloud for production

## License
MIT License