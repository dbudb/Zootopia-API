import json
from typing import Any


def load_data(file_path: str) -> list[dict[str, Any]]:
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def load_template(file_path: str) -> str:
    """loads a textfile"""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def save_file(file_path: str, content: str) -> None:
    """saves a text file"""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def serialize_output(animals):
    selected_animal_data = ""
    for animal in animals:
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
    return selected_animal_data

def main():
    animals_data = load_data("animals_data.json")
    html_template = load_template("animals_template.html")
    animals_html = serialize_output(animals_data)
    html_filled = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)
    save_file("animals.html", html_filled)

if __name__ == "__main__":
    main()