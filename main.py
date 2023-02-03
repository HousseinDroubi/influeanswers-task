import requests
import random
import pandas as pd

# Get 5 random numbers
randomlist = random.sample(range(1, 30), 5)

# Convert numbers to string
random_list_str = []
for x in randomlist:
  if(x>=10):
    random_list_str.append(str(x))
  else:
    random_list_str.append("0"+str(x))

# The below function is to download text file
def download_file(day):
    date = "2014-06-"+day  
    base_url = "https://chatlogs.planetrdf.com/swig/"+date+".txt"  
    target_txt_path = "chat-days/"+date+".txt"
    response = requests.get(base_url)
    response.raise_for_status() 
    with open(target_txt_path, "wb") as f:
        f.write(response.content)
    print("File downloaded.")

# The below function is to remove unwanted additions
def clear_file(day):
    date = "2014-06-"+day
    with open("chat-days/"+date+'.txt') as f:
        contents = f.read()
    my_list = contents.split("\n")
    cleared_list = []    
    
    for index, val in enumerate(my_list):
        # The unwanted additions in this case are 'has quit', 'has left' and 'has joined' which are the most repeated words.
        has_quit = 'has quit'
        has_joined = 'has joined'
        has_left = 'has left'
        if(has_quit in val ):
            my_list[index]=''    
        if(has_joined in val ):
            my_list[index]=''
        if(has_left in val ):
            my_list[index]=''

    # Build a new list
    for index,val in enumerate(my_list):
        if(not val.__eq__('')):
            cleared_list.append(date+" "+val)

    # Edit saved files by overwriting
    file = open("chat-days/"+date+'.txt','w')
    for item in cleared_list:
        file.write(item+"\n")
    file.close()

# The below function is to read contents from the text file
all_chat = ""
def read_file(day):
    global all_chat
    date = "2014-06-"+day
    with open('chat-days/'+date+'.txt') as f:
        contents =f.read()
    all_chat=all_chat+contents

# The below function is to split conversations by new line
def chat_to_list(chats):
    my_list = chats.split("\n")
    my_list.pop(len(my_list)-1)
    return my_list    