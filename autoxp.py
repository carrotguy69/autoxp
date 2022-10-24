import asyncio, discord, json, random, time
from datetime import datetime
from discord.ext import commands

data = None
with open ("config.json", "r") as f:
    data = json.load(f)

if not data["token"]:
    print("You have not set a token in the config.json file, if you need help finding your user token, use this tutorial: https://linuxhint.com/get-discord-token/")

if not data["channel"]:
    print("You have not set any channels for the bot to send messages in. Open config.json and add a channel id")

if not data["messages"]:
    print("You have not set any messages to the bot to send.")

client = discord.Client()

async def send():
    channel = client.get_channel(random.choice(data['channel']))
    msg = random.choice(data["messages"])
    emoji = [x for x in channel.guild.emojis if not x.animated and x.is_usable()]
    msg = random.choice((random.choice(emoji), random.choice(data["messages"])))
    
    print(f"[{datetime.fromtimestamp((time.time())).strftime('%A, %B %d, %Y, %I:%M:%S %p')}] {channel.guild.name} - #{channel.mention}: {msg}")
    await channel.send(msg)

@client.event
async def on_ready():
    while True:
        await send()
        await asyncio.sleep(int(data["cooldown"]))

client.run(data["token"], bot = False)
