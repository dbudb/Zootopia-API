import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')

for animal in animals_data:
    name = animal.get("name")
    diet = animal.get("characteristics").get("diet")
    locations = animal.get("locations")
    animal_type = animal.get("characteristics").get("type")


    print(name)
    print(diet)
    print(locations)
    print(animal_type)

