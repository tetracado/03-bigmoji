# This example requires the 'message_content' intent.
import bmhidden
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #print("CONTENT: ")
    #print(message.content)
    if message.content.startswith('<:'):
        emid=message.content.split(":")[2]
        emid=emid[:(len(emid)-1)]
        emurl="https://cdn.discordapp.com/emojis/"+emid+".png"
        await message.channel.send(emurl)


    #if message.content.startswith('$hello'):
    #    await message.channel.send('Hello!')

client.run(bmhidden.token)
