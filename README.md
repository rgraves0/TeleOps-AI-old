# TeleOps AI

Telegram-based AI assistant for:
- Gmail summaries
- OTP extraction
- Security alerts
- Event reminders
- Telegram automation

## Commands

/start
/latest
/find
/otp
/security
/event
/today
/deleteevent

## Run

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```
