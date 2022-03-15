# cmofy_memer_telegram_bot
A simple telegram bot made with the telegram.ext library.
<br>
The bot consists of a class with functions within which handler functions for command and messages can be defined.
<br>
The bot servers as a meme bot which gets memes from a meme generating api (here I use the best one I could find for this prupose which you can check out at https://meme-api.herokuapp.com/gimme,
but any other api can be provided when instanciating the bot class as long as it returns a json response and the image url is contained in a field named 'url', though one could easily change this.)
<br>
<bold>
The bot will support the following commands and messages:
<br>
/start - returns a hello and a list of possible messages
<br>
/getusers- returns a list of names of all the users who used the bot thus far
<br>
any message containing 'meme' in it - returns one random meme
<br>

DO BE IMPLEMENTED
<br>
/broadcast <MESSAGE> - send a message to all the users who are using the bot
  <br>
subsribe me to memes <MINUTES> - subscribes the user to recieve one random meme every X minutes
  <br>
unsubscribe me - unsubscribes the user
  <br>
/story - generates a random ultra-short story and sends it to the user
  <br>
  
Feel free to fork this code, add your own handler functions and play around with it
  <br>
  <h1>
SOON AVAILABLE ON TELEGRAM
  </h1>
  </bold>
