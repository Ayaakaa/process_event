import json
import requests
import csv
import os

from data import api, jp_diff, jp_asset, tw_diff, tw_asset

def process_json(location1, location2, path: str):
    if location1 != None:
        f = open(f'data/raw/{location1}/{location2}/{path}')
    else:
        f = open(f'data/raw/{location2}/{path}')
    data = json.load(f)
    f.close()
    return data

def get_sekai_data(server: str, type: str, path: str):
    #raise error
    possible_server = ['tw','jp']
    possible_type = ['diff', 'assets']
    if server not in possible_server:
        raise ValueError(f'Server {server} is not supported, it must be tw or jp')
    if type not in possible_type:
        raise ValueError(f'Type {type} is not supported, it must be diff or assets')
    
    #run
    content_type = 'text/plain'
        
    if type == 'assets':
        if server == 'tw':
            url = tw_asset
        elif server == 'jp':
            url = jp_asset
        link = f'{url}{path}'
        return link
            
    elif type == 'diff':
        if server == 'tw':
            url = tw_diff
        elif server == 'jp':
            url = jp_diff
    
    data = f'{url}{path}'
    
    r = requests.get(data) 
    json =  r.json()
    return json    

def get_character_id(character_2d_id: int):
    character_data = get_sekai_data(server=f'tw', type='diff', path='main/character2ds.json') 
    for character in character_data:
        if character_2d_id == character['id']:
            character_id = character['characterId']
            return character_id
    
def get_character_name(character_id: int):
    character_data = get_sekai_data(server=f'tw', type='diff', path='main/gameCharacters.json') 
    for character in character_data:
        if character_id == character['id']:
            try: first_name = character['firstName']
            except: first_name = ''
            try: last_name = character['givenName']
            except: last_name = ''
            name = f'{first_name}{last_name}'
            if name == '': return False
            else:
                return name
    return False

def get_files(folder_path: str):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return files

def get_folders(folder_path: str):
    folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    return folders