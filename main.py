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

# The below function is to build the dataframe as required
def list_to_dic(list):
    # Define lists
    chat_day_list=[]
    chat_hour_list=[]
    chat_minute_list=[]
    chat_username_list=[]
    char_message_list=[]

    # Fill lists by dataframe attributes
    for chat in list:
        chat_day = chat[:10]
        chat_day_list.append(chat_day)

        chat_time = chat[11:16]
        hours, minutes = map(str, chat_time.split(':'))
        chat_hour_list.append(hours)
        chat_minute_list.append(minutes)

        username = chat[21:]
        user_chat_list = username.split(">")
        username = user_chat_list[0]
        chat_username_list.append(username)

        index = chat.find(">")
        text = chat[index+2:]
        char_message_list.append(text)

    # Build the the whole list and return it
    dict = {"CHAT_DAY": chat_day_list,
        "CHAT_HOUR": chat_hour_list,
        "CHAT_MINUTE": chat_minute_list,
        "USERNAME":chat_username_list,
        "CHAT_MESSAGE":char_message_list}
    df = pd.DataFrame(dict)
    return df    
 
# Download 5 files 
for x in random_list_str:
    download_file(x)    

# Clear files from unwanted additions
for x in random_list_str:
    clear_file(x)

# Read the contents from the 5 files
for x in random_list_str:
    read_file(x)

# Split conversations into one list
chat_list = chat_to_list(all_chat)