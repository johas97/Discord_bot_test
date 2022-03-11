import os
import discord
import requests 
import json
from pprint import pprint 

taglist = []

class PersonTag: 
  def __init__(self, user_id, emoji_id):
    self.user_id = user_id
    self.emoji_id = emoji_id
    
def add_to_taglist(user_id, emoji_id):
  
  user = PersonTag(user_id, emoji_id)
  taglist.append(user)

# 1) Fixa is tagged funktionen
def is_tagged(user_id):
  for user in taglist:
    print(user.user_id)
    print(user_id)
    if str(user.user_id) == str(user_id):
       return True
       
  return False
# 2) Jobba med att utföra reactions! 
def execute_reactions(user_id):
  actions_to_execute = []
  for user in taglist: 
    if user.user_id == user_id: 
      actions_to_execute.append(user)

  

  
      
    
  
  
       
    
  


  
  
  