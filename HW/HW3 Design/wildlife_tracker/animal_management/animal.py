from typing import Any, Optional

class Animal:

    def __init__(self, age:int, animal_id:int, species: str):

        self.age = age
        self.animal_id = animal_id
        self.species = species
        
def update_animal_details(animal_id: int, **kwargs: Any) -> None:
    pass

def get_animal_details(animal_id) -> dict[str, Any]:
    pass

