# 🚀 TeleOps AI

TeleOps AI is a lightweight Telegram-based AI operations assistant designed for personal productivity, email management, reminders, and automation.

Built for low-resource VPS environments like Oracle Cloud Free Tier (AMD VM 1GB RAM).

---

# ✨ Features

## 📧 Gmail AI Assistant

* Summarize latest emails
* Search emails by keyword
* Detect OTP codes
* Detect security alerts
* AI-powered email summaries

## 📅 Event Reminder System

* Add events from Telegram
* View upcoming events
* Delete events
* Automatic reminder notifications

## 🤖 AI Integration

* Groq API integration
* Fast AI responses
* Lightweight cloud inference
* VPS-friendly architecture

## 🔒 Security

* Telegram admin-only access
* Hidden FastAPI docs
* HTTPS support
* Webhook secret validation
* Sensitive files excluded from Git

---

# 🛠️ Tech Stack

* Python
* FastAPI
* python-telegram-bot
* Groq API
* Gmail API
* APScheduler
* SQLite
* Nginx
* Oracle Cloud VPS

---

# 📦 Commands

| Command                   | Description             |
| ------------------------- | ----------------------- |
| `/start`                  | Start TeleOps AI        |
| `/latest`                 | Summarize latest emails |
| `/find keyword`           | Search emails           |
| `/otp`                    | Extract OTP codes       |
| `/security`               | Show security alerts    |
| `/event YYYY-MM-DD title` | Add event               |
| `/today`                  | Show all events         |
| `/deleteevent ID`         | Delete event            |

---

# 📌 Example Usage

## Add Event

```bash
/event 2026-05-10 Birthday is comming!
```

---

## Search Emails

```bash
/find Ollama
```

---

## Extract OTPs

```bash
/otp
```

---

# ⚙️ Installation

## 1. Clone Repo

```bash
git clone https://github.com/YOUR_USERNAME/TeleOps-AI.git
cd TeleOps-AI
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment

Create `.env`

```env
TELEGRAM_BOT_TOKEN=
TELEGRAM_ADMIN_ID=
GROQ_API_KEY=
WEBHOOK_SECRET=
APP_URL=https://ai.example.com
```

---

## 5. Add Google Credentials

Place:

* `credentials.json`
* `token.json`

inside project root.

---

## 6. Run Server

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

# 🌐 Production Deployment

Recommended stack:

* Oracle Cloud Free Tier VPS
* Ubuntu 22.04+
* Nginx Reverse Proxy
* Cloudflare DNS + SSL
* HTTPS via Certbot

---

# 🔥 Future Plans

* Multi-email support
* Outlook/Yahoo integration
* Google Calendar sync
* AI daily briefing
* Flight & hotel search assistant
* Inline Telegram buttons
* PostgreSQL support
* AI workflow automation

---

# ⚠️ Important Security Notes

Never upload these files to GitHub:

```gitignore
.env
token.json
credentials.json
venv/
```

---

# 📄 License

MIT License

---

# ❤️ Built For

Personal AI operations, productivity, automation, and lightweight cloud infrastructure experiments.
