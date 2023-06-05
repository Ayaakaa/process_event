import csv
import os

from modules.story import Story
from utilities import get_character_name, get_character_id

def process_story(location1, location2, path):
    short_path = path.split(".")
    if location1 != None:
        if os.path.exists(f"data/processed/{location1}/{location2}"):
            pass
        else: 
            os.mkdir(f"data/processed/{location1}/{location2}")
        file_path = f'data/processed/{location1}/{location2}/{short_path[0]}.csv'
    else:
       file_path = f'data/processed/{location2}/{short_path[0]}.csv'
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer = csv.writer(file, escapechar=' ', quoting=csv.QUOTE_NONE)
        #writer.writerow('name', 'line')
        
        story_data = Story()
        story_data.story(location1, location2, path)
        
        for data in story_data.TalkData:
            character_2d_id = data["TalkCharacters"][0]["Character2dId"]
            display_name = data["WindowDisplayName"]
            dialogue = data["Body"]
            str(dialogue).replace('\n', '')
            character_id = get_character_id(character_2d_id)
            character_name = get_character_name(character_id)
            if character_name == False: character_name = display_name
            writer.writerow([str(character_name), dialogue])
        print(f'done {path}')
        return
    
