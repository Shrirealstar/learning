from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define a function to handle the /start command
def start(update, context):
    update.message.reply_text("Hi! I'm a dummy chatbot. How can I help you?")

# Define a function to handle normal messages
def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    # Create an Updater object and pass your bot's token
    updater = Updater("7081124036:AAH3RZLPV2j4WKnvOaKR4toIoO5RkaHLzYc", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the /start command handler
    dp.add_handler(CommandHandler("start", start))

    # Register the echo handler for normal messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
