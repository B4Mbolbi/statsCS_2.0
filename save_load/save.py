import json
import os

path = os.getcwd()
path = path.split('\\')
del path[-1]
path = '\\'.join(path) + '\\'

def save_stata(steamid, data):
    with open(f'{path}cashe\\cashe_data\\{steamid}.json', 'w+') as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    save_stata('45255253',{'1':2})