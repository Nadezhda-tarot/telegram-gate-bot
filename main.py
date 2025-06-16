import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")
CHAT_LINK = os.getenv("CHAT_LINK")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    try:
        member = await context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user.id)
        if member.status in ["member", "administrator", "creator"]:
            await update.message.reply_text(f"Вы подписаны на канал! Вот ссылка для входа в чат: {CHAT_LINK}")
        else:
            raise Exception("Not a member")
    except:
        await update.message.reply_text(f"Пожалуйста, подпишитесь на канал {CHANNEL_USERNAME} и нажмите /start снова.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()