"""I plan on taking some information from my personal ff14 playable character and just trying to see all the stats
   based on different job classes. Write them to a file and just analyze the information."""


# Avatar class is supposed to create a character which we will fill up with information
class Avatar:
    def __init__(self, name, gender, race):
        self.name = name
        self.gender = gender
        self.race = race

    def get_name(self):
        return self.name

    def get_basic_info(self):
        return (f"Name: {self.name}\n"
                f"Gender: {self.gender}\n"
                f"Race: {self.race}\n")
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


sophie = Avatar("Sophie", "Female", "Midlander")
knee_height = Avatar("Mountain", "Male", "Lalafell")

dark_knight_weapon = PhysicalWeapon("Shadowbringer", "Dark Knight", 530, 90)
white_mage_weapon = MagicalWeapon("Staff", "White Mage", 1, 20)


# Asks what role to pick. Tank, Healer or DPS
def select_character_role():
    # character_role = []
    not_selected_character = True
    while not_selected_character:
        user_selects = input("Select a role: Type (t) for Tank, (h) for Healer or (d) for Dps and (q) to quit.").lower()

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


# select_character_tank_class has a list of all tank classes. Returns a class if user input matches name on  tank list.
def select_character_tank_class():
    tank_classes = ["Paladin", "Warrior", "Dark Knight", "Gunbreaker"]
    tank_level = []

    not_selected_class = True
    not_selected_tank_level = True
    minimum_level = 1
    maximum_level = 90
    try:
        while not_selected_class:
            user_selected_tank_class = input("Type the exact tank class (Ignore capitalization): ").title()

            if user_selected_tank_class in tank_classes:
                while not_selected_tank_level:
                    try:
                        user_selected_tank_level = int(input(f"Enter {user_selected_tank_class} level: "))
                        if user_selected_tank_level < minimum_level or user_selected_tank_level > maximum_level:
                            print("Not a valid range. Levels go from 1 - 90.")
                        else:
                            tank_level.append(user_selected_tank_level)
                            not_selected_tank_level = False
                    except ValueError:
                        print("That is not a number")
            else:
                print("Class not found. Try again.")
            return user_selected_tank_class, tank_level
    except ValueError:
        print("Enter a valid number.")
    # while not_selected_class:
    #     user_selected_tank_class = input("Type the exact tank class (Ignore capitalization): ").title()
    #     if user_selected_tank_class in tank_classes:
    #         try:
    #             user_selected_tank_level = int(input(f"Enter {user_selected_tank_class} level: "))
    #             if user_selected_tank_level < minimum_level or user_selected_tank_level > maximum_level:
    #                 print("Invalid level range. Levels range from 1 to 90.")
    #             tank_level.append(user_selected_tank_level)
    #         except ValueError:
    #             print("Enter valid numbers.")
    #         not_selected_class = False
    #         return user_selected_tank_class, tank_level
    #     else:
    #         print("Class not found. Try again.")


# select_character_healer_class has a list of playable healer classes. Returns class if user input matches name on list.
def select_character_healer_class():
    healer_classes = ["White Mage", "Scholar", "Astrologian", "Sage"]
    healer_level = []

    not_selected_class = True
    not_selected_healer_level = True
    minimum_level = 1
    maximum_level = 90

    try:
        while not_selected_class:
            user_selected_healer_class = input("Type the exact healer class (Ignore capitalization): ").title()
            if user_selected_healer_class in healer_classes:
                while not_selected_healer_level:
                    try:
                        user_selected_healer_level = int(input(f"Enter {user_selected_healer_class} level: "))
                        if user_selected_healer_level < minimum_level or user_selected_healer_level > maximum_level:
                            print("Not a valid range. Levels are from 1 - 90.")
                        else:
                            healer_level.append(user_selected_healer_level)
                            not_selected_healer_level = False
                    except ValueError:
                        print("That is not a number.")
            else:
                print("Class not found. Try again.")
            return user_selected_healer_class, healer_level
    except ValueError:
        print("Enter a valid number.")


# select_character_dps_class has a list of playable dps class. Returns class if user input matches name on list.
def select_character_dps_class():
    dps_classes = ["Dragoon", "Monk", "Ninja", "Samurai", "Reaper", "Bard", "Machinist", "Dancer", "Black Mage",
                   "Summoner", "Red Mage", "Blue Mage"]
    dps_level = []

    not_selected_class = True
    not_selected_dps_level = True
    minimum_level = 1
    maximum_level = 90
    try:
        while not_selected_class:
            user_selected_dps_class = input("Type the exact dps class (Ignore capitalization): ").title()
            if user_selected_dps_class in dps_classes:
                while not_selected_dps_level:
                    try:
                        user_selected_dps_level = int(input(f"Enter {user_selected_dps_class} level: "))
                        if user_selected_dps_level < minimum_level or user_selected_dps_level > maximum_level:
                            print(f"Invalid range. Levels are from {minimum_level} - {maximum_level}.")
                        else:
                            dps_level.append(user_selected_dps_level)
                            not_selected_dps_level = False
                    except ValueError:
                        print("That is not a number.")
            else:
                print("Class not found. Try again.")
            return user_selected_dps_class, dps_level
    except ValueError:
        print("Enter a valid number.")


# print(select_character_role())
# print(select_character_tank_class())
# print(select_character_healer_class())
# print(select_character_dps_class())
# add_to_page(sophie.get_basic_info(), white_mage_weapon.get_magic_weapon_info())
print(sophie.get_basic_info())

# print(white_mage_weapon)
# print(knee_height)
# print(dark_knight_weapon)


# returns a list of jobs unlocked by character
def form_a_list_of_jobs():
    my_jobs = []
    continue_asking = True
    while continue_asking:
        match select_character_role():
            case "Tank":
                my_jobs.append(select_character_tank_class())

            case "Healer":
                my_jobs.append(select_character_healer_class())

            case "Dps":
                my_jobs.append(select_character_dps_class())
            case _:
                print("(q)uit")
                continue_asking = False
    return my_jobs


# add_to_page writes to a file with the character name as file title.
def add_to_page(character_info):
    with open(f"{sophie.get_name()}.txt", "a+") as my_character_info:
        my_character_info.write(character_info)
        for job in form_a_list_of_jobs():
            my_character_info.write(f"{job}\n")

        # my_character_info.write(weapon_info)
# print(form_a_list_of_jobs())


add_to_page(sophie.get_basic_info())