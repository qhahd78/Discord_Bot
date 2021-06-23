import discord
import json
client = discord.Client()

with open("discord.json","r") as key_file:
    key = json.load(key_file)

@client.event
async def on_ready(): 
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): 
    if message.author == client.user:
        return 
    elif message.content.startswith('!울어라'):
        await message.channel.send('야옹')
    elif message.content.startswith('!고양이'):
        await message.channel.send('웨옹')
    elif message.content.startswith('!test'):
        embed = discord.Embed(title="제목", description="내용", color=0x62c1cc)
        embed.set_footer(text="하단내용")
        await message.channel.send("test 결과", embed=embed)
client.run(key["KEY"])