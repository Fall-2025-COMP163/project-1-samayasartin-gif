# COMP 163 - Project 1: Character Creator & Saving/Loading
# Name: Samaya Sartin
# Date: 10/23/2025
# AI Usage: Copilot Microsoft - Explained how to use with open(...) as file, Update Character action, Majority of bugs in my code.

# do not use try finally BUT you CAN use with, as
import os

def calculate_stats(character_class, level):
    if character_class == "Warrior":
        strength = 10 * level
        magic = 1 * level
        health = 100 * level
    elif character_class == "Mage":
        strength = 5 * level
        magic = 10 * level
        health = 100 * level
    elif character_class == "Rogue":
        strength = 7 * level
        magic = 3 * level
        health = 100 * level
    elif character_class == "Cleric":
        strength = 8 * level
        magic = 7 * level
        health = 100 * level
    else:
        return None
    return strength, magic, health

def create_character(name, character_class, level=1):
    stats = calculate_stats(character_class, level)
    if stats is None:
        return None
    strength, magic, health = stats
    character = {}
    character["name"] = name
    character["class"] = character_class
    character["level"] = level
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    character["gold"] = 100
    return character

def save_character(character, filename):
    if "/" in filename or "\\" in filename:
        return False
    with open(filename, "w") as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
    return True

def load_character(filename):
    if not os.path.exists(filename):
        return None
    with open(filename, "r") as file:
        lines = file.readlines()
    character = {}
    for line in lines:
        parts = line.strip().split(": ")
        if len(parts) == 2:
            key = parts[0]
            value = parts[1]
            if key == "Character Name":
                character["name"] = value
            elif key == "Class":
                character["class"] = value
            elif key == "Level":
                character["level"] = int(value)
            elif key == "Strength":
                character["strength"] = int(value)
            elif key == "Magic":
                character["magic"] = int(value)
            elif key == "Health":
                character["health"] = int(value)
            elif key == "Gold":
                character["gold"] = int(value)
    return character

def display_character(character):
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")

def level_up(character, save_name="save_game.txt"):
    character["level"] = character["level"] + 1
    stats = calculate_stats(character["class"], character["level"])
    character["strength"] = stats[0]
    character["magic"] = stats[1]
    character["health"] = stats[2]
    save_character(character, save_name)

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    level = 1
    print("Do you have a character already? (Yes or No): ")
    existing_character = input()
    while existing_character == "Yes":
        filename = input("Enter file name: ")
        character = load_character(filename)
        if character is not None:
            display_character(character)
        else:
            print("Character not found.")
        existing_character = "No"

    hero_type = input("What type of hero are you?: ")
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    while hero_type not in valid_classes:
        print("Invalid class!")
        hero_type = input("What type of hero are you? (Choose from Warrior, Mage, Rogue, Cleric): ")

    hero_name = input("Enter your hero's name: ")
    save_name = input("Enter filename: ")
    character = create_character(hero_name, hero_type, level)
    level_up(character, save_name)
    display_character(character)
    print()
