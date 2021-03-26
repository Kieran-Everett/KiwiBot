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

        self.activePolls = {}
    

    def parseMessage(self, message):

        question = ""
        answers = []
        currentAnswer = ""
        appending = False
        firstArg = True

        for char in message:
            if char == '"' and appending == False: # Opening speech marks
                appending = True
            elif char == '"' and appending == True: # Closing speech marks
                appending = False
                if firstArg: # If it is the first argument then that is the question
                    question = currentAnswer
                    currentAnswer = ""
                    firstArg = False
                else: # Else it creates a new answer with zero votes
                    answers.append(currentAnswer)
                    currentAnswer = ""
            elif appending == True:
                currentAnswer += char


    async def on_message(self, message):

        if message.author.id == self.user.id:
            return
        

        # Proper bot commands start with a '!k'
        if message.content.startswith("!k"):

            splitMessage = message.content.split()
            
            if splitMessage[1] == "poll" and splitMessage[2] == "create":
                question, answers = self.parseMessage(message.content)
                pollID = len(self.activePolls) + 1

                self.activePolls[ str(pollID) ] = { "Question": question }

                answerID = 1
                for answer in answers:
                    self.activePolls[ str(pollID) ][ str(answerID) ] = { "answer": answer, "votes": 0 }
                    answerID += 1
                
                await message.reply("Created poll!")
                toSend = "New poll: " + self.activePolls[ str(pollID) ][ "question" ] + "\n"
                answerID = 0
                for answer in self.activePolls[ str(pollID) ]:
                    if answerID == 0:
                        answerID += 1
                    else:
                        toSend += answerID + ") " + answer[ str(answerID) ]["answer"] + "\n"
                await message.channel.send(toSend)

            elif splitMessage[1] == "poll" and splitMessage[2] == "vote": # usage: !k poll vote {pollID} {answerID}
                try:
                    activePolls[int(splitMessage[3])-1].vote(int(splitMessage[4]))
                except:
                    await message.reply("Error: Enter a valid poll ID")
        

        # Alice is mean to the bot
        if message.content.startswith("was alice mean to you?") and message.author != "al.is.kinda.cute#2251":
            await message.reply("yes she was :(") # Await lets you multitask without doing thread stuff
        elif message.content.startswith("was alice mean to you?") and message.author == "al.is.kinda.cute#2251":
            await message.reply("you know you were :(")
        
        if message.author == "al.is.kinda.cute#2251" and random.randint(1, 100) == 69:
            await message.reply("meanie :confounded:")
        
        
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


if __name__ == "__main__":
    client = MyClient()
    client.run(token)