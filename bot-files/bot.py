import os
from dotenv import load_dotenv
from telegram import Update, InputFile
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Load environment variables from .env file
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
CHANNEL_ID = os.getenv('CHANNEL_ID')

application = Application.builder().token(BOT_TOKEN).build()

# Handler to start the bot
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Welcome to the Web3 Launchpad bot!")

# Handler to handle admin messages
async def handle_message(update: Update, context: CallbackContext):
    if update.message:
        user = update.message.from_user
        if user.username == ADMIN_USERNAME:
            if update.message.text:
                await context.bot.send_message(chat_id=CHANNEL_ID, text=update.message.text)
            elif update.message.photo:
                photo_file = await update.message.photo[-1].get_file()
                await context.bot.send_photo(chat_id=CHANNEL_ID, photo=photo_file.file_id, caption=update.message.caption)
            await update.message.reply_text("Announcement sent!")
        else:
            await update.message.reply_text("You are not authorized to send announcements.")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="This type of message is not supported.")

# Command handler to start the bot
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

# Message handler to handle admin messages
message_handler = MessageHandler(filters.TEXT | filters.PHOTO, handle_message)
application.add_handler(message_handler)

# Start polling for updates
application.run_polling()
