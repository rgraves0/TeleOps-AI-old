from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI, Request, HTTPException
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from ai_utils import ask_ai
from calendar_utils import (
    add_event,
    list_events,
    delete_event,
    get_due_events,
    mark_reminded,
)
from config import *
from gmail_utils import get_latest_emails, search_emails
from security import authorized

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None
)

telegram_app = ApplicationBuilder().token(
    TELEGRAM_BOT_TOKEN
).build()

scheduler = AsyncIOScheduler()

async def check_reminders():
    today = datetime.now().strftime("%Y-%m-%d")

    events = get_due_events(today)

    for event in events:
        event_id, title, event_date = event

        await telegram_app.bot.send_message(
            chat_id=TELEGRAM_ADMIN_ID,
            text=f"⏰ Reminder\n\n{title}\n📅 {event_date}"
        )

        mark_reminded(event_id)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not authorized(update.effective_user.id):
        return

    await update.message.reply_text(
        "TeleOps AI Online ✅"
    )

async def latest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    emails = get_latest_emails()

    summary = ask_ai(
        "Summarize these emails briefly:\n\n" + "\n".join(emails)
    )

    await update.message.reply_text(summary)

async def find(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args)

    emails = search_emails(query)

    summary = ask_ai(
        f"Search query: {query}\n\nEmails:\n" + "\n".join(emails)
    )

    await update.message.reply_text(summary)

async def otp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    emails = search_emails("OTP OR verification code")

    result = ask_ai(
        "Extract OTP codes:\n\n" + "\n".join(emails)
    )

    await update.message.reply_text(result)

async def security(update: Update, context: ContextTypes.DEFAULT_TYPE):
    emails = search_emails(
        "security OR suspicious OR login"
    )

    result = ask_ai(
        "Find security alerts:\n\n" + "\n".join(emails)
    )

    await update.message.reply_text(result)

async def add_calendar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text(
            "Usage: /event YYYY-MM-DD Event Name"
        )
        return

    event_date = context.args[0]
    title = " ".join(context.args[1:])

    add_event(title, event_date)

    await update.message.reply_text(
        f"✅ Event added\n\n📅 {event_date}\n📝 {title}"
    )

async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    events = list_events()

    if not events:
        await update.message.reply_text("No events.")
        return

    lines = []

    for event in events:
        event_id, title, event_date = event
        lines.append(
            f"{event_id}. 📅 {event_date} — {title}"
        )

    await update.message.reply_text(
        "\n".join(lines)
    )

async def delete_calendar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Usage: /deleteevent ID"
        )
        return

    event_id = int(context.args[0])

    delete_event(event_id)

    await update.message.reply_text(
        f"🗑️ Deleted event {event_id}"
    )

telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CommandHandler("latest", latest))
telegram_app.add_handler(CommandHandler("find", find))
telegram_app.add_handler(CommandHandler("otp", otp))
telegram_app.add_handler(CommandHandler("security", security))
telegram_app.add_handler(CommandHandler("event", add_calendar))
telegram_app.add_handler(CommandHandler("today", today))
telegram_app.add_handler(CommandHandler("deleteevent", delete_calendar))

@app.on_event("startup")
async def startup():
    await telegram_app.initialize()
    await telegram_app.start()

    scheduler.add_job(
        check_reminders,
        "interval",
        minutes=1
    )

    scheduler.start()

    await telegram_app.bot.set_webhook(
        url=f"{APP_URL}/webhook/{WEBHOOK_SECRET}"
    )

@app.post("/webhook/{secret}")
async def webhook(secret: str, request: Request):
    if secret != WEBHOOK_SECRET:
        raise HTTPException(status_code=403)

    data = await request.json()

    update = Update.de_json(
        data,
        telegram_app.bot
    )

    await telegram_app.process_update(update)

    return {"ok": True}

@app.get("/healthz")
async def health():
    return {"status": "running"}
