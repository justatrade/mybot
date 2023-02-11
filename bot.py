import config
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

logging.basicConfig(filename='bot.log', level=logging.INFO)


async def greet_user(update, context):
    print('The command was get: /start')
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    await update.message.reply_text(user_text)

def main() -> None:
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", greet_user))
    app.add_handler(MessageHandler(filters.TEXT, talk_to_me))
    logging.info('Bot was started')
    app.run_polling()


if __name__ == '__main__':
    main()