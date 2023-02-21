# This example requires the 'message_content' intent.

import discord
import config as conf
import schedule as sched
from datetime import date



intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):

    if message.author == client.user:
        return 

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
    if date.today().day != 21:
        return
    else:    
        print("It's the first of the Month...")
        message.channel.send("It's the first of the mooooonth... https://youtu.be/4j_cOsgRY7w?t=9")
        return

# sched.every().day.at("14:17").do(bone_message)
"""


client.run(conf.secret_token)
