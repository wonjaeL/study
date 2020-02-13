class Animal:
    def __init__(self, name, age, leg_count):
        self.name = name
        self.age = age
        self.leg_count = leg_count
        pass


    ## 다리개수를 출력하는 함수구현
    def print_legs(self):
        print(self.leg_count)
        pass


class Dog(Animal):
    ## 이름과 나이를 출력하는 함수 구현
    def name_age(self):
        print(self.name)
        print(self.age)
        pass


class Cat(Animal):
    ## 나이 곱하기 다리개수를 출력하는 함수 구현
    def age_leg(self):
        print(self.leg_count*self.age)
        pass


dog1 = Dog("check",7,4)
dog2 = Dog("nobless",4,5)
cat1 = Cat("topclass",5,6)
cat2 = Cat("munbock",5,4)
cat3 = Cat("gf",3,5)

animals = [dog1, dog2, cat1, cat2, cat3]

for animal in animals:
    if type(animal) == Dog:
        animal.name_age()
    if type(animal) == Cat:
        animal.age_leg()
    animal.print_legs()
