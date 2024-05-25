from abc import ABC, abstractmethod

# Animal class
class Animal:
    """
    Represents an animal in the shelter.
    """
    def __init__(self, name, species, breed, age):
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.is_adopted = False

    def mark_as_adopted(self):
        self.is_adopted = True

    def __str__(self):
        return f"{self.name}, {self.species}, {self.breed}, Age: {self.age}, Adopted: {self.is_adopted}"

# Adopter class
class Adopter:
    """
    Represents an adopter who can adopt animals.
    """
    def __init__(self, name):
        self.name = name
        self.adopted_animals = []

    def adopt_animal(self, animal):
        if not animal.is_adopted:
            animal.mark_as_adopted()
            self.adopted_animals.append(animal)
            return True
        return False

    def __str__(self):
        return f"Adopter: {self.name}, Adopted Animals: {[animal.name for animal in self.adopted_animals]}"

# AnimalShelter class
class AnimalShelter:
    """
    Manages the collection of animals and adopters.
    """
    def __init__(self):
        self.animals = []
        self.adopters = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def register_adopter(self, adopter):
        self.adopters.append(adopter)

    def __str__(self):
        return f"Shelter has {len(self.animals)} animals and {len(self.adopters)} adopters"

# Strategy Pattern
class AdoptionStrategy(ABC):
    """
    Abstract base class for adoption strategies.
    """
    @abstractmethod
    def adopt(self, adopter, animal):
        pass

#Concrete Strategy Classes
class FirstComeFirstServedStrategy(AdoptionStrategy):
    """
    Adopts the animal on a first-come, first-served basis.
    """
    def adopt(self, adopter, animal):
        if not animal.is_adopted:
            return adopter.adopt_animal(animal)
        return False

class PriorityBasedAdoptionStrategy(AdoptionStrategy):
    """
    Adopts the animal based on a priority, such as species being a puppy or kitten.
    """
    def adopt(self, adopter, animal):
        if not animal.is_adopted and (animal.species == 'puppy' or animal.species == 'kitten'):
            return adopter.adopt_animal(animal)
        return False

# Main function to test the system
if __name__ == "__main__":
    # Create animal shelter
    shelter = AnimalShelter()

    # Add animals
    animal1 = Animal("Buddy", "dog", "Golden Retriever", 3)
    animal2 = Animal("Mittens", "cat", "Siamese", 2)
    shelter.add_animal(animal1)
    shelter.add_animal(animal2)

    # Create adopters
    adopter1 = Adopter("Alice")
    adopter2 = Adopter("Bob")
    shelter.register_adopter(adopter1)
    shelter.register_adopter(adopter2)

    # Adopt animals using strategy
    strategy = FirstComeFirstServedStrategy()
    strategy.adopt(adopter1, animal1)
    strategy.adopt(adopter2, animal2)

    # Print status
    print(shelter)
    print(adopter1)
    print(adopter2)
    print(animal1)
    print(animal2)
