import pandas as pd
import os

# get current file path
base_path = os.path.dirname(__file__)

# go to data folder
file_path = os.path.join(base_path, '../data/songs.csv.txt')

# load data
data = pd.read_csv(file_path)

mood = input("Enter your mood: ").lower()

result = data[data['mood'] == mood]

if len(result) > 0:
    print("\nRecommended songs:")
    for song in result['song']:
        print("-", song)
else:
    print("No songs found")