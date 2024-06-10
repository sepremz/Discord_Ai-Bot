# Discord_Ai-Bot
![Screenshot 2024-06-10 172053](https://github.com/sepremz/Discord_Ai-Bot/assets/72527110/1c3b05dc-00d2-4aee-bdf8-44c2fe9d0d23)
Discord_Ai Bot using Python

## Installation

- before you start you have to install discord and google-generativeai by this command: pip install discord google-generativeai
- after download go to Discord Developer Portal and create a Bot!
- in settings go to Bot tab and got to Privileged Gateway Intents then check mark on;Presence Intent and Server Members Intent and Message Content Intent
- then go to Installation tab go to Install link and chose Discord Provided Link, In Guild Install chose Bot and Administrator then copy the link of the bot and paste it in the browser then chose the server that you want to add the bot.
- then go to Bot tab again and press Rest Token; get the token then paste it in 'Discord Token'
- after that, you have to get the Gemini Api key: you can get it from this link: https://ai.google.dev/gemini-api/docs/api-key, and when you get the key paste it in 'Gemini_Api_Key'

## Customization
- you can change the prefix of the bot in the python file! bot = commands.Bot(command_prefix='/', intents=intents)
- and you can alose change the key word after the prefix! @bot.command(name='ai')
- in my option I used prefix "/" and the key word is "ai"
