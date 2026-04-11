# 🚀 LeetCode Accountability System

A serverless Python-based system that enforces **daily LeetCode consistency** by automatically tracking submissions and sending reminder emails if you skip a day.

---

## 🎯 The Problem

Initially, this system was built as a **local background script** that:

* Ran continuously using a `while True` loop
* Checked LeetCode activity at fixed intervals
* Sent reminder emails if no submission was made

### ❌ Limitations of the Local Approach

* Required the user's **laptop to stay ON 24/7**
* Consumed unnecessary system resources
* Stopped working if the terminal was closed
* Not practical for real-world usage

---

## ⚡ The Solution (Architecture Upgrade)

The system was redesigned using a **serverless cron-based architecture** powered by GitHub Actions.

### 🔥 Key Idea:

Instead of running continuously, the system:

> Executes only when needed, on cloud infrastructure.

---

## 🧠 How It Works Now

1. GitHub Actions triggers the workflow every *N hours* (cron job)
2. A fresh virtual machine (`ubuntu-latest`) is created
3. The repository is cloned and dependencies are installed
4. The Python script runs:

   * Fetches LeetCode submissions
   * Checks if a problem was solved today (UTC)
   * Sends email if inactive
5. The machine is destroyed after execution

---

## 🔄 Execution Model

**Old Model (Local Daemon):**

```
while True:
    check()
    sleep()
```

**New Model (Serverless Cron):**

```
Every N hours:
    spin up machine → run script → shut down
```

---

## 🔐 Secure Configuration

Sensitive data is handled using **GitHub Secrets**:

* `SENDER_EMAIL`
* `APP_PASSWORD`
* `LEETCODE_USERNAME`
* `TARGET_EMAIL`

> No credentials are stored in the repository or hardcoded.

---

## ⚙️ Tech Stack

* **Language:** Python 3
* **API Handling:** `requests` (LeetCode GraphQL API)
* **Email Service:** `smtplib` via Gmail SMTP
* **Automation:** GitHub Actions (cron-based execution)
* **Environment Management:** `python-dotenv`

---

## 📦 Setup Instructions

### 1. Clone Repository & Setup Environment

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

### 3. Configure Secrets (IMPORTANT)

Since this project runs on GitHub Actions:

1. Go to your repository → **Settings**
2. Navigate to: **Secrets and variables → Actions**
3. Add the following secrets:

```
SENDER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_16_character_app_password
LEETCODE_USERNAME=your_username
TARGET_EMAIL=your_email@gmail.com
```

---

### 4. Workflow Configuration

The automation is defined in:

```
.github/workflows/leetcode_tracker.yml
```

Example schedule:

```yaml
- cron: '0 */2 * * *'  # Runs every 2 hours
```

You can also trigger it manually using:

```
workflow_dispatch
```

---

## 🧪 Example Behavior

| Scenario              | Outcome                     |
| --------------------- | --------------------------- |
| Submission made today | ✅ No email sent             |
| No submission         | 📧 Reminder sent            |
| Still inactive        | 🔁 Repeated checks via cron |

---

## 🚧 Future Improvements

* Multi-user support (database integration)
* SMS notifications (via APIs like Twilio)
* Web dashboard for tracking streaks
* SaaS version with user authentication

---

## 🧨 Why This Exists

Motivation is unreliable. Systems are not.

This project removes friction and excuses by:

> **automating discipline through external enforcement**

---

## 📌 One-Line Summary

> A serverless system that uses cron-based cloud execution to track LeetCode activity and enforce daily consistency via automated reminders.

---
BY- 
T.VAISHNAV 😃👾
