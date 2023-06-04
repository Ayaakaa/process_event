import json

def process_json(path: str):
    f = open(f'{path}')
    data = json.load(f)
    f.close()
    return data