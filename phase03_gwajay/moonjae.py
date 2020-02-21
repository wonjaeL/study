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


def get_moonjae():
    return key_list, music_list


def calculate():
    from phase03_gwajay.answer import answer
    singer_list = answer()

    if not singer_list:
        print('Fail - list가 비어있습니다.')
        exit(1)

    for singer in singer_list:
        song_list = singer.get_song_list()
        if not song_list:
            print('Fail - song_list가 비어있습니다.')
            exit(1)
        for song in song_list:
            if not hasattr(song, 'name'):
                print('Fail - song Name attribute가 없습니다.')
                exit(1)
            if not hasattr(song, 'like'):
                print('Fail - like attribute가 없습니다.')
                exit(1)
            if not hasattr(song, 'album_price'):
                print('Fail - album_price attribute가 없습니다.')
                exit(1)

    print('PASS - 수고하셨습니다.')
