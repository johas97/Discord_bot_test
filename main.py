import os
import discord
import requests 
import json
from pprint import pprint 
client = discord.Client()


def get_meme(): 
  response = requests.get("https://meme-api.herokuapp.com/gimme")
  json_data = json.loads(response.text)
  return json_data
  



@client.event 
async def on_redy () : 
  print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(messege): 
  if messege.author == client.user: 
    return

  if messege.content.startswith('summon'):
    json_data = get_meme()
    meme_title = json_data['title']
    meme_pic = json_data['preview'][-1]
    await messege.channel.send(meme_title)
    await messege.channel.send(meme_pic)

client.run(os.environ['bot_token'])

