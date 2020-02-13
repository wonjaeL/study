class Animal:
    def __init__(self, name, age, leg_count):
        pass

    ## 다리개수를 출력하는 함수 구현
    def print_legs(self):
        print(self.leg_count)


class Dog(Animal):
    ## 이름과 나이를 출력하는 함수 구현
    def name_age(self):
        print("Name = ", self.name, "\nAge = ", self.age)


class Cat(Animal):
    ## 나이 곱하기 다리개수를 출력하는 함수 구현
    def age_leg(self):
        print(self.age * self.leg_count)


dog1 = Dog("James", 3, 4)
dog2 = Dog("Bong", 10, 5)
cat1 = Cat("Rilly", 2, 4)
cat2 = Cat("Jason", 5, 3)
cat3 = Cat("Bro", 6, 4)

animals = [dog1, dog2, cat1, cat2, cat3]

for animal in animals:
    if type(animal) == Dog:
        animal.name_age()
    if type(animal) == Cat:
        animal.age_leg()
    animal.print_legs()
