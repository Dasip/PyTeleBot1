from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler, CommandHandler
from telegram.ext import Filters


TOKEN = "1203054967:AAE6HsWJxFcL8FoNWLlv9_gxPuHcjrdxe6Y"
TG_API = "https://telegg.ru/orig/bot"


def message_handler(update: Update, context):
    context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=update.effective_message.text)


def start_handler(update: Update, context):
    context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text="Привет"
    )

def main():
    my_update = Updater(
        token=TOKEN,
        use_context=True,
        #base_url=TG_API
    )

    m_handler = MessageHandler(Filters.text, message_handler)
    c_handler = CommandHandler("start", start_handler)

    my_update.dispatcher.add_handler(c_handler)
    my_update.dispatcher.add_handler(m_handler)


    my_update.start_polling()
    my_update.idle()


if __name__ == "__main__":
    main()