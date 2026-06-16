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
    main_location = locations[0]
    animal_type = animal.get("characteristics").get("type")

    print(f"Name: {name}")
    if diet and diet != "None":
        print(f"Diet: {diet}")
    if main_location and main_location != "None":
        print(f"Location: {main_location}")
    if animal_type and animal_type != "None":
        print(f"Type: {animal_type}")
    print()
