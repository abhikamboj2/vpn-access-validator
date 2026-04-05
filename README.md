# 🚀 VPN Access Validator

## 📌 Overview

VPN Access Validator is an automated testing system built using Python and Selenium to verify whether a website correctly enforces VPN-based access restrictions.

It simulates user interactions across multiple flows (Home & Auto), tests with different ZIP codes, and validates whether access is properly blocked when expected.

---

## 🔥 Problem Solved

Many enterprise applications rely on VPN-based access control. Manually verifying access behavior across multiple scenarios is repetitive and error-prone.

This project automates the process and helps detect:

* ❌ Unauthorized access without VPN
* ✅ Correctly blocked requests

It also sends alerts when unexpected behavior is detected.

---

## ⚙️ Features

* ✅ Automated browser testing using Selenium
* ✅ Supports multiple flows (Home & Auto)
* ✅ Tests multiple ZIP codes
* ✅ Detects access control issues
* ✅ Logs execution details
* ✅ Generates structured results
* ✅ Sends email alerts for failures

---

## 🧠 How It Works

1. Opens the target website
2. Selects flow (Home / Auto)
3. Enters ZIP code
4. Checks:

   * If **"Access Denied" → Expected behavior**
   * If page loads → **Issue detected**
5. Stores results
6. Sends email alert if any issue is found

---

## 🛠️ Tech Stack

* Python
* Selenium
* SMTP (Email Automation)
* python-dotenv

---

## 📂 Project Structure

```
vpn-access-validator/
│
├── main.py
├── check_status.py
├── email_automation.py
├── zip_code.py
│
├── logs/
│   └── app.log
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

### 1. Clone Repository

```bash
git clone https://github.com/abhikamboj2/vpn-access-validator.git
cd vpn-access-validator
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure Environment Variables

Create a `.env` file:

```env
Base_URL=your_website_url
Email_Address=your_email@gmail.com
Email_Password=your_app_password
Sender_Email_Address=receiver_email@gmail.com
```

⚠️ Do NOT use your actual Gmail password. Use an App Password.

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📧 Email Alerts

If any ZIP code is **NOT blocked (unexpected behavior)**, the system sends an email alert with details.

---

## 📊 Sample Output

```
Zip: 85054 | Flow: Home | Status: BLOCKED
Zip: 85054 | Flow: Auto | Status: NOT_BLOCKED
```
## 🔧 Customization

This project is tailored for a specific website and access validation workflow.

If you plan to use it for another application, you will need to:
- Update Selenium locators in `check_status.py`
- Modify flow logic (Home / Auto or equivalent)
- Adjust validation conditions (e.g., "Access Denied" checks)
- Update input fields such as ZIP code or other parameters

Since web structures vary, minor changes in DOM may require updates to the automation logic.

---

## ⚠️ Notes

* Ensure `.env` is not committed to GitHub
* Logs are stored in `logs/app.log`
* Use Chrome browser with Selenium

---

## 👨‍💻 Author

Abhi Kamboj
