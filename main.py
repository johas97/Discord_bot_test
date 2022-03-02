import os
import discord
import requests 
import json
from pprint import pprint 
client = discord.Client()


def get_meme(): 
  response = requests.get("https://meme-api.herokuapp.com/gimme")
  json_data = json.loads(response.text)
  meme_title = json_data['title']
  meme_pic = json_data['preview'][-1]
  print(meme_pic)

@client.event 
async def on_redy () : 
  print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message): 
  if message.author == client.user: 
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hellow!')

#client.run(os.environ['bot_token'])

get_meme()