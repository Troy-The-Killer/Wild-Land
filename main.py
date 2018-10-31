#!/usr/bin/env python3.6

import discord
import configuration
import asyncio

# Client:
client = discord.Client()

# Variáveis:
token = configuration.Token()

# Cores:
Red = 0xFF0000
Green = 0x00FF00
Blue = 0x0000FF

# Online:
@client.event
async def on_ready():
    print(f'──────────────────────────')
    print(f'Nome: {client.user.name}')
    print(f'  ID: {client.user.id}')
    print(f'──────────────────────────')

    membros = str(len(set(client.get_all_members())))

    while True:
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name=f'💞 {membros} Membros'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name=f'💞 Criador: Joty#6922'))

client.run(token)