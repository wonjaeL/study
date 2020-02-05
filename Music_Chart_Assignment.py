# 가수 리스트
singer_list = ['IU', 'BTS', 'Bruno Mars', 'Kim Seung Ju', 'Mariah Carey']
# Dictionary에 사용되는 key list
key_list = ['singer_name_new', 'music_name', 'like', 'sales_count', 'album_price']

music_list = []
music_list.append(
    {key_list[0]: singer_list[0], key_list[1]: 'Love Poem', key_list[2]: 50, key_list[3]: 100, key_list[4]: 10000})
music_list.append(
    {key_list[0]: singer_list[0], key_list[1]: 'Rain Drop', key_list[2]: 30, key_list[3]: 50, key_list[4]: 8000})
music_list.append(
    {key_list[0]: singer_list[0], key_list[1]: 'Palette', key_list[2]: 70, key_list[3]: 120, key_list[4]: 11000})
music_list.append({key_list[0]: singer_list[0], key_list[1]: '23', key_list[2]: 65, key_list[3]: 90, key_list[4]: 9000})
music_list.append(
    {key_list[0]: singer_list[1], key_list[1]: 'DNA', key_list[2]: 100, key_list[3]: 150, key_list[4]: 11000})
music_list.append(
    {key_list[0]: singer_list[1], key_list[1]: 'Mic Drop', key_list[2]: 90, key_list[3]: 140, key_list[4]: 12000})
music_list.append(
    {key_list[0]: singer_list[1], key_list[1]: 'Spring Days', key_list[2]: 70, key_list[3]: 120, key_list[4]: 10000})
music_list.append(
    {key_list[0]: singer_list[2], key_list[1]: 'Nothing on U', key_list[2]: 150, key_list[3]: 120, key_list[4]: 10000})
music_list.append(
    {key_list[0]: singer_list[2], key_list[1]: 'Uptown Funk', key_list[2]: 200, key_list[3]: 220, key_list[4]: 7500})
music_list.append(
    {key_list[0]: singer_list[3], key_list[1]: 'I love Girls', key_list[2]: 450, key_list[3]: 450, key_list[4]: 11000})
music_list.append(
    {key_list[0]: singer_list[4], key_list[1]: 'All I want for Christmas is You', key_list[2]: 250, key_list[3]: 250,
     key_list[4]: 5000})
music_list.append(
    {
        key_list[0]: singer_list[4],
        key_list[1]: 'Hero',
        key_list[2]: 200,
        key_list[3]: 150, key_list[4]: 6500
    })

temp_count_dict_profit = {}
temp_count_dict_Like = {}
best_song = {
    'song': None,
    'count': 0
}
for music in music_list:
    singer = music[key_list[0]]
    if singer not in temp_count_dict_profit:
        temp_count_dict_profit[singer] = 0
    if singer not in temp_count_dict_Like:
        temp_count_dict_Like[singer] = 0

    temp_count_dict_profit[singer] = temp_count_dict_profit[singer] + music[key_list[3]] * music['album_price']
    temp_count_dict_Like[singer] = temp_count_dict_Like[singer] + music['like']

    if best_song['count'] < music['like']:
        best_song['count'] = music['like']
        best_song['song'] = music['music_name']

singer_length = 5
for i in range(0, singer_length):
    print(singer_list[i])
    print(temp_count_dict_Like[singer_list[i]])
    print(temp_count_dict_profit[singer_list[i]])

print(best_song['song'])
