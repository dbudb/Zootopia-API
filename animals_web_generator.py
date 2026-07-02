import os
import json
import requests
from typing import Any
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.api-ninjas.com/v1/animals'
HEADERS = {'X-Api-Key': API_KEY}

def fetch_data(url: str, name: str) -> list[dict[str, Any]]:
    """fetches animal data from API"""
    res = requests.get(url, params={'name': name}, headers=HEADERS)
    return res.json()


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


def serialize_animal(animal: dict[str, Any]) -> str:
    """returns html for a single animal: name, diet, location, type"""
    name = animal.get("name")
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    animal_type = characteristics.get("type")
    locations = animal.get("locations")
    main_location = locations[0] if locations else None

    output = ""
    output += "<li class='cards__item'>"
    output += f"<div class='card__title'>{name}</div>"
    output += "<p class='card__text'>"

    if diet:
        output += f"<strong>Diet:</strong> {diet}<br/>"
    if main_location:
        output += f"<strong>Location:</strong> {main_location}<br/>"
    if animal_type:
        output += f"<strong>Type:</strong> {animal_type}<br/>"

    output += "</p></li>"
    return output


def serialize_output(animals: list[dict[str, Any]]) -> str:
    """returns html for all animals"""
    return "".join(serialize_animal(animal) for animal in animals)


def main():
    """loads information from a json file, loads a html template,
    serializes the information, pastes into html and saves file
    """
    try:
        animals_data = fetch_data(BASE_URL, "Fox")
        html_template = load_template("animals_template.html")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return
    except json.JSONDecodeError as e:
        print(f"File could not be decoded as JSON: {e}")
        return

    animals_html = serialize_output(animals_data)
    html_filled = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    try:
        save_file("animals.html", html_filled)
    except OSError as e:
        print(f"Could not save due to OS error: {e}")
if __name__ == "__main__":
    main()