# Financial Performance Analysis (Budget vs Actual)

## Overview

This project analyzes **financial performance by comparing Budget vs Actual spending across different departments**.
The objective is to identify **financial variances, monitor departmental performance, and support data-driven financial decision making**.

The project demonstrates a **complete end-to-end data analytics workflow**, including data cleaning, data analysis using Python and SQL, and interactive dashboard visualization.

---

# Project Objectives

* Analyze **budget vs actual financial performance**
* Calculate **financial variance across departments**
* Identify **departments exceeding their allocated budgets**
* Track **monthly financial trends**
* Create a **visual dashboard for business insights**

---

# Tools & Technologies

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **SQL**
* **Power BI**
* **Microsoft Excel**
* **Git & GitHub**

---

# Project Structure

```
financial-performance-analysis
│
├── data
│   ├── financial_data.csv
│   ├── clean_financial_data.csv
│   └── financial_analysis_output.csv
│
├── python
│   ├── data_cleaning.py
│   └── financial_analysis.py
│
├── sql
│   └── financial_analysis.sql
│
├── dashboard
│   └── financial_dashboard.pbix
│
├── images
│   └── dashboard_preview.png
│
├── README.md
└── requirements.txt
```

---

# Dataset Description

The dataset contains financial information for different departments.

| Column     | Description              |
| ---------- | ------------------------ |
| Month      | Reporting month          |
| Department | Department name          |
| Budget     | Planned financial budget |
| Actual     | Actual spending          |

---

# Data Analysis Process

### 1. Data Cleaning

* Handled missing values
* Standardized column names
* Removed inconsistent data entries

### 2. Financial Analysis

* Calculated **Budget vs Actual variance**
* Aggregated department-level spending
* Generated monthly performance summaries

### 3. SQL Queries

SQL was used to perform:

* Department spending analysis
* Total budget vs actual comparison
* Monthly financial performance trends
* Identification of overspending departments

### 4. Dashboard Visualization

A **Power BI dashboard** was created to visualize:

* Total Budget vs Actual spending
* Department performance comparison
* Financial variance
* Monthly financial trends

---

# Key Insights

* Identified departments **exceeding their allocated budgets**
* Compared **planned vs actual expenditures**
* Generated financial summaries to assist **business decision-making**
* Provided clear visual insights through **interactive dashboards**

---

# How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/financial-performance-analysis.git
```

### 2. Install required libraries

```bash
pip install -r requirements.txt
```

### 3. Run Python scripts

Run the scripts in the following order:

```
python data_cleaning.py
python financial_analysis.py
```

---


# Author

**Abhishek Roy**

