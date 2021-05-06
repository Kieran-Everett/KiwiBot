import discord

with open('token.txt') as tokenFile:
    token = tokenFile.read()

vc = None


class MyClient(discord.Client):


    async def on_ready(self): # Fancy async stuff using asyncio
        # Essentially an __init__ method

        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("-------")

        global vc
        channelvc = client.get_channel(835242646417965106)
        vc = await channelvc.connect()

    async def on_message(self, message):

        if message.author.id == self.user.id:
            return
        
        if message.content == "play song":
            vc.play((discord.FFmpegPCMAudio("song.m4a")))
        if message.content == "pause":
            vc.pause()
        if message.content == "resume":
            vc.resume()
        if message.content == "stop":
            vc.stop()


client = MyClient()
client.run(token)