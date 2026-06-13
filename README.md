# 📈 Bluestock Mutual Fund Analytics Capstone Project

## End-to-End Data Engineering, Analytics & Business Intelligence Solution for Mutual Fund Performance Evaluation

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)
![License](https://img.shields.io/badge/License-MIT-success)

---

# Project Overview

The **Bluestock Mutual Fund Analytics Capstone Project** is a complete end-to-end data analytics solution designed to analyze, evaluate, and visualize mutual fund performance using modern Data Analytics and Business Intelligence techniques.

The project integrates multiple datasets through an ETL pipeline, stores cleaned data in a SQLite data warehouse, performs exploratory and advanced financial analysis, and presents insights through interactive dashboards.

The objective is to demonstrate practical skills in:

* Data Engineering
* SQL
* Python
* Exploratory Data Analysis
* Financial Analytics
* Business Intelligence
* Dashboard Development

---

# Problem Statement

The Indian Mutual Fund industry consists of thousands of investment schemes across multiple categories.

Most investors evaluate funds only based on historical returns while ignoring:

* Risk
* Expense Ratio
* Alpha
* Beta
* Sharpe Ratio
* Portfolio Concentration
* Investor Behaviour

This project develops a unified analytics platform capable of transforming raw mutual fund data into actionable business insights.

---

# Project Objectives

* Build an automated ETL pipeline
* Clean and validate datasets
* Create a SQLite Data Warehouse
* Perform Exploratory Data Analysis
* Evaluate fund performance
* Analyze investment risk
* Study investor behaviour
* Develop interactive dashboards
* Generate business recommendations

---

# Technologies Used

## Programming

* Python

## Libraries

* Pandas
* NumPy
* Matplotlib
* Plotly
* SQLAlchemy
* Requests
* Streamlit

## Database

* SQLite

## Visualization

* Power BI
* Streamlit

## Version Control

* Git
* GitHub

---

# Project Architecture

```
Raw Data

        │

        ▼

ETL Pipeline

        │

        ▼

Data Cleaning

        │

        ▼

SQLite Warehouse

        │

        ▼

SQL Queries

        │

        ▼

EDA

        │

        ▼

Advanced Analytics

        │

        ▼

Power BI / Streamlit Dashboard

        │

        ▼

Business Insights
```

---

# Datasets Used

## Fund Master

Contains:

* AMFI Code
* Scheme Name
* Fund House
* Category
* Risk Category
* Expense Ratio

---

## NAV History

Contains:

* NAV Date
* NAV Value

Used for:

* Trend Analysis
* Rolling Metrics
* Simulation

---

## Performance Dataset

Contains:

* 1-Year Return
* 3-Year Return
* 5-Year Return
* Alpha
* Beta
* Sharpe Ratio

---

## Investor Transactions

Contains:

* Investor ID
* Transaction Date
* Investment Amount

Used for:

* Cohort Analysis
* SIP Analysis

---

# ETL Pipeline

The ETL pipeline performs:

* Data Extraction
* Missing Value Handling
* Duplicate Removal
* Data Type Conversion
* Validation
* Loading into SQLite

---

# Database Schema

## Dimension Tables

* dim_fund
* dim_date

## Fact Tables

* fact_nav
* fact_performance
* fact_transactions

---

# Exploratory Data Analysis

Performed analyses include:

* Category Distribution
* Fund House Comparison
* Return Distribution
* Risk Distribution
* Expense Ratio Analysis
* NAV Trends

---

# Advanced Analytics

Implemented:

* Sharpe Ratio
* Alpha
* Beta
* Rolling Analysis
* Risk vs Return
* Cohort Analysis

---

# Bonus Challenges

## B1

Automated NAV ETL

* API Fetch
* SQLite Update
* Scheduled Execution

---

## B2

Streamlit Dashboard

Features:

* KPI Cards
* Interactive Charts
* Filters
* Analytics Pages

---

## B3

Monte Carlo Simulation

Projects future NAV paths using stochastic simulation to estimate uncertainty and expected growth.

---

## B4

Markowitz Efficient Frontier

Implements Modern Portfolio Theory for portfolio optimization and efficient frontier visualization.

---

## B5

Automated HTML Report

Generates a professional weekly performance summary with KPIs and insights.

---

# Folder Structure

```
Bluestock_MF_Capstone/

│

├── data/
│   ├── raw/
│   ├── processed/
│   ├── advanced/
│   └── db/
│
├── notebooks/
│
├── scripts/
│
├── sql/
│
├── reports/
│
├── dashboard/
│
├── bonus/
│
├── README.md
│
├── requirements.txt
│
└── LICENSE
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd Bluestock_MF_Capstone
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

Run Streamlit Dashboard

```bash
streamlit run app.py
```

Run Monte Carlo

```bash
python monte_carlo.py
```

Run Markowitz

```bash
python markowitz.py
```

Run NAV Fetch

```bash
python nav_fetch.py
```

Generate HTML Report

```bash
python email_report.py
```

---

# Business Insights

* Risk-adjusted metrics are superior to return-only evaluation.
* Higher Sharpe Ratio generally indicates better investment efficiency.
* Portfolio diversification reduces concentration risk.
* Continuous monitoring enables informed investment decisions.
* Analytics improves transparency and decision support.

---

# Future Scope

* Live API Integration
* Machine Learning Prediction
* AI-based Recommendation Engine
* Web Deployment
* Cloud Database Migration
* Real-time Dashboards
* Sentiment Analysis
* Portfolio Optimization

---

# Skills Demonstrated

* Python Programming
* Data Engineering
* SQL
* SQLite
* ETL Pipeline
* Exploratory Data Analysis
* Financial Analytics
* Business Intelligence
* Dashboard Development
* Portfolio Optimization

---

# Author

**Arpit Singh**

Data Analytics & Artificial Intelligence Enthusiast

---

# License

This project is created for educational and portfolio purposes.


# 🚀 Bluestock Mutual Fund Analytics Capstone v1.0.0

## Highlights

This release marks the completion of the **Bluestock Mutual Fund Analytics Capstone Project**, an end-to-end Data Analytics and Business Intelligence solution for mutual fund performance evaluation.

## Features

* ✅ Automated ETL Pipeline
* ✅ Data Cleaning & Validation
* ✅ SQLite Data Warehouse
* ✅ SQL Analytics
* ✅ Exploratory Data Analysis
* ✅ Financial Performance Analysis
* ✅ Risk Analytics (Alpha, Beta, Sharpe Ratio)
* ✅ Interactive Power BI Dashboard
* ✅ Streamlit Dashboard
* ✅ Monte Carlo NAV Simulation
* ✅ Markowitz Efficient Frontier Portfolio Optimization
* ✅ Automated NAV Fetch Utility
* ✅ Automated HTML Performance Report Generator

## Tech Stack

* Python
* Pandas
* NumPy
* SQLite
* SQLAlchemy
* Matplotlib
* Plotly
* Streamlit
* Power BI

## Repository Contents

* Source Code
* SQL Scripts
* Data Pipeline
* Dashboard Files
* Final Report
* Presentation
* Documentation

## Status

🎉 Stable Release – Version 1.0.0
