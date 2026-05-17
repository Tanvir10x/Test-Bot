import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, CopyTextButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

API_TOKEN = "8466000076:AAGgxdomtK8g9tGGdqI6B17ywyWTo9gymHI"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    copy_button = InlineKeyboardButton(
        text="123-456", 
        copy_text=CopyTextButton(text="123456")
    )
    
    keyboard = [[copy_button]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "OTP Receive 💥", reply_markup=reply_markup
    )

if __name__ == "__main__":
    application = ApplicationBuilder().token(API_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    
    application.run_polling()
