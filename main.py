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