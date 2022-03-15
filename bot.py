import logging
import re
from flask import request

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

class ComfyMemerBot:

    user_set = set()

    def __init__(self, memes_api, max_chats=5):
        self.api = memes_api
        self.max_chats = max_chats
        
    def get_command_handler_functions(self):
        # Add command handler functions here and return them to be initialized to dispatcher when the bot is created
        def start(update: Update, context: CallbackContext):
            msg= f"Sup king, cool username {update.effective_user.username}, welcome to the comfiest of the comfy meme sharing chatbots.\nHere are some of the commands you can use:"
            ComfyMemerBot.user_set.add((update.effective_user.id, update.effective_user.name))
            update.message.reply_text(msg)
        
        def getusers(update: Update, context: CallbackContext):
            msg=""
            for user in ComfyMemerBot.user_set:
                print(user)
                msg+= user[1] + " "
            update.message.reply_markdown_v2(msg)

        return [start, getusers]

    def get_message_handler_functions(self, update: Update, context: CallbackContext):
        # Same but for messages, not commands, add a hanlder function and call it in an if branch
        def getmeme(update: Update, context: CallbackContext):
            res = requests.get(self.api).json()
            print(res)
            meme_src = res["url"]

            update.message.reply_text("Here you go king!")
            update.message.reply_photo(meme_src)

        def creator(update: Update, context: CallbackContext):
            msg = f"Behond! My maker, my creator!\ntelegram: \nmail: \nmy github repo: "
            update.message.reply_text(msg)

        msg = update.message.text
        if re.match(r".*meme.*", msg):
            getmeme(update, context)
        elif re.match(r".*maker.*", msg):
            creator(update, context)
        return [(r"*meme*", ), (r"*maker*", creator)]

    def initDispatcher(self, updater: Updater):
        self.dispetcher = updater.dispatcher

        for func in self.get_command_handler_functions():
            self.dispetcher.add_handler(CommandHandler(func.__name__, func))
        
            self.dispetcher.add_handler(MessageHandler(Filters.text, self.get_message_handler_functions))

    def run(self, token: str):
        updater = Updater(token)

        self.initDispatcher(updater)

        updater.start_polling()

        updater.idle()
