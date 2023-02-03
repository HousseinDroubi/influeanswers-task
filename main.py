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