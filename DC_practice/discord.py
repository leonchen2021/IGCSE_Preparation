import discord

client =  discord.Client()

async def on_ready():
    print('現在のログイン:', client.user)

async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('說'):
        tmp = message.content.split(" ",2)
        if len(tmp) == 1:
            await message.channel.send("何を言いたいですか？")
        else:
            await message.channel.send(tmp[1])

    if message.content == 'ping':
        await message.channel.send('pong')

client.run('あなたのロボット TOKEN')
