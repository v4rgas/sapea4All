import discord
from discord.ext import commands
import asyncio


channelID = 0 #id canal
TOKEN = ''

with open('msg.txt', 'a') as f:
    # Client de Discord.py
    client = commands.Bot(command_prefix='-')

    # Simple evento ready para avisar cuando el Bot esta listo

    @client.event
    async def on_ready():
        print('Iniciado como ' + client.user.name)

    @client.event
    async def on_message(message):
        # Ignoremos todos los mensajes que son de otros Bots
        if message.author.bot is True:
            return
        if str(message.content) != '' and (message.channel.id == channelID:
            print(f'{message.author}: {message.content}', file=f)

    client.run(TOKEN)
