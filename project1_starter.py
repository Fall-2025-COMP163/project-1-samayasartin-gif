# COMP 163 - Project 1: Character Creator & Saving/Loading
# Name: Samaya Sartin
# Date: 10/23/2025
# AI Usage: Copilot Microsoft - Explained how to use with open(...) as file, Update Character action, Majority of bugs in my code.

# do not use try finally BUT you CAN use with, as
import os
def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)"""

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
    return (strength, magic, health)
    # Return a tuple: (strength, magic, health)

def create_character(name, character_class, level):
    """Creates a new character with stats and returns name, class, level, strength, magic, health, and gold
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    stats = calculate_stats(character_class, level)
    strength = stats[0]
    magic = stats[1]
    health = stats[2]
    return {"name": name, "class": character_class, "level": level, "strength": strength, "magic": magic, "health": health, "gold": 100}
    # Returns the character's full stats in a usable dictionary

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred

    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    character_name = character["name"]
    class_name = character["class"]
    level = character["level"]
    strength = character["strength"]
    magic = character["magic"]
    health = character["health"]
    gold = character["gold"]
    with open(filename, "w") as file:
        file.write(f"Character Name: {character_name}\n")
        file.write(f"Class: {class_name}\n")
        file.write(f"Level: {level}\n")
        file.write(f"Strength: {strength}\n")
        file.write(f"Magic: {magic}\n")
        file.write(f"Health: {health}\n")
        file.write(f"Gold: {gold}\n")
    return True

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    if os.path.exists(filename):
        print("File exists!")
        display_character(filename)

    else:
        print("File not found.")

def display_character(character_file):
    """
    Prints formatted character sheet
    Returns: None (prints to console)

    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    print(f"=== CHARACTER SHEET ===")
    with open(character_file, "r") as file:
        print(file.read())

def level_up(character,save_name):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    level_up = input("Do you want to level up?(Yes or No): ")
    while level_up == "Yes":
        character["level"] += 1
        print(f"Want to level up again? (Yes or No): {character['level']}")
        level_up = input()
        save_character(character, save_name)
    if level_up == "No":
        print("Level up cancelled.")
    print(f"Character Leveled up! Level: {character['level']}")
    save_character(character, save_name)

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    level = 1
    print("Do you have a character already? (Yes or No): ")
    existing_character = input()
    while existing_character == "Yes":
        filename = input("Enter file name: ")
        load_character(filename)
    hero_type = input("What type of hero are you?: ")
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    while hero_type not in valid_classes:
        print("Invalid class!")
        hero_type = input("What type of hero are you? (Choose from Warrior, Mage, Rogue, Cleric): ")
    hero_name = input("Enter your hero's name: ")
    save_name = input("Enter filename: ")
    character = create_character(hero_name, hero_type, level)
    level_up(character, save_name)
    display_character(save_name)
    print()

    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
