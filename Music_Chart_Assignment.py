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


temp_count_dict_profit = {}

for music in music_list:
    singer = music['singer_name']
    if singer not in temp_count_dict_profit:
        temp_count_dict_profit[singer] = 0

    count_profit = temp_count_dict_profit[singer] + music['sales_count']*music['album_price']
    temp_count_dict_profit[singer] = count_profit






temp_count_dict_Like = {}

for music in music_list:
    singer = music['singer_name']
    if singer not in temp_count_dict_Like:
        temp_count_dict_Like[singer] = 0

    count_like = temp_count_dict_Like[singer] + music['like']
    temp_count_dict_Like[singer] = count_like

#마지막에 print 0,1,2,3,4 반복문으로 쓰려고 하는데 계속 에러나서 일단 알아보겠습니다.
print(singer_list[0])
print(temp_count_dict_Like[singer_list[0]])
print(temp_count_dict_profit[singer_list[0]])

print(singer_list[1])
print(temp_count_dict_Like[singer_list[1]])
print(temp_count_dict_profit[singer_list[1]])

print(singer_list[2])
print(temp_count_dict_Like[singer_list[2]])
print(temp_count_dict_profit[singer_list[2]])

print(singer_list[3])
print(temp_count_dict_Like[singer_list[3]])
print(temp_count_dict_profit[singer_list[3]])

print(singer_list[4])
print(temp_count_dict_Like[singer_list[4]])
print(temp_count_dict_profit[singer_list[4]])





### 통과기준 - music_list를 이용하여서 singer_list에 있는 5명의 가수를 순서대로

#              가수명, 좋아요 합계, 앨범수익(앨범 판매량 X 앨범가격) 출력하시오

#   Example
#IU
#215
#3530000
#BTS
#260
#4530000
#Bruno Mars
#350
#2850000
#Kim Seung Ju
#450
#4950000
#Mariah Carey
#450
#2225000

#            > IU             (가수명)

#            > 215            (좋아요 합계)

#            > 3530000        (앨범수익)

###

### 심화 - Like가 가장 많은 노래를 best_song 변수에 넣고 맨 마지막에 출력하시오

best_song = ''

