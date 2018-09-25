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

    def walk(self):
        """
        This outputs the behaviour of the instance of the Dog class
        :return self.name is walking!:
        """
        return "{} is walking!\n".format(self.name)


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
        :return I have len(self.pet_dogs) dogs:
        """
        return "I have {} dogs\n".format(len(self.pet_dogs))

    def walk(self):
        """
        This calls the walk method for each instance of the Dog class
        :return:
        """
        for dog in self.pet_dogs:
            print(dog.walk())


if __name__ == "__main__":
    records = [Dog("tom", 6), Dog("Fletcher", 7), Dog("Larry", 9)]
    my_pets = Pets(records)
    my_pets.walk()
