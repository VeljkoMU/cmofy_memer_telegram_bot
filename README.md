# cmofy_memer_telegram_bot
  <h1>
NOW AVAILABLE ON TELEGRAM!
https://t.me/comfy_memer_bot
  </h1>
  Might not be always up though.

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
/broadcast <MESSAGE> - send a message to all the users who are using the bot
  <br>
 Send me memes every X minutes. - sends the user memes every c minutes
  </br>
/unsubscribe - stops sending the memes to the user
  <br>
Show me your maker! - shows the user my email and a link to this repository.
  Write me a haiku! - generates a haiku for the user
  </br>
  
  
Feel free to fork this code, add your own handler functions and play around with it
  <br>

  </bold>
