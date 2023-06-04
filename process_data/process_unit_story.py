import csv

from modules.unit_story import UnitStory
from utilities import get_character_name, get_character_id

async def process_unit_story(path):
    with open(f'data/processed/event_story/{path}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        
        unit_story_data = UnitStory()
        unit_story_data.unit_story(path)
        
        for data in unit_story_data.TalkData:
            character_2d_id = data["TalkCharacters"][0]["Character2dId"]
            display_name = data["WindowDisplayName"]
            dialogue = data["Body"]
            character_id = await get_character_id(character_2d_id)
            character_name = await get_character_name(character_id)
            writer.writerow([character_name, dialogue])
    return