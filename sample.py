music_chart = [
    {'name': 'Bang Bang Bang', 'singer': 'bigbang', 'count': 333},
    {'name': 'aaaaa', 'singer': 'bigbang', 'count': 444},
    {'name': 'ffffff', 'singer': 'wonjae', 'count': 111},
    {'name': 'ccccc', 'singer': 'wonjae', 'count': 555},
    {'name': 'bbbbbbb', 'singer': 'wonjae', 'count': 111},
    {'name': 'eeeeeeeee', 'singer': 'wonjae', 'count': 111},
]

temp_count_dict = {}

for music in music_chart:
    singer = music['singer']
    if singer not in temp_count_dict:
        temp_count_dict[singer] = 0

    count_ = temp_count_dict[singer] + music['count']
    temp_count_dict[singer] = count_

print(temp_count_dict['bigbang'])
print(temp_count_dict['wonjae'])
