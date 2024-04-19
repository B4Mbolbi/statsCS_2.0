from save_load import *


def get_funck_webbapp(bot: TeleBot, id, data: dict):
    print(data)
    redackt = eval(data)
    key = list(redackt.keys())[0]
    print(key)
    if key == 'add_game':
        for keyR, valueR in redackt[key].items():
            bot.send_message(id, return_text_is_dict(keyR, valueR))

    if key == 'check_aspect':
        info = get_info_steam(redackt[key])
        if 'photo' in info:
            bot.send_photo(id, info['photo'], caption=info['text'], reply_markup=wedAppKeyboard_stats())
            save_user_id_steamId(id, info['steamid'])
        # if len(get_stat(info['steamid'])) > 4096:
        #    for x in range(0, len(get_stat(info['steamid'])), 4096):
        #       bot.send_message(id, get_stat(info['steamid'])[x:x + 4096])
        #    else:
        #       bot.send_message(id, get_stat(info['steamid']))

    if key == "get_info_user":
        steamId = get_id_steam(id)
        dataUSerSteam = get_data_user_stats(steamId)
        bot.send_message(id, f'Твоя стата по {redackt[key]['aspect']}', reply_markup=wedAppKeyboard_stats())
        text = get_sorted_data_translate(aspect=redackt[key]['aspect'], data_gamer=dataUSerSteam)
        bot.send_message(id, text)