"""I plan on taking some information from my personal ff14 playable character and just trying to see all the stats
   based on different job classes. Write them to a file and just analyze the information."""


# Avatar class is supposed to create a character which we will fill up with information
class Avatar:
    def __init__(self, name, gender, race, role, character_class):
        self.name = name
        self.gender = gender
        self.race = race
        self.role = role
        self.character_class = character_class

    def get_name(self):
        return self.name

    def get_basic_info(self):
        return (f"Name: {self.name}\n"
                f"Gender: {self.gender}\n"
                f"Race: {self.race}\n"
                f"Role: {self.role}\n"
                f"Class: {self.character_class}\n")
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

    def __str__(self):
        return (f"Weapon name: {self.weapon_name}\n"
                f"Weapon class: {self.weapon_class}\n"
                f"Item level: {self.weapon_item_level}\n"
                f"Magic Damage: {self.magical_damage}\n")


# PhysicalWeapon is like MagicalWeapon that only the type of damage differs and will be labeled as physical damage
class PhysicalWeapon(Weapon):
    def __init__(self, weapon_name, weapon_class, weapon_item_level, physical_damage):
        super().__init__(weapon_name, weapon_class, weapon_item_level)
        self.physical_damage = physical_damage

    def __str__(self):
        return (f"Weapon name: {self.weapon_name}\n"
                f"Weapon class: {self.weapon_class}\n"
                f"Item level: {self.weapon_item_level}\n"
                f"Physical Damage: {self.physical_damage}\n")


sophie = Avatar("Sophie than", "Female", "Midlander", "Healer", "White Mage")
knee_height = Avatar("Mountain", "Male", "Lalafell", "Tank", "Dark Knight")

dark_knight_weapon = PhysicalWeapon("Shadowbringer", "Dark Knight", 530, 90)
white_mage_weapon = MagicalWeapon("Staff", "White Mage", 1, 20)


def add_to_page(info):
    with open(f"{sophie.get_name()}.txt", "a+") as my_character_info:
        my_character_info.write(info)


add_to_page(sophie.get_basic_info())
# print(sophie.get_basic_info())
# print(white_mage_weapon)
# print(knee_height)
# print(dark_knight_weapon)