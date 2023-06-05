import asyncio
import os

from utilities import get_files, get_folders
from process_data.process_story import process_story

#Unit Story
#files = get_files("data/raw/unit_story")
#for i in files:
#    if i != '.DS_Store':
#        process_story(None, 'unit_story', i)
#print('done_all')

#Event Story
folders = get_folders("data/raw/event_story")
for folder in folders:
    if folder != '.DS_Store':
        files = get_files(f"data/raw/event_story/{folder}")
        
        for file in files:
            if file != '.DS_Store':
               process_story('event_story', folder, file)