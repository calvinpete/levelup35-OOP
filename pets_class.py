class Dog:
    """
    This class holds the profile information of a dog
    """
    animal_class = "mammal"

    def __init__(self, name, age, is_hungry=True):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

    def eat(self):
        """
        This changes the value of is_hungry to False
        :return:
        """
        self.is_hungry = False


class Pets:
    """
    This class holds instances of the Dog class
    """
    records = []  # allows storage of data outside the class

    def __init__(self, pet_dogs):
        self.pet_dogs = pet_dogs  # instance variable

    def pets_owned(self):
        """
        This outputs the number of instances of the Dog class stored in the data structure
        :return:
        """
        return "I have {} dogs\n".format(len(self.pet_dogs))


if __name__ == "__main__":
    records = [Dog("tom", 6), Dog("Fletcher", 7), Dog("Larry", 9)]
    my_pets = Pets(records)
    my_pets.pets_owned()
    for dog in my_pets.pet_dogs:
        print("{0} is {1}\n".format(dog.name, dog.age))
    else:
        print("And they're all {}s, of course.\n".format(dog.animal_class))

    for dog in my_pets.pet_dogs:
        if dog.is_hungry:
            dog.eat()

    if dog.is_hungry:
        print("My dogs are hungry")
    else:
        print("My dogs are not hungry")


