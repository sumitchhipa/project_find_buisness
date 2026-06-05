# 🚀 Business Finder Automation

An automated lead generation system that discovers businesses from Google Maps, stores them in a database, exports them to Google Sheets/CSV, and sends instant notifications via Telegram and Email.

---

## 📌 Features

### 🔍 Google Maps Scraping

* Search businesses by category and postcode
* Scrape business details automatically
* Extract:

  * Business Name
  * Address
  * Phone Number
  * Website
  * Google Maps URL
  * Place ID

### 🗄️ Database Storage

* SQLite database integration
* Stores all discovered businesses
* Prevents duplicate entries using Place ID

### 📊 Data Export

* Export new businesses to CSV
* Export new businesses to Google Sheets

### 🔔 Notifications

* Telegram Bot Notifications
* Email Notifications (Gmail SMTP)

### ⚡ Automation Logic

* Detects newly discovered businesses
* Ignores already existing businesses
* Sends alerts only for new leads

---

# 🏗️ Project Architecture

```text
Google Maps
      │
      ▼
 Playwright Scraper
      │
      ▼
 Business Details
      │
      ▼
 SQLite Database
      │
      ├────────► Duplicate Detection
      │
      ├────────► CSV Export
      │
      ├────────► Google Sheets Export
      │
      ├────────► Telegram Notification
      │
      └────────► Email Notification
```

---

# 🛠️ Tech Stack

| Technology        | Purpose               |
| ----------------- | --------------------- |
| Python            | Core Development      |
| Playwright        | Web Scraping          |
| SQLite            | Database              |
| Google Sheets API | Cloud Data Storage    |
| Telegram Bot API  | Instant Notifications |
| Gmail SMTP        | Email Alerts          |
| CSV               | Data Export           |

---

# 📂 Project Structure

```text
new_business_project/
│
├── config/
│   └── config.json
│
├── data/
│   ├── businesses.db
│   └── new_businesses.csv
│
├── src/
│   ├── database/
│   │   └── db.py
│   │
│   ├── scraper/
│   │   └── maps_scraper.py
│   │
│   ├── exporters/
│   │   ├── csv_exporter.py
│   │   └── google_sheets_exporter.py
│   │
│   ├── notifications/
│   │   ├── telegram_notifier.py
│   │   └── email_notifier.py
│   │
│   └── utils/
│       └── config_loader.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/business-finder-automation.git
cd business-finder-automation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browser:

```bash
playwright install
```

---

# 🔧 Configuration

Create a configuration file:

```json
{
  "postcodes": [
    "302001",
    "302004",
    "302020"
  ],
  "categories": [
    "dentist",
    "gym",
    "restaurant"
  ]
}
```

---

# ▶️ Run The Project

```bash
python main.py
```

---

# 📈 Example Output

```text
RUNNING SEARCH: dentist in 302001

Businesses Found: 8

NEW BUSINESS FOUND:
Dr. Mahima Dental Clinic

Telegram Notification Sent

Email Notification Sent

Exported To Google Sheets

Saved To Database
```

---

# 🔔 Telegram Notifications

Whenever a new business is discovered:

```text
🚀 NEW BUSINESS FOUND

Name:
ABC Dental Clinic

Phone:
9876543210

Website:
www.example.com
```

---

# 📧 Email Notifications

The system automatically sends an email containing:

* Business Name
* Address
* Phone Number
* Website
* Google Maps Link

---

# 📊 Google Sheets Integration

Every newly discovered business is automatically appended to Google Sheets for easy tracking and management.

---

# 🎯 Use Cases

* Lead Generation
* Local Business Research
* Market Analysis
* Sales Prospecting
* Agency Outreach
* Business Intelligence

---

# 🔒 Duplicate Detection

Each business is identified using its Google Place ID.

This ensures:

* No duplicate records
* No duplicate notifications
* Clean database storage

---

# 🚀 Future Enhancements

* Scheduled Automatic Runs
* Multi-City Search
* Website Email Extraction
* Lead Scoring System
* Docker Deployment
* CRM Integration
* AI-Powered Lead Qualification

---

# 👨‍💻 Author

**Sumit Chhipa**

MCA Student | Data Science & AI Enthusiast

Passionate about Python Automation, Machine Learning, NLP, and Building Real-World AI Applications.

---

## ⭐ If you found this project useful, consider giving it a star.
