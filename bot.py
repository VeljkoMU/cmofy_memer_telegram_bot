import copy
import re
import sys
from flask import request
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
from haiku_generator import generate_haiku

class ComfyMemerBot:

    user_set: set((int, str, Update)) = set()


    def __init__(self, memes_api, max_chats=5):
        self.api = memes_api
        self.max_chats = max_chats
        self.commands = "TO SEND A MESSAGE TO ALL THE USERS USING THE BOT:\n/broadcast <MESSAGE>\n\nLIST ALL USERS USING THE BOT:\n/getusers\n\nTELL THE BOT TO SEND YOU A MEME:\nYo bro, hit me up with a meme bro!\nYo, meme me up!\nOR ANY OTHER MESSAGE CONTAINING \"meme\"\n\nGET INFO ON TH GUY WHO MADE THIS AND A GITHUB TO THE CODE:\nShow me your maker!\n\nGET THE BOT TO SEND YOU MEMES EVERY X MINUTES:\nYo bro, can I get a dank meme every X minutes?\nMeme me up every X minutes bro!\nSend some memes to me me every X\nWHERE X IS THE NUMBER OF MINUTES\n\nTO STOP THE MEMES JUST DO:\n/unsubscribe\n\nTO GET THE BOT TO GENERATE A HAIKU:\nWrite me a haiku\nOR ANY OTHER MESSAGE CONTAINING \"haiku\""

        

    def get_command_handler_functions(self):
        # Add command handler functions here and return them to be initialized to dispatcher when the bot is created
        def start(update: Update, context: CallbackContext):
            msg= f"Sup king, cool username {update.effective_user.name}, welcome to the comfiest of the comfy meme sharing chatbots.\nHere are some of the commands you can use:"
            ComfyMemerBot.user_set.add((update.effective_user.id, update.effective_user.name, copy.copy(update)))
            update.message.reply_text(msg)
            update.message.reply_text(self.commands)
            

        
        def getusers(update: Update, context: CallbackContext):
            msg=""
            for user in ComfyMemerBot.user_set:
                msg+= user[1] + " "
            update.message.reply_markdown_v2(msg)



        def broadcast(update: Update, context: CallbackContext):
            message = update.message.text
            message = message[10:]
            user = update.effective_user.name

            msg= f"Hear ye! Hear ye! \n A wayfearing traveller from a distant land sends us a message! \n Is he a friend? A foe? Judge for yourselves. \n His name {user}\nThe message reads: "
            for _, _, updt in ComfyMemerBot.user_set:
                updt.message.reply_text(msg)
                updt.message.reply_text(message)

        

        def unsubscribe(update: Update, context: CallbackContext):
            job_name = str(update.message.chat_id)
            jobs = context.job_queue.get_jobs_by_name(job_name)
            for job in jobs:
                job.schedule_removal()

            update.message.reply_text("Alright, I won't be seneding you memes no more, your loss tho!")


        return [getusers, start, broadcast, unsubscribe]



    def get_message_handler_functions(self, update: Update, context: CallbackContext):
        # Same but for messages, not commands, add a hanlder function and call it in an if branch
        def getmeme(update: Update, context: CallbackContext):
            res = requests.get(self.api).json()
            meme_src = res["url"]

            update.message.reply_text("Here you go king!")
            update.message.reply_photo(meme_src)



        def creator(update: Update, context: CallbackContext):
            msg = f"Behond! My maker, my creator!\nemail: veki.uskovic@gmail.com \nmy github repo: https://github.com/VeljkoMU/cmofy_memer_telegram_bot"
            update.message.reply_text(msg)



        def send_memes_to_subscriber(context: CallbackContext):
            res = requests.get(self.api).json()
            meme_src = res["url"]
            context.bot.send_message(context.job.context, text="Your schedualed meme king, keep grinding!")
            context.bot.sendPhoto(context.job.context, photo=meme_src)

        def subscribe_to_memes(update: Update, context: CallbackContext):
            chat_id = update.message.chat_id

            timer = [int(s) for s in update.message.text.split() if s.isdigit()][0]
            timer = timer if timer>0 else -timer

            context.job_queue.run_repeating(send_memes_to_subscriber, timer * 60, context=chat_id, name=str(chat_id))
            update.message.reply_text("Sure thing bro, I'll be sending you all the dankest memes.")

        

        def haiku(update: Update, context: CallbackContext):
            haiku = generate_haiku()
            update.message.reply_text(f"For your reading pleasure, {update.effective_user.name}-San:")
            update.message.reply_text(haiku)



        msg = update.message.text
        if re.match(r".*meme\s.*", msg):
            getmeme(update, context)
        elif re.match(r".*maker.*", msg):
            creator(update, context)
        elif re.match(r".*every [0-9]+.*", msg):
            subscribe_to_memes(update, context)
        elif re.match(r".*haiku.*", msg):
            haiku(update, context)
        else:
            update.message.reply_text("I can't understand you bro! Haven't you read the commands? Just do /start")



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
