from phase03.dong_cats import Dog, Cat

dog1 = Dog("check", 7, 4)
dog2 = Dog("nobless", 4, 5)
cat1 = Cat("topclass", 5, 6)
cat2 = Cat("munbock", 5, 4)
cat3 = Cat("gf", 3, 5)

animals = [dog1, dog2, cat1, cat2, cat3]

for animal in animals:
    if type(animal) == Dog:
        animal.name_age()
    if type(animal) == Cat:
        animal.age_leg()
    animal.print_legs()
