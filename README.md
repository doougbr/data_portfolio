
# 🧴 Perfume Listings Analysis: End-to-End Data Pipeline Project

## 📌 Project Overview

This is an end-to-end data pipeline project built to demonstrate data analyst skills using a real-world dataset. The project focuses on **perfume listings from eBay**, combining my passion for perfumery with technical expertise in data ingestion, transformation, storage, analysis, and visualization.

The goal is to extract valuable insights from the dataset and present them in an interactive Power BI dashboard.

---

## 🧰 Tools & Technologies

- **Python** (Pandas, native libraries, Google Cloud libraries)
- **Google Cloud Platform**  
  - Cloud Storage  
  - BigQuery
- **Power BI**
- **GitHub** (version control)

---

## 🔁 ETL Workflow

### 1. **Data Extraction**
- Source: Kaggle perfume listings dataset
- Accessed via **Kaggle API**

### 2. **Data Transformation**
- Cleaned and processed using **Pandas**
- Converted to **Parquet** for storage efficiency
- Uploaded to **Google Cloud Storage** via automated Python script

### 3. **Data Loading**
- Data ingested into **BigQuery** from Cloud Storage
- Tables created and validated using SQL queries

### 4. **Data Visualization**
- Connected **Power BI** to BigQuery
- Transformed data using Power Query (e.g., merged datasets, split location fields)
- Built a **dashboard** following best practices (minimal color palette, contrast, clean layout)

---

## 📊 Dashboard Preview

> *(Insert screenshot or GIF of the dashboard here)*

Key Features:
- Filter by location, brand, or price range
- Visualize top-selling brands and average prices
- Analyze regional trends and listing distributions

---

## 📈 Key Insights

- Brand **X** had the highest average price across all regions.
- Listings from **Europe** were priced higher than those from **North America**.
- Most common cities for perfume listings were **[City A, City B, City C]**.
- Parquet files reduced data size by **~X%** compared to CSV format.

---

## 🗂️ Project Structure

```
perfume-analysis/
│
├── data/                   # Raw and transformed datasets
├── notebooks/              # Jupyter notebooks (optional)
├── scripts/                # Python scripts for ETL
├── dashboard/              # Power BI report files
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

---

## ⚙️ How to Run

### Prerequisites:
- Python 3.8+
- GCP account with access to Cloud Storage and BigQuery
- Power BI Desktop

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/perfume-analysis.git
cd perfume-analysis
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API keys
- Save your `kaggle.json` in `~/.kaggle/`
- Authenticate your Google Cloud SDK or set service account credentials

### 4. Run the ETL script
```bash
python scripts/upload_to_gcs.py
```

---

## 🚀 Future Improvements

- Automate data ingestion using **Cloud Functions** or **Airflow**
- Deploy dashboard via **Power BI Service**
- Enhance visualizations with forecasting or ML-based price predictions
- Add web scraping for real-time listings

---

## 📎 References

- [Kaggle Dataset](https://www.kaggle.com/)
- [Google Cloud Storage Docs](https://cloud.google.com/storage/docs)
- [BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Power BI Desktop](https://powerbi.microsoft.com/)

---

## 💬 Connect

Have questions or feedback? Feel free to reach out or open an issue!
