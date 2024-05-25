# Animal Shelter Management System
## The goal of this lab is to create an Animal Shelter Management System that leverages Object-Oriented Programming (OOP) principles to manage animals and adopters efficiently. This system will support the addition and removal of animals, registration of adopters, and adoption processes using different strategies. The system ensures animals are marked as adopted appropriately and provides detailed status updates

## Key Components and OOP Principles
1. Animal Class:

* Encapsulation: Encapsulates the properties of an animal such as name, species, breed, age, and adoption status.
* Abstraction: Provides methods to mark an animal as adopted and to represent the animal as a string for easy readability.

2. Adopter Class:

* Encapsulation: Encapsulates the properties of an adopter, including their name and the list of adopted animals.
* Abstraction: Provides methods to adopt an animal and represent the adopter's details as a string.

3. AnimalShelter Class:

* Encapsulation: Manages collections of animals and adopters.
* Abstraction: Provides methods to add or remove animals, register adopters, and get the shelter's status.

4. AdoptionStrategy Abstract Class:

* Abstraction: Defines a high-level interface for different adoption strategies.
* Inheritance: Allows for the creation of different strategies that implement the adoption process differently.

5. Concrete Strategy Classes:

* FirstComeFirstServedStrategy: Implements a straightforward adoption process where the first adopter to *     request an animal gets to adopt it.
* PriorityBasedAdoptionStrategy: Implements a priority-based adoption process, prioritizing the adoption of puppies and kittens.

6. Strategy Pattern
The strategy pattern is used to define a family of algorithms, encapsulate each one, and make them interchangeable. This pattern allows the Animal Shelter to adopt different strategies for animal adoption without changing the shelter's core logic. By switching strategies, the shelter can easily adapt to new policies or requirements