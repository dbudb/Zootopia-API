import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')

selected_animal_data = ""

for animal in animals_data:
    name = animal.get("name")
    diet = animal.get("characteristics").get("diet")
    locations = animal.get("locations")
    main_location = locations[0]
    animal_type = animal.get("characteristics").get("type")

    print(f"Name: {name}\n")
    selected_animal_data += f"Name: {name}\n"
    if diet and diet != "None":
        selected_animal_data += f"Diet: {diet}\n"
        print(f"Diet: {diet}")
    if main_location and main_location != "None":
        selected_animal_data += f"Location: {main_location}\n"
        print(f"Location: {main_location}")
    if animal_type and animal_type != "None":
        selected_animal_data += f"Type: {animal_type}\n"
        print(f"Type: {animal_type}")
    selected_animal_data += "\n"
    print()


print(50*"\n")

print(selected_animal_data)