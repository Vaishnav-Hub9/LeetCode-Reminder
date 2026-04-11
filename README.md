# 🚀 LeetCode Accountability System

A lightweight Python-based background service that enforces **daily LeetCode consistency** by automatically tracking your submissions and sending reminder emails if you miss a day.

---

## 🎯 What It Does

* Monitors your **public LeetCode activity** using your username
* Uses **UTC time (LeetCode reset time)** for accurate daily tracking
* Sends **automated email reminders** if no submission is detected
* Runs continuously as a **local background daemon**
* Requires **zero manual input after setup**

---

## 🧠 How It Works

1. Fetches your recent submissions using LeetCode’s GraphQL API
2. Extracts the latest submission timestamp
3. Compares it with the current UTC date
4. If no submission is found for today:

   * Sends a reminder email
   * Repeats at fixed intervals until you solve a problem

---

## ⚙️ Tech Stack

* **Language:** Python 3
* **API Handling:** `requests` (LeetCode GraphQL queries)
* **Scheduling:** `schedule` (continuous background execution)
* **Email Service:** `smtplib` via Gmail SMTP
* **Environment Management:** `python-dotenv`

---

## 📦 Setup Instructions

### 1. Clone & Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
# Gmail credentials (App Password required)
SENDER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_16_character_app_password

# Tracking configuration
LEETCODE_USERNAME=your_leetcode_username
TARGET_EMAIL=your_email@gmail.com
INTERVAL_HOURS=2
```

> ⚠️ Make sure `.env` is added to `.gitignore` to keep credentials secure.

---

### 4. Run the System

```bash
python main.py
```

* Runs an **initial check immediately**
* Continues monitoring in the background at your defined interval
* Keep the terminal open to keep the service running

---

## 🔐 Security Notes

* Uses **Gmail App Passwords** (not your real password)
* Credentials are stored locally via `.env`
* No sensitive data is hardcoded or exposed

---

## 🧪 Example Behavior

| Scenario                   | Outcome                           |
| -------------------------- | --------------------------------- |
| You solved a problem today | ✅ No email sent                   |
| You didn’t solve           | 📧 Reminder sent                  |
| Still inactive             | 🔁 Repeated reminders at interval |

---

## 🚧 Future Improvements

* Multi-user support (database integration)
* SMS notifications (via APIs like Twilio)
* Web dashboard for tracking streaks
* Deployment as a cloud service (24/7 uptime)

---

## 🧨 Why This Exists

Consistency beats motivation.

This system removes excuses by **automating accountability** — if you skip, it reminds you until you don’t.

---

## 📌 One-Line Summary

> A no-excuses system that tracks your LeetCode activity and forces daily consistency through automated reminders.
