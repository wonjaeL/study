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


temp_count_like = {}
temp_count_profit = {}


for music in music_list :
    singer = music['singer_name']

    if singer not in temp_count_like :
        temp_count_like[singer] = 0
    if singer not in temp_count_profit :
        temp_count_profit[singer] = 0

    count_l = temp_count_like[singer] + music['like']
    temp_count_like[singer] = count_l
    count_p = temp_count_profit[singer] + music['sales_count'] * music['album_price']
    temp_count_profit[singer] = count_p


for name in singer_list :
    print(name)
    print(temp_count_like[name])
    print(temp_count_profit[name])


# best song
count_music_like = {}
count_best_song = 0

for music in music_list :
    music_name = music['music_name']
    music_like = music['like']

    count_music_like[music_like] = music_name

    if count_best_song < music_like :
        count_best_song = music_like
best_song = count_music_like[count_best_song]

print('best_song = ',best_song)

# 만약에 like 수가 같은 곡들이 있으면 어떡하죠?

### 통과기준1 - music_list를 이용하여서 singer_list에 있는 5명의 가수를 순서대로
#              가수명, 좋아요 합계, 앨범수익(앨범 판매량 X 앨범가격) 출력하시오
#   Example
#            > IU             (가수명)
#            > 215            (좋아요 합계)
#            > 3530000        (앨범수익)
###
# 통과기준2 - Like가 가장 많은 노래를 best_song 변수에 넣고 맨 마지막에 출력하시오
best_song = ''