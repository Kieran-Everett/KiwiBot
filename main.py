import discord
import random
import requests


with open('token.txt') as tokenFile:
    token = tokenFile.read()


class MyClient(discord.Client):


    async def on_ready(self): # Fancy async stuff using asyncio
        # Essentially an __init__ method

        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("-------")

    async def on_message(self, message):

        if message.author.id == self.user.id:
            return
        
        # Alice is mean to the bot
        if message.content.startswith("was alice mean to you?") and message.author != "al.is.kinda.cute#2251":
            await message.reply("yes she was :(") # Await lets you multitask without doing thread stuff
        elif message.content.startswith("was alice mean to you?") and message.author == "al.is.kinda.cute#2251":
            await message.reply("you know you were :(")
        
        if message.author == "al.is.kinda.cute#2251" and random.randint(1, 100) == 69:
            print("meanie :confounded:")
        
        
        if "pog" in message.content.lower():
            await message.reply("poggers")
        

        if message.content == "how much of an epic gamer am i?":
            r = requests.get("https://osu.ppy.sh/users/13764285")
            offset = 13
            scoreLen = 5
            if r.status_code == 200:
                globalLocation = r.text.find("global")
                await message.reply("You are epic gamer #{}".format(r.text[globalLocation + offset:globalLocation + offset + scoreLen]))
            else:
                await message.reply("something isn't quite right, {} this should be 200 and not whatever it is now".format(r.status_code))
        
        if "i am" in message.content.lower():
            await message.reply("Hi" + message.content[message.content.find("i am")+4:] + ", nice to meet you")
        elif "i'm" in message.content.lower():
            await message.reply("Hi" + message.content[message.content.find("i'm")+3:] + ", nice to meet you")
        elif "im" in message.content.lower():
            await message.reply("Hi" + message.content[message.content.find("im")+2:] + ", nice to meet you")


client = MyClient()
client.run(token)