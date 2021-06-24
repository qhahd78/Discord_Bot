import discord
import json
import os
from api import cat, dog

client = discord.Client()

with open("discordkey.json","r") as key_file:
    key = json.load(key_file)

@client.event
async def on_ready(): 
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): 
    if message.author == client.user:
        return 
    elif message.content.startswith('!울어라고양이'):
        await message.channel.send('야옹!')
    elif message.content.startswith('!짖어라강아지'):
        await message.channel.send('멍멍!')
    elif message.content.startswith('!김하온'):
        await message.channel.send('안녕 나를 소개하지')
    elif message.content.startswith('!고양이사진'):
        embed = discord.Embed(title="고양이 랜덤 사진", description="고양이지롱", color=0x62c1cc)
        embed.set_footer(text="랜덤야옹이다!")
        embed.set_thumbnail(url=cat())
        await message.channel.send(embed=embed)
    elif message.content.startswith('!강아지사진'):
        embed = discord.Embed(title="강아지 랜덤 사진", description="강아지지롱", color=0x62c1cc)
        embed.set_footer(text="랜덤강아지!")
        embed.set_thumbnail(url=dog())
        await message.channel.send(embed=embed)
    elif message.content.startswith('!나가'):
        await client.change_presence(status=discord.Status.offline)
    elif message.content.startswith('!핑'):
        await message.channel.send('퐁!')
client.run(key["KEY"])