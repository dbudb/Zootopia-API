import json

def load_data(file_path: str) -> json:
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def load_template(file_path: str) -> str:
    "loads a textfile"
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def save_html(file_path: str, content: str) -> None:
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(html_filled)


animals_data = load_data("animals_data.json")
selected_animal_data = ""
html_template = load_template("animals_template.html")

for animal in animals_data:

    name = animal.get("name")
    diet = animal.get("characteristics").get("diet")
    locations = animal.get("locations")
    main_location = locations[0]
    animal_type = animal.get("characteristics").get("type")

    selected_animal_data += "<li class='cards__item'>"
    selected_animal_data += f"<div class='card__title'>{name}</div>"
    selected_animal_data += f"<p class='card__text'>"

    if diet and diet != "None":
        selected_animal_data += f"<strong>Diet:</strong> {diet}<br/>"
    if main_location and main_location != "None":
        selected_animal_data += f"<strong>Location:</strong> {main_location}<br/>"
    if animal_type and animal_type != "None":
        selected_animal_data += f"<strong>Type:</strong> {animal_type}<br/>"

    selected_animal_data += "</p></li>"

html_filled = html_template.replace("__REPLACE_ANIMALS_INFO__", selected_animal_data)
save_html("animals.html", html_filled)
