class Pets:
    """
    This class holds instances of the Dog class
    """
    def __init__(self):
        self.records = []  # allows storage of data outside the class

    def add_pet(self, pet):
        """
        Stores an instance of the Dog class in a data structure
        :param pet:
        :return:
        """
        self.records.append(pet)

    def walk(self):
        """
        This calls the walk method for each instance of the Dog class
        :return:
        """
        for i in self.records:
            i.walk()


class Dog:
    """
    This class holds the profile information of a dog
    """
    def __init__(self, name, age, kind, is_hungry=True):
        self.name = name
        self.age = age
        self.kind = kind
        self.is_hungry = is_hungry

    def walk(self):
        """
        This outputs the behaviour of the instance of the Dog class
        :return:
        """
        print("{} is walking.\n".format(self.name))


if __name__ == "__main__":
    tom = Dog("Tom", 6, "mammal")
    fletcher = Dog("Fletcher", 7, "mammal")
    larry = Dog("Larry", 9, "mammal")
    my_pets = Pets()
    my_pets.add_pet(tom)
    my_pets.add_pet(fletcher)
    my_pets.add_pet(larry)
    my_pets.walk()
