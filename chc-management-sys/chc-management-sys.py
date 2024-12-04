import os


class Character:
    def __init__(self, character_name, description, level, health):
        self.character_name = character_name
        self.description = description
        self.level = level
        self.health = health


class Weapon:
    def __init__(self, name, description, damage, level):
        self.name = name
        self.description = description
        self.damage = damage
        self.level = level


class Armor:
    def __init__(self, name, description, defense, level):
        self.name = name
        self.description = description
        self.defense = defense
        self.level = level


def create_character():
    character_name = input("\nEnter character name: ")
    description = input("Enter character description: ")
    level = int(input("Enter character level (1-99): "))
    level = max(1, min(level, 99))
    health = int(input("Enter character health: "))
    character = Character(character_name, description, level, health)
    save_character(character)
    print("\nCharacter successfully joined the party!")


def save_character(character):
    file_name = f"{character.character_name.replace(' ', '_')}_character.txt"
    with open(file_name, "w") as file:
        file.write(f"{character.character_name},{character.description}, {character.level}, {character.health}")


def delete_character():
    character_files = [f for f in os.listdir() if f.endswith("_character.txt")]
    if not character_files:
        print("\nUnfortunately, you have no members in your party.")
        return

    print("\nMembers of the Party:")
    for i, file_name in enumerate(character_files):
        print(f"{i + 1}. {file_name.replace('_character.txt', '').replace('_', ' ')}")

    while True:
        try:
            choice = int(input("\nSelect character to retire: "))
            if 1 <= choice <= len(character_files):
                os.remove(character_files[choice - 1])
                print("\nCharacter retired. Goodbye...")
                break
            else:
                print("\nInvalid choice.")
        except ValueError:
            print("\nInvalid choice. Please enter a number.")


def edit_character():
    character_files = [f for f in os.listdir() if f.endswith("_character.txt")]
    if not character_files:
        print("\nUnfortunately, you have no members in your party.")
        return

    print("\nAvailable Party Members:")
    for i, file_name in enumerate(character_files):
        print(f"{i + 1}. {file_name.replace('_character.txt', '').replace('_', ' ')}")

    while True:
        try:
            choice = int(input("\nSelect a party member to 'fix': "))
            if 1 <= choice <= len(character_files):
                file_name = character_files[choice - 1]
                with open(file_name, "r") as file:
                    file.readlines()
                    description = input("\nEnter new character description: ")
                    level = int(input("Enter new character level (1-99): "))
                    level = max(1, min(level, 99))
                    health = int(input("Enter new character health: "))
                    character = Character(file_name.replace('_character.txt', ''), description, level, health)
                    save_character(character)
                    print("\nParty member 'fixed' successfully.")
                    break
            else:
                print("\nInvalid choice.")
        except ValueError:
            print("\nInvalid choice. Please enter a number.")


def view_all_characters():
    character_files = [f for f in os.listdir() if f.endswith("_character.txt")]
    if not character_files:
        print("\nUnfortunately, you have no members in your party.")
        return

    print("\nAll Party Members:")
    for i, file_name in enumerate(character_files):
        with open(file_name, "r") as file:
            character_data = file.readline().strip().split(",")
            character_data = [data.strip() for data in character_data]
            name, description, level, health = character_data
            view_all_characters = f"{i + 1}. {name}\n- {description}\nLVL: {level}\nHP: {health}\n"
            print(view_all_characters.replace('_', ' '))


def create_weapon():
    name = input("\nEnter weapon name: ")
    description = input("Enter weapon description: ")
    damage = int(input("Enter weapon damage: "))
    level = int(input("Enter weapon level: "))
    return Weapon(name, description, damage, level)


def save_weapon(weapon):
    file_name = f"{weapon.name.replace(' ', '_')}_weapon.txt"
    with open(file_name, "w") as file:
        file.write(f"{weapon.name},{weapon.description},{weapon.damage},{weapon.level}\n")


def delete_weapon():
    weapon_files = [f for f in os.listdir() if f.endswith("_weapon.txt")]
    if not weapon_files:
        print("\nNo weapons found in inventory.")
        return

    print("\nWeapons in Inventory:")
    for i, file_name in enumerate(weapon_files):
        print(f"{i + 1}. {file_name.replace('_weapon.txt', '').replace('_', ' ')}")

    while True:
        try:
            choice = int(input("\nSelect weapon to delete: "))
            if 1 <= choice <= len(weapon_files):
                os.remove(weapon_files[choice - 1])
                print("\nWeapon destroyed successfully.")
                break
            else:
                print("\nInvalid choice.")
        except ValueError:
            print("\nInvalid choice. Please enter a number.")


def edit_weapon():
    weapon_files = [f for f in os.listdir() if f.endswith("_weapon.txt")]
    if not weapon_files:
        print("\nNo weapons found in inventory.")
        return

    print("\nWeapons in Inventory:")
    for i, file_name in enumerate(weapon_files):
        print(f"{i + 1}. {file_name.replace('_weapon.txt', '').replace('_', ' ')}")

    while True:
        try:
            choice = int(input("\nSelect weapon to sharpen: "))
            if 1 <= choice <= len(weapon_files):
                file_name = weapon_files[choice - 1]
                with open(file_name, "r") as file:
                    weapon_data = file.readline().strip().split(",")
                    name, description, damage, level = weapon_data
                    description = input("Enter new weapon description: ")
                    damage = int(input("Enter new weapon damage: "))
                    level = int(input("Enter new weapon level: "))
                    new_weapon = Weapon(name, description, damage, level)
                    save_weapon(new_weapon)
                    print("\nWeapon sharpened successfully!")
                    break
            else:
                print("\nInvalid choice.")
        except ValueError:
            print("\nInvalid choice. Please enter a number.")


def view_weapons():
    weapon_files = [f for f in os.listdir() if f.endswith("_weapon.txt")]
    if not weapon_files:
        print("\nNo weapons found in inventory.")
        return

    print("\nWeapons in Inventory:")
    for i, file_name in enumerate(weapon_files):
        with open(file_name, "r") as file:
            weapon_data = file.readline().strip().split(",")
            name, description, damage, level = weapon_data
            view_weapons = f"{i + 1}. {name}\n- {description}\nDMG: {damage}\nLVL: {level}\n"
            print(view_weapons.replace('_', ' '))


def create_armor():
    name = input("\nEnter armor name: ")
    description = input("Enter armor description: ")
    defense = int(input("Enter armor defense: "))
    level = int(input("Enter armor level: "))
    return Armor(name, description, defense, level)


def save_armor(armor):
    file_name = f"{armor.name.replace(' ', '_')}_armor.txt"
    with open(file_name, "w") as file:
        file.write(f"{armor.name},{armor.description},{armor.defense},{armor.level}\n")


def delete_armor():
    armor_files = [f for f in os.listdir() if f.endswith("_armor.txt")]
    if not armor_files:
        print("\nNo armor found in wardrobe.")
        return

    print("\nAvailable Armor:")
    for i, file_name in enumerate(armor_files):
        print(f"{i + 1}. {file_name.replace('_armor.txt', '').replace('_', ' ')}")

    while True:
        try:
            choice = int(input("\nSelect armor to destroy: "))
            if 1 <= choice <= len(armor_files):
                os.remove(armor_files[choice - 1])
                print("\nArmor destroyed successfully!")
                break
            else:
                print("\nInvalid choice.")
        except ValueError:
            print("\nInvalid choice. Please enter a number.")


def edit_armor():
    armor_files = [f for f in os.listdir() if f.endswith("_armor.txt")]
    if not armor_files:
        print("\nNo armor found in wardrobe.")
        return

    print("\nArmor in Wardrobe:")
    for i, file_name in enumerate(armor_files):
        print(f"{i + 1}. {file_name.replace('_armor.txt', '').replace('_', ' ')}")

    while True:
        try:
            choice = int(input("\nSelect armor to repair: "))
            if 1 <= choice <= len(armor_files):
                file_name = armor_files[choice - 1]
                with open(file_name, "r") as file:
                    armor_data = file.readline().strip().split(",")
                    name, description, defense, level = armor_data
                    description = input("Enter new armor description: ")
                    defense = int(input("Enter new armor defense: "))
                    level = int(input("Enter new armor level: "))
                    new_armor = Armor(name, description, defense, level)
                    save_armor(new_armor)
                    print("\nArmor repaired successfully.")
                    break
            else:
                print("\nInvalid choice.")
        except ValueError:
            print("\nInvalid choice. Please enter a number.")


def view_armor():
    armor_files = [f for f in os.listdir() if f.endswith("_armor.txt")]
    if not armor_files:
        print("\nNo armor found in wardrobe.")
        return

    print("\nArmor in Wardrobe:")
    for i, file_name in enumerate(armor_files):
        with open(file_name, "r") as file:
            armor_data = file.readline().strip().split(",")
            name, description, defense, level = armor_data
            view_armor = f"{i + 1}. {name}\n- {description}\nDEF: {defense}\nLVL: {level}\n"
            print(view_armor.replace('_', ' '))


def main_menu():
    print()
    print("Welcome, adventurer, to the RPG Character Management System!")
    print("Choose your action:")
    print("1. Manage Characters")
    print("2. Manage Weapons")
    print("3. Manage Armor")
    print("4. Exit")


def character_menu():
    print("\nCharacter Menu:")
    print("1. Create New Character")
    print("2. Delete Character")
    print("3. Edit Character")
    print("4. View All Characters")
    print("5. Return to Main Menu")


def weapon_menu():
    print("\nWeapon Menu:")
    print("1. Create New Weapon")
    print("2. Delete Weapon")
    print("3. Edit Weapon")
    print("4. View All Weapons")
    print("5. Return to Main Menu")


def armor_menu():
    print("\nArmor Menu:")
    print("1. Create New Armor")
    print("2. Delete Armor")
    print("3. Edit Armor")
    print("4. View All Armor")
    print("5. Return to Main Menu")


def main():
    while True:
        main_menu()
        choice = input("\nPlease select an option: ")

        if choice == "1":
            while True:
                character_menu()
                character_choice = input("\nPlease select an option: ")

                if character_choice == "1":
                    create_character()
                elif character_choice == "2":
                    delete_character()
                elif character_choice == "3":
                    edit_character()
                elif character_choice == "4":
                    view_all_characters()
                elif character_choice == "5":
                    break
                else:
                    print("\nInvalid choice.")

        elif choice == "2":
            while True:
                weapon_menu()
                weapon_choice = input("\nPlease select an option: ")

                if weapon_choice == "1":
                    weapon = create_weapon()
                    save_weapon(weapon)
                    print("\nWeapon forged successfully!")
                elif weapon_choice == "2":
                    delete_weapon()
                elif weapon_choice == "3":
                    edit_weapon()
                elif weapon_choice == "4":
                    view_weapons()
                elif weapon_choice == "5":
                    break
                else:
                    print("\nInvalid choice.")

        elif choice == "3":
            while True:
                armor_menu()
                armor_choice = input("\nPlease select an option: ")

                if armor_choice == "1":
                    armor = create_armor()
                    save_armor(armor)
                    print("\nArmor crafted successfully!")
                elif armor_choice == "2":
                    delete_armor()
                elif armor_choice == "3":
                    edit_armor()
                elif armor_choice == "4":
                    view_armor()
                elif armor_choice == "5":
                    break
                else:
                    print("\nInvalid choice.")

        elif choice == "4":
            print("\nFarewell, adventurer! \n"
                  "Until next time...")
            break

        else:
            print("\nInvalid choice. Please enter a number.")


if __name__ == "__main__":
    main()
