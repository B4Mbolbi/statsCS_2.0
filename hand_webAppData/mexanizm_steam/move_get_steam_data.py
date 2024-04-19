import json
from steam_web_api import Steam

steam = Steam('2A00FF13176354B158C00C5246680F28')


def save_stata(steamid, data):
    with open(f'cashe\\{steamid}.json', 'w+') as f:
        json.dump(data, f, indent=2)


def get_text(data):
    text = f'''
    Привет {data['personaname']}
    Твой профиль стим {data['profileurl']}
    твой стим ID {data['steamid']}
    '''

    return {'photo': data['avatar'], 'text': text, 'steamid': data['steamid']}


def get_info_steam(data):
    steam_id = data['SteamId']
    steam_name = data['SteamName']
    print(steam_name)
    print(steam_id)
    info_person = {}
    if (steam_name == '') or ((steam_id != '') and (steam_name != '')):
        user_name = steam.users.get_user_details(steam_id)['player']
        user_game = steam.apps.get_user_stats(steam_id, '730')
        stats = user_game['playerstats']['stats']
        for i in stats:
            # print(i['name'] , ' ' , i['value'])
            info_person[i['name']] = i['value']
        save_stata(user_name['steamid'], info_person)

        infoPerson = {'avatar': user_name['avatarfull'], 'personaname': user_name['personaname'],
                      'profileurl': user_name['profileurl'], 'steamid': user_name['steamid']}
        return get_text(infoPerson)

    if steam_id != '':
        user_name = steam.users.search_user(steam_name)['player']
        user_game = steam.apps.get_user_stats(user_name['steamid'], '730')
        stats = user_game['playerstats']['stats']
        for i in stats:
            # print(i['name'] , ' ' , i['value'])
            info_person[i['name']] = i['value']
        save_stata(user_name['steamid'], info_person)

        # pprint.pprint(user_name)
        # pprint.pprint(info_person)

        infoPerson = {'avatar': user_name['avatarfull'], 'personaname': user_name['personaname'],
                      'profileurl': user_name['profileurl'], 'steamid': user_name['steamid']}
        return get_text(infoPerson)


if __name__ == '__main__':
    get_info_steam({'SteamId': '76561198870737841', 'SteamName': 'KoAnMiKs'})

