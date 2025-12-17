import discord

class MyClient(discord.Client):  
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return

    if message.content.startswith('$kitkat'):
      # for i in range(5):
      await message.channel.send('KitKat')
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTQ0OTE1NjY4NTk4NDk2MDU2Mw.GOSEHF.w3BtAvlx5ZJf5CokuApzccJFcWtZw0Zev6gjwg')