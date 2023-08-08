"""I plan on taking some information from my personal ff14 playable character and just trying to see all the stats
   based on different job classes. Write them to a file and just analyze the information."""


# Avatar class is supposed to create a character which we will fill up with information
class Avatar:
    def __init__(self, name, gender, race, character_level):
        self.name = name
        self.gender = gender
        self.race = race
        self.character_level = character_level

    def get_name(self):
        return self.name

    def get_basic_info(self):
        return (f"Name: {self.name}\n"
                f"Gender: {self.gender}\n"
                f"Race: {self.race}\n"
                f"Level: {self.character_level}\n")
        # info_dictionary = {"Name": self.name,
        #                    "Gender": self.gender,
        #                    "Race": self.race,
        #                    "Role": self.role,
        #                    "Class": self.character_class
        #                    }
        # return info_dictionary


    # def __str__(self):
    #     return (f"Name: {self.name}\n"
    #             f"Gender: {self.gender}\n"
    #             f"Race: {self.race}\n"
    #             f"Role: {self.role}\n"
    #             f"Class: {self.character_class}")


# Weapon class creates a weapon that accepts a weapon name, weapon class and item level
class Weapon:
    def __init__(self, weapon_name, weapon_class, weapon_item_level):
        self.weapon_name = weapon_name
        self.weapon_class = weapon_class
        self.weapon_item_level = weapon_item_level


# Since there are basically 2 different types of combat weapon types. Class Magical still needs the previous attributes
# but we will be adding magical damage here.
class MagicalWeapon(Weapon):
    def __init__(self, weapon_name, weapon_class, weapon_item_level, magical_damage):
        super().__init__(weapon_name, weapon_class, weapon_item_level)
        self.magical_damage = magical_damage

    def get_magic_weapon_info(self):
        return (f"Weapon: {self.weapon_name}\n"
                f"Equip class: {self.weapon_class}\n"
                f"Item level: {self.weapon_item_level}\n"
                f"Magic damage: {self.magical_damage}\n")

    # def __str__(self):
    #     return (f"Weapon name: {self.weapon_name}\n"
    #             f"Weapon class: {self.weapon_class}\n"
    #             f"Item level: {self.weapon_item_level}\n"
    #             f"Magic Damage: {self.magical_damage}\n")


# PhysicalWeapon is like MagicalWeapon that only the type of damage differs and will be labeled as physical damage
class PhysicalWeapon(Weapon):
    def __init__(self, weapon_name, weapon_class, weapon_item_level, physical_damage):
        super().__init__(weapon_name, weapon_class, weapon_item_level)
        self.physical_damage = physical_damage

    def __str__(self):
        return (f"Weapon: {self.weapon_name}\n"
                f"Equip class: {self.weapon_class}\n"
                f"Item level: {self.weapon_item_level}\n"
                f"Physical Damage: {self.physical_damage}\n")


sophie = Avatar("Sophie", "Female", "Midlander", 90)
knee_height = Avatar("Mountain", "Male", "Lalafell", 90)

dark_knight_weapon = PhysicalWeapon("Shadowbringer", "Dark Knight", 530, 90)
white_mage_weapon = MagicalWeapon("Staff", "White Mage", 1, 20)


def add_to_page(character_info, weapon_info):
    with open(f"{sophie.get_name()}.txt", "a+") as my_character_info:
        my_character_info.write(character_info)
        my_character_info.write(weapon_info)


def select_character_role():
    # character_role = []
    not_selected_character = True
    while not_selected_character:
        user_selects = input("Select a role: Type (t) for Tank, (h) for Healer or (d) for Dps").lower()

        if user_selects == "t":
            not_selected_character = False
            # character_role.append(user_selects)
            return "Tank"
        elif user_selects == "h":
            # character_role.append(user_selects)
            not_selected_character = False
            return "Healer"
        elif user_selects == "d":
            # character_role.append(user_selects)
            not_selected_character = False
            return "Dps"
        elif user_selects == "q":
            return "Exiting selection"
        else:
            print("Invalid input. Try again.")


def select_character_tank_class():
    tank_classes = ["Paladin", "Warrior", "Dark Knight", "Gunbreaker"]

    not_selected_class = True
    while not_selected_class:
        user_selected_tank_class = input("Type the exact tank class (Ignore capitalization): ").title()
        if user_selected_tank_class in tank_classes:
            not_selected_class = False
            return user_selected_tank_class
        else:
            print("Class not found. Try again.")


def select_character_healer_class():
    healer_classes = ["White Mage", "Scholar", "Astrologian", "Sage"]

    not_selected_class = True
    while not_selected_class:
        user_selected_healer_class = input("Type the exact healer class (Ignore capitalization): ").title()
        if user_selected_healer_class in healer_classes:
            not_selected_class = False
            return user_selected_healer_class
        else:
            print("Class not found. Try again.")


def select_character_dps_class():
    dps_classes = ["Dragoon", "Monk", "Ninja", "Samurai", "Reaper", "Bard", "Machinist" "Dancer", "Black Mage",
                   "Summoner", "Red Mage", "Blue Mage"]

    not_selected_class = True
    while not_selected_class:
        user_selected_dps_class = input("Type the exact dps class (Ignore capitalization): ").title()
        if user_selected_dps_class in dps_classes:
            not_selected_class = False
            return user_selected_dps_class
        else:
            print("Class not found. Try again.")




# print(select_character_role())
# print(select_character_tank_class())
# print(select_character_healer_class())
print(select_character_dps_class())
# add_to_page(sophie.get_basic_info(), white_mage_weapon.get_magic_weapon_info())
# print(sophie.get_basic_info())
# print(white_mage_weapon)
# print(knee_height)
# print(dark_knight_weapon)