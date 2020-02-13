from phase03.animal import Animal


class Dog(Animal):
    ## 이름과 나이를 출력하는 함수 구현
    def name_age(self):
        print(self.name)
        print(self.age)


class Cat(Animal):
    ## 나이 곱하기 다리개수를 출력하는 함수 구현
    def age_leg(self):
        print(self.leg_count * 40000 * self.age)
