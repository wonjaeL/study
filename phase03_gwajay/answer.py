from phase03_gwajay.moonjae import get_moonjae  # Do not change this line


class Music:
    # name 이라는 attribute를 추가해주세요
    # like라는 attribute를 추가해주세요
    # album_price라는 attribute를 추가해주세요
    pass


class Singer:
    # name 이라는 attribute를 추가해주세요
    # music_list 라는 list 를 만들어서 가수가 부른 노래를 저장해주세요

    def get_song_list(self):
        return self.music_list

    pass


def answer():
    singer_list = []
    ##########
    ## Example
    ##########
    ## instance = Music(xxxx,xxxx,xxx,xxx)
    ## singer_list.append(instance)

    key_list, music_list = get_moonjae()  # Do not change this line
    # ///////////////////////////////////////////////////////////////////////////////////

    '''
        이 부분에 여러분의 알고리즘 구현이 들어갑니다.
        Music, Singer Class의 __init__함수를 구현하시고
        30번줄 부터 42번줄 까지 지우고 구현하세요
        key_list, music_list에 값이 담겨져 있습니다.
        참고해서 singer class를 이용하여 instance를
        모든 singer를 class_list에 담아주세요
        (이번 문제에서는 상속이 없습니다.)
    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    return singer_list


from phase03_gwajay.moonjae import calculate

calculate()
