import selfcord
import os
from dotenv import load_dotenv
from typing import List

load_dotenv()

bot_token = os.getenv("ACCOUNT_TOKEN")

# tries to self react using the given emojis as a list
async def self_react(message, emoji):
    for e in emoji:
        try:
            await message.add_reaction(e)
        except Exception as x:
            print(x)


print(f'Acc Token is {bot_token}') # this was implemented as a debugging feature
class MyClient(selfcord.Client):
    async def on_ready(self):
        print('Logged on as', self.user) # if you're logged in you will see your name printed

    async def on_message(self, message):
        if message.author.id == self.user.id:
            print('message is', message)
            #await message.add_reaction('\U0001F62D')
            #await message.add_reaction(':thonk:961423622147309618')
            #await message.add_reaction(':patrickNotes:1202293366465757315')
            emoji = ['\U0001F62D',':thonk:961423622147309618',':patrickNotes:1202293366465757315']
            await self_react(message,emoji) # if you don't use this function, the bot will stop as soon as he find an invalid emoji.

            



client = MyClient()
client.run(bot_token)