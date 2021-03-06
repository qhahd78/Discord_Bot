# from requests.models import default_hooks
import discord
from discord.ext import commands
import json
import os
import asyncio
from api import cat, dog
from ggutoo import ggutoo

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

# 끝말잇기 게임 코드 
@client.event
async def on_message(message): 
    if message.content.startswith('!끄투'):
        embed = discord.Embed(title="끄투게임", description="끄투게임을 시작합니다. 단어를 입력하세요.")
        await message.channel.send(embed=embed)

        # channel = message.channel 
        # def check(m): 
        #     return m.author == message.author and m.channel == channel
        # input 기다리기
        while True : 
            msg2 = await client.wait_for('message')
            # api로부터 응답 받아와서 저장
            # sentences = api.apifun(msg2.content)

            # 끄투겜으로 보내기 
            sentences = ggutoo.ggutoo(msg2.content)
            # 응답 전송
            # 사전에 없는 단어일 경우
            # if sentences == False : 
            embed = discord.Embed(title=msg2.content, description=sentences)
            await message.channel.send(embed=embed)
            await client.change_presence(status=discord.Status.offline)


            # 사전에 있는 단어일 경우 뜻 출력해주기 
            # else : 
            #     embed = discord.Embed(title=msg2.content, description=str(sentences))
            #     await message.channel.send(embed=embed)

client.run(key["KEY"])
