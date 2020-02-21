from phase03_gwajay.moonjae import get_moonjae  # Do not change this line


class Music:

    def __init__(self, name, like, album_price):
        self.name = name
        self.like = like
        self.album_price = album_price


class Singer:
    def __init__(self, name, music_list):
        self.name = name
        self.music_list = music_list

    def get_song_list(self):
        return self.music_list

    pass


def answer():
    key_list, music_list = get_moonjae()

    singer_list = []
    singer_dict = {}
    for music_dict in music_list:
        singer_name = music_dict['singer_name']
        if singer_name not in singer_dict:
            singer_dict[singer_name] = Singer(music_dict['singer_name'], [])
            singer_list.append(singer_dict[singer_name])

        music = Music(music_dict['music_name'], music_dict['like'], music_dict['album_price'])
        singer_dict[singer_name].music_list.append(music)

    return singer_list


from phase03_gwajay.moonjae import calculate

calculate()
