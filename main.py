from bot import ComfyMemerBot

TOKEN = "My_Token"
API ="https://meme-api.herokuapp.com/gimme"

if __name__=="__main__":
    bot = ComfyMemerBot(API)
    bot.run(TOKEN)