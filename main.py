import discord
import random
import requests


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
        

        if message.content == "how much of an epic gamer am i?":
            r = requests.get("https://osu.ppy.sh/users/13764285")
            offset = 13
            scoreLen = 5
            if r.status_code == 200:
                globalLocation = r.text.find("global")
                await message.reply("You are epic gamer #{}".format(r.text[globalLocation + offset:globalLocation + offset + scoreLen]))
            else:
                await message.reply("something isn't quite right, {} this should be 200 and not whatever it is now".format(r.status_code))


client = MyClient()
client.run(token)