import json
import aiohttp
import csv

from data import api, jp_diff, jp_asset, tw_diff, tw_asset

def process_json(path: str):
    f = open(f'{path}.json')
    data = json.load(f)
    f.close()
    return data

async def get_sekai_data(server: str, type: str, path: str):
    #raise error
    possible_server = ['tw','jp']
    possible_type = ['diff', 'assets']
    if server not in possible_server:
        raise ValueError(f'Server {server} is not supported, it must be tw or jp')
    if type not in possible_type:
        raise ValueError(f'Type {type} is not supported, it must be diff or assets')
    
    #run
    content_type = 'text/plain'
    session = aiohttp.ClientSession()
        
    if type == 'assets':
        if server == 'tw':
            url = tw_asset
        elif server == 'jp':
            url = jp_asset
        link = f'{url}{path}'
        await session.close()
        return link
            
    elif type == 'diff':
        if server == 'tw':
            url = tw_diff
        elif server == 'jp':
            url = jp_diff
    
    data = f'{url}{path}'
    
    async with session.get(data) as r:
        json = await r.json(content_type=f'{content_type}')
        await session.close()
        return json    

async def get_character_id(character_2d_id: int):
    character_data = await get_sekai_data(server=f'tw', type='diff', path='main/character2ds.json') 
    for character in character_data:
        if character_2d_id == character['id']:
            character_id = character['characterId']
            return character_id
    
async def get_character_name(character_id: int):
    character_data = await get_sekai_data(server=f'tw', type='diff', path='main/gameCharacters.json') 
    for character in character_data:
        if character_id == character['id']:
            first_name = character['firstName']
            last_name = character['givenName']
            name = f'{first_name}{last_name}'
            return name