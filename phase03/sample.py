class Animal:
    def __init__(self, name, age, leg_count):
        pass

    ## 다리개수를 출력하는 함수구현
    def print_legs(self):
        pass


class Dog:
    ## 이름과 나이를 출력하는 함수 구현
    def name_age(self):
        pass


class Cat:
    ## 나이 곱하기 다리개수를 출력하는 함수 구현
    def age_leg(self):
        pass


dog1 = Dog()
dog2 = Dog()
cat1 = Cat()
cat2 = Cat()
cat3 = Cat()

animals = [dog1, dog2, cat1, cat2, cat3]

for animal in animals:
    if type(animal) == Dog:
        animal.name_age()
    if type(animal) == Cat:
        animal.age_leg()
    animal.print_legs()
