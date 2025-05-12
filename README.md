# 📈 Real-Time Stock Price Monitoring & Alert System

This project is a **real-world automation framework** that monitors live stock prices, logs them periodically, and sends **instant email alerts** when a stock crosses a predefined price threshold.

Built using **Python**, this framework combines **web scraping (Selenium)**, **API integration**, **email notifications**, and **automated logging/reporting** to simulate a real-time monitoring and alerting platform.

---

## ✅ Features

- 🔎 Scrapes stock price from MarketWatch using **Selenium**
- 🌐 Fetches real-time stock data via **Alpha Vantage API**
- 📬 Sends email alerts when stock crosses threshold
- 📊 Logs prices in a CSV file for historical tracking
- 🧪 Includes unit tests for API, email, and scraper
- 📄 Clean HTML report generation with **pytest-html**

---

## 🛠️ Tech Stack

- **Python 3**
- **Selenium WebDriver**
- **Requests**
- **Pytest**
- **SMTP (for Email Alerts)**
- **Pytest-HTML**
- **Webdriver-Manager**

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Credentials

Edit `config/settings.json` with:

- Your Gmail address & app password
- Alpha Vantage API key
- Stock symbol (e.g., AAPL)
- Alert price threshold

```json
{
  "email": "your_email@example.com",
  "email_password": "your_password",
  "stock_api_key": "your_api_key",
  "target_stock_symbol": "AAPL",
  "threshold": 150
}
```

### 3. Run the Monitor

```bash
python src/stock_monitor.py
```

The script will fetch the current stock price every minute and alert you via email if the price exceeds the threshold.

---

## 🧪 Running Tests

```bash
pytest --html=reports/test-report.html
```

Open the generated HTML report to review test results for:

- API integration
- Web scraping
- Email functionality

---

## 📁 Folder Structure

```
stock-price-monitor/
├── src/                # Source logic
│   ├── stock_scraper.py
│   ├── stock_api.py
│   ├── email_alert.py
│   └── stock_logger.py
├── tests/              # Pytest-based test cases
│   ├── test_stock_scraper.py
│   ├── test_email_alert.py
│   └── test_api_integration.py
├── config/             # JSON-based configuration
│   └── settings.json
├── reports/            # CSV logs and test reports
├── requirements.txt    # Project dependencies
└── README.md           # This file
```

---

## 📬 Output Example

📧 Email Alert:
> "Stock Alert: AAPL Price Crossed 150  
> The stock price for AAPL has reached $152.30"

📊 Log Entry:
```
Stock Symbol, Price, Timestamp
AAPL, 151.73, 2025-05-12T08:35:12
```

---

## 👨‍💻 Author

**Sandeep Vemula**  
7+ years experienced SDET | Python, Automation, Selenium, API Testing

---

## ⭐️ Impress Recruiters

This project shows:
- Advanced Python scripting
- Real-time automation capability
- End-to-end test automation
- Clean framework with logging and reporting"# stock-price-monitor" 
