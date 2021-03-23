import discord
import random


with open('token.txt') as tokenFile:
    token = tokenFile.read()


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("-------")

    async def on_message(self, message):

        if message.author.id == self.user.id:
            return
        
        # Alice is mean to the bot
        if message.content.startswith("was alice mean to you?") and message.author != "al.is.kinda.cute#2251":
            await message.reply("yes she was :(")
        elif message.content.startswith("was alice mean to you?") and message.author == "al.is.kinda.cute#2251":
            await message.reply("you know you were :(")
        
        if message.author == "al.is.kinda.cute#2251" and random.randint(1, 100) == 69:
            print("meanie :confounded:")
        
        
        if "pog" in message.content.lower():
            await message.reply("poggers")


client = MyClient()
client.run(token)