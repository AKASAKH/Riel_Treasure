from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes

# Define the /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Create a keyboard with a "Share Phone Number" button
    keyboard = [[KeyboardButton("Share Phone Number", request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    
    # Send a message with the keyboard
    await update.message.reply_text("Please share your phone number to proceed:", reply_markup=reply_markup)

# Handle the shared contact
async def handle_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.message.contact
    phone_number = contact.phone_number
    user_name = contact.first_name
    
    # Save the phone number (e.g., in a database or variable)
    await update.message.reply_text(f"Thank you, {user_name}! Your phone number ({phone_number}) has been received.")

# Set up the bot
def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    application = Application.builder().token("7900758146:AAE-ybyjf6HYIgoY0g-alXXllC5yKIMcJDI").build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.CONTACT, handle_contact))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()