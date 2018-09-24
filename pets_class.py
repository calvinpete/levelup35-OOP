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

    def pets_owned(self):
        """
        This outputs the number of instances of the Dog class stored in the data structure
        :return:
        """
        print("I have {} dogs\n".format(len(self.records)))

    def pet_profile(self):
        """
        This outputs the information of each instance of the Dog class
        :return:
        """
        for i in self.records:
            #  The __getattribute__ provides access to the instance attributes
            print("{0} is {1}\n".format(i.__getattribute__("name"), i.__getattribute__("age")))

    def animal_class(self):
        """
        This checks for a specific attribute of each instance of the Dog class in the data structure
        :return:
        """
        for i in self.records:
            #  The __getattribute__ provides access to the instance attributes
            if i.__getattribute__("kind") != "mammal":
                print("one of them is not a mammal.\n")
                return self.records
        else:
            print("And they're all mammals, of course.\n")

    def pets_meal(self):
        """
        This checks if an instance of the dog class is hungry then the instance is fed
        :return:
        """
        for i in self.records:
            if i.__getattribute__("is_hungry"):
                i.eat()
        else:
            print("My dogs are hungry\n")


class Dog:
    """
    This class holds the profile information of a dog
    """
    def __init__(self, name, age, kind, is_hungry=True):
        self.name = name
        self.age = age
        self.kind = kind
        self.is_hungry = is_hungry

    def eat(self):
        """
        This changes the value of is_hungry to False
        :return:
        """
        self.is_hungry = False


if __name__ == "__main__":
    tom = Dog("Tom", 6, "mammal")
    fletcher = Dog("Fletcher", 7, "mammal")
    larry = Dog("Larry", 9, "mammal")
    my_pets = Pets()
    my_pets.add_pet(tom)
    my_pets.add_pet(fletcher)
    my_pets.add_pet(larry)
    my_pets.pets_owned()
    my_pets.pet_profile()
    my_pets.animal_class()
    my_pets.pets_meal()
