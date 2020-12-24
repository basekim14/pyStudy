# -*- coding: utf-8 -*-
def convert_script(game, server):
    names = ['search_game', 'search_game_text', 'search_server', 'search_server_text']
    prefix = 'document.querySelector("#g_searchbar_form > input[name='
    midfix = ']").setAttribute("value", "'
    postfix = '");'

    scripts = [prefix + 'search_game' + midfix + game_db[game] + postfix,
               prefix + 'search_game_text' + midfix + game + postfix,
               prefix + 'search_server' + midfix + server_db[server] + postfix,
               prefix + 'search_server_text' + midfix + server + postfix]
    
    return scripts    

game_db = {
    'search_game_text': 'search_game',}

server_db = {
    'search_server_text': 'search_server',}

if __name__ == '__main__':
    print('총 %d개의 게임 코드와 %d개의 서버 코드가 존재함.' % (len(game_db), len(server_db)))

