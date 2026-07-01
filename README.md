# 📊 InfluenceIQ — YouTube Analytics & Intelligence Platform

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=yellow" alt="Python Version">
  <img src="https://img.shields.io/badge/PostgreSQL-14%2B-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-D71F27?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/Streamlit-Interactive%20UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/NLP-VADER%20%7C%20Rules-orange?style=for-the-badge" alt="NLP Engine">
  <img src="https://img.shields.io/badge/Build-Passing-emerald?style=for-the-badge" alt="Build Status">
  <img src="https://img.shields.io/badge/License-MIT-blueviolet?style=for-the-badge" alt="License">
</p>

---

## 🚀 Overview

**InfluenceIQ** is an end-to-end data engineering and natural language processing (NLP) intelligence platform designed to scrape, analyze, and visualize YouTube channel metrics, videos, and audience engagement comments. 

The platform fetches data via the **YouTube Data API v3**, models database relationships using **SQLAlchemy ORM**, stores records securely inside a **PostgreSQL** database, and processes comments through a multi-stage **NLP Text Cleaning and Enrichment Pipeline**. Finally, it feeds an interactive **Streamlit dashboard** that provides actionable engagement and behavioral metrics.

---

## ✨ Features

- 📥 **Automated Data Ingestion:** Extract real-time channel statistics, video information, and top comment threads using the official YouTube Data API v3.
- 🗄️ **Relational Database Backend:** Robust relational tables representing Channels, Videos, and Comments built with **SQLAlchemy ORM** on top of **PostgreSQL**.
- 🧹 **Advanced Text Cleaning:** Normalization engine that strips URLs, emojis, duplicate spacing, and punctuation to clean messy online text.
- 🚫 **Toxicity & Abuse Filtering:** Keyword-matching classifier that tracks and tags comments that violate community standards or contain aggressive language.
- 🤖 **Spam Detection:** Integrated phrase matcher to catch and filter out repetitive promotions, links, and bot-generated comments.
- 🧠 **Sentiment Intelligence:** Powered by the **VADER Sentiment Analyzer** to classify user messages into Positive, Neutral, and Negative categories.
- ⚙️ **Feature Engineering:** Computes critical key performance indicators (KPIs) like comment-to-view ratios, sentiment score distributions, and spam metrics.
- 📊 **Executive Dashboard:** A responsive **Streamlit** dashboard featuring interactive **Plotly** data visualisations, statistics summaries, and custom filters.

---

## 🧠 NLP & Data Pipeline Architecture

The platform runs as a series of modular data pipelines. Below is the system flow:

```mermaid
flowchart TD
    A[Raw YouTube Data API v3] -->|Fetch Channel & Videos| B[Database Ingestion]
    B -->|Fetch Comments| C[Text Cleaning & Normalization]
    C -->|Strip URLs/Emojis| D[Spam Detection Pipeline]
    D -->|Keyword Rules| E[Sentiment Analysis Engine]
    E -->|VADER Classification| F[Abusive Language Filter]
    F -->|Toxicity Checking| G[Feature Engineering Core]
    G -->|Calculate KPIs| H[(PostgreSQL Database)]
    H -->|Query Metrics| I[Interactive Streamlit Dashboard]
    
    style A fill:#3b82f6,stroke:#1d4ed8,stroke-width:2px,color:#fff
    style H fill:#10b981,stroke:#047857,stroke-width:2px,color:#fff
    style I fill:#8b5cf6,stroke:#6d28d9,stroke-width:2px,color:#fff
```

---

## 📂 Project Structure

```
InfluenceIQ
├── data/                   # Raw data backups and JSON artifacts
├── notebook/               # Exploratory Data Analysis & experiments
├── reports/                # Static reporting documents
├── src/                    # System source code
│   ├── api/                # YouTube Data API scraping integration
│   ├── abusive/            # Abuse & toxicity detection logic
│   ├── cleaning/           # Text processing & spam filters
│   ├── dashboard/          # Streamlit UI panels & app configuration
│   ├── database/           # Relational schemas & postgres connector
│   ├── features/           # Feature engineering metrics
│   ├── pipeline/           # Sequential orchestration files
│   ├── repositories/       # DB access repositories
│   ├── sentiment/          # VADER sentiment configuration
│   └── utils/              # Project wide helper functions
├── main.py                 # Command line pipeline supervisor
└── requirements.txt        # Package configuration manifest
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/InfluenceIQ.git
cd InfluenceIQ
```

### 2. Configure Virtual Environment
```bash
# Initialize venv
python -m venv .venv

# Activate on Windows:
.venv\Scripts\activate

# Activate on macOS / Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
Create a file named `.env` in the root of the project directory and configure the database link and your API key:
```env
DATABASE_URL="postgresql://neondb_owner:YOUR_PASS@ep-YOUR-HOST.neon.tech/neondb?sslmode=require"
YOUTUBE_API_KEY="AIzaSyBr3RPSS4..."
```

---

## ▶️ How to Run

### Command Line Interface (Ingestion & Pipelines)
To run the automated data extraction, cleaning, spam detection, sentiment analysis, and feature engineering, execute:
```bash
python main.py
```
This runs an interactive command line interface where you can choose to fetch YouTube data, process NLP pipelines in batches, or execute the complete end-to-end flow sequentially.

### Executive Streamlit Dashboard
To launch the interactive dashboard website:
```bash
streamlit run src/dashboard/app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📈 Dashboard Layout & Insights

- **🏠 Home Overview:** Core summaries of channels, general view-to-comment analytics, and total records.
- **🎥 Video Performance:** engagement, views, likes, and subscription stats mapped by video.
- **💬 Comment Details:** Live feed of comments, raw versus clean text representation, and detailed metrics.
- **🧠 NLP Analytics:** Interactive charts detailing sentiment distributions, spam versus authentic comment counts, and toxicity warnings.
- **📊 Executive Insights:** Advanced aggregated key insights for audience intelligence.

---

## 🔮 Future Enhancements
- [ ] Implement real-time streaming pipelines using YouTube API webhooks.
- [ ] Add Topic Modeling (LDA) to classify themes of discussion.
- [ ] Introduce a Machine Learning Recommendation model.
- [ ] Transition the pipeline to containerized Cloud Run deployments.

---
*Created with ❤️ for creators, marketers, and data engineers. Licensed under the MIT License.*
