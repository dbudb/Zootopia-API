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


def serialize_output(animals: list[dict[str, Any]]) -> str:
    """gets list of animal objects and returns html formatted str with only name, diet, location and type per animal"""
    selected_animal_data = ""
    for animal in animals:
        name = animal.get("name")
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        animal_type = characteristics.get("type")
        locations = animal.get("locations")
        main_location = locations[0] if locations else None

        selected_animal_data += "<li class='cards__item'>"
        selected_animal_data += f"<div class='card__title'>{name}</div>"
        selected_animal_data += "<p class='card__text'>"

        if diet:
            selected_animal_data += f"<strong>Diet:</strong> {diet}<br/>"

        if main_location:
            selected_animal_data += f"<strong>Location:</strong> {main_location}<br/>"

        if animal_type:
            selected_animal_data += f"<strong>Type:</strong> {animal_type}<br/>"

        selected_animal_data += "</p></li>"
    return selected_animal_data


def main():
    """loads information from a json file, loads a html template,
    serializes the information, pastes into html and saves file
    """
    animals_data = load_data("animals_data.json")
    html_template = load_template("animals_template.html")
    animals_html = serialize_output(animals_data)
    html_filled = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)
    save_file("animals.html", html_filled)


if __name__ == "__main__":
    main()