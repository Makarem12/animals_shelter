import pytest
from animals_shelter import *

# Test Animal Class
def test_animal_initialization():
    animal = Animal("Buddy", "dog", "Golden Retriever", 3)
    assert animal.name == "Buddy"
    assert animal.species == "dog"
    assert animal.breed == "Golden Retriever"
    assert animal.age == 3
    assert not animal.is_adopted

def test_animal_mark_as_adopted():
    animal = Animal("Buddy", "dog", "Golden Retriever", 3)
    animal.mark_as_adopted()
    assert animal.is_adopted

# Test Adopter Class
def test_adopter_initialization():
    adopter = Adopter("Alice")
    assert adopter.name == "Alice"
    assert adopter.adopted_animals == []

def test_adopter_adopt_animal():
    adopter = Adopter("Alice")
    animal = Animal("Buddy", "dog", "Golden Retriever", 3)
    result = adopter.adopt_animal(animal)
    assert result
    assert animal.is_adopted
    assert adopter.adopted_animals == [animal]

# Test AnimalShelter Class
def test_animal_shelter_initialization():
    shelter = AnimalShelter()
    assert shelter.animals == []
    assert shelter.adopters == []

def test_animal_shelter_add_animal():
    shelter = AnimalShelter()
    animal = Animal("Buddy", "dog", "Golden Retriever", 3)
    shelter.add_animal(animal)
    assert shelter.animals == [animal]

def test_animal_shelter_register_adopter():
    shelter = AnimalShelter()
    adopter = Adopter("Alice")
    shelter.register_adopter(adopter)
    assert shelter.adopters == [adopter]

# Test Adoption Strategies
def test_first_come_first_served_strategy():
    shelter = AnimalShelter()
    animal = Animal("Buddy", "dog", "Golden Retriever", 3)
    adopter = Adopter("Alice")
    shelter.add_animal(animal)
    shelter.register_adopter(adopter)

    strategy = FirstComeFirstServedStrategy()
    result = strategy.adopt(adopter, animal)
    assert result
    assert animal.is_adopted
    assert adopter.adopted_animals == [animal]

def test_priority_based_adoption_strategy():
    shelter = AnimalShelter()
    animal1 = Animal("Buddy", "dog", "Golden Retriever", 3)
    animal2 = Animal("Kitty", "cat", "Siamese", 1)
    adopter = Adopter("Alice")
    shelter.add_animal(animal1)
    shelter.add_animal(animal2)
    shelter.register_adopter(adopter)

    strategy = PriorityBasedAdoptionStrategy()
    result1 = strategy.adopt(adopter, animal1)
    result2 = strategy.adopt(adopter, animal2)

# Run tests
if __name__ == "__main__":
    pytest.main()
