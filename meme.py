import os
import discord
import requests 
import json
from pprint import pprint 


def get_meme(): 
  response = requests.get("https://meme-api.herokuapp.com/gimme")
  json_data = json.loads(response.text)
  return json_data