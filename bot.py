# This example requires the 'message_content' intent.

import discord
import config as conf
import schedule as sched
from datetime import date


# Intents allow the bot to have the ability to receive and send requests. 
# https://discordpy.readthedocs.io/en/stable/api.html#discord.Intents

intents = discord.Intents.default()
intents.message_content = True

# turns on the intents in a keyword `client` that will be used to grab data like
# user names and to create events, decorators used to declare async events. 
# https://discordpy.readthedocs.io/en/stable/api.html?highlight=client%20event#discord-api-events
# https://discordpy.readthedocs.io/en/stable/api.html?highlight=client%20event#discord.Client.event
client = discord.Client(intents=intents)


@client.event
# on_ready() is called when the conection is made. 
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
# on_message() is called when a message is sent to the discord server/channel. 
async def on_message(message):
    # keeps the bot from responding to itself. 
    if message.author == client.user:
        return 

    # turns the message contents to lower case and checks if it contains
    # the string `$bizzy_bone`. Then, the bot usses `message.channel.send` 
    # to reply in the channel. 
    if "$bizzy_bone" in message.content.lower():
        await message.channel.send("I Miss my uncle Charles y'all... https://youtu.be/DUBC47Z7i6A?t=99")
        return

    if "$crossroads" in message.content.lower():
        await message.channel.send("What you gonna do?   https://youtu.be/VMYAEHE2GrM?t=52")
        return

#Commented out until I can further work on it. 
"""
@client.event
async def bone_message(message):
    if date.today().day != 1:
        return
    else:    
        print("It's the first of the Month...")
        message.channel.send("It's the first of the mooooonth... https://youtu.be/4j_cOsgRY7w?t=9")
        return

# sched.every().day.at("10:15").do(bone_message)
"""

# turns on the event listeners. Immediately runs on_ready() once connected. 
# conf.secret_token is from the config file. 
client.run(conf.secret_token)

