class Animal:
    def __init__(self, name, age, leg_count):
        self.name = name
        self.age = age
        self.leg_count = leg_count

    ## 다리개수를 출력하는 함수구현
    def print_legs(self):
        print(self.leg_count)
