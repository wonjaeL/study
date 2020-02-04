# 가수 리스트
singer_list = ['IU', 'BTS', 'Bruno Mars', 'Kim Seung Ju','Mariah Carey']

# Dictionary에 사용되는 key list
key_list = ['singer_name', 'music_name', 'like', 'sales_count', 'album_price']

music_list = []
music_list.append({key_list[0]: singer_list[0], key_list[1]: 'Love Poem', key_list[2]: 50, key_list[3]: 100, key_list[4]: 10000})
music_list.append({key_list[0]: singer_list[0], key_list[1]: 'Rain Drop', key_list[2]: 30, key_list[3]: 50, key_list[4]: 8000})
music_list.append({key_list[0]: singer_list[0], key_list[1]: 'Palette', key_list[2]: 70, key_list[3]: 120, key_list[4]: 11000})
music_list.append({key_list[0]: singer_list[0], key_list[1]: '23', key_list[2]: 65, key_list[3]: 90, key_list[4]: 9000})
music_list.append({key_list[0]: singer_list[1], key_list[1]: 'DNA', key_list[2]: 100, key_list[3]: 150, key_list[4]: 11000})
music_list.append({key_list[0]: singer_list[1], key_list[1]: 'Mic Drop', key_list[2]: 90, key_list[3]: 140, key_list[4]: 12000})
music_list.append({key_list[0]: singer_list[1], key_list[1]: 'Spring Days', key_list[2]: 70, key_list[3]: 120, key_list[4]: 10000})
music_list.append({key_list[0]: singer_list[2], key_list[1]: 'Nothing on U', key_list[2]: 150, key_list[3]: 120, key_list[4]: 10000})
music_list.append({key_list[0]: singer_list[2], key_list[1]: 'Uptown Funk', key_list[2]: 200, key_list[3]: 220, key_list[4]: 7500})
music_list.append({key_list[0]: singer_list[3], key_list[1]: 'I love Girls', key_list[2]: 450, key_list[3]: 450, key_list[4]: 11000})
music_list.append({key_list[0]: singer_list[4], key_list[1]: 'All I want for Christmas is You', key_list[2]: 250, key_list[3]: 250, key_list[4]: 5000})
music_list.append({key_list[0]: singer_list[4], key_list[1]: 'Hero', key_list[2]: 200, key_list[3]: 150, key_list[4]: 6500})

temp_dict={}


for music in music_list:
    a = music['singer_name']
    if a not in temp_dict:
        temp_dict[a] = 1
        temp_dict[a+'_like'] = music['like']
        temp_dict[a+'_profit'] = music['sales_count']*music['album_price']
    else:
        temp_dict[a+'_like'] += music['like']
        temp_dict[a+'_profit'] += music['sales_count']*music['album_price']

for name in temp_dict:
    if temp_dict[name] == 1:
        print('singer = {}' .format(name))
        print('like = {}' .format(temp_dict[name+'_like']))
        print('profit = {}' .format(temp_dict[name+'_profit']))
        print('\n')

best_song = ''
best_song_like = 0
for music in music_list:
    if music['like'] > best_song_like:
        best_song = music['music_name']
        best_song_like = music['like']

print('best_ song = \'{}\'' .format(best_song))
