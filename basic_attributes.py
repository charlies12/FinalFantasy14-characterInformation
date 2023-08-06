class Avatar:
    def __init__(self, name, gender, race, role, character_class):
        self.name = name
        self.gender = gender
        self.race = race
        self.role = role
        self.character_class = character_class

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Gender: {self.gender}\n"
                f"Race: {self.race}\n"
                f"Role: {self.role}\n"
                f"Class: {self.character_class}")


class Weapon:
    def __init__(self, weapon_name, weapon_class, weapon_item_level):
        self.weapon_name = weapon_name
        self.weapon_class = weapon_class
        self.weapon_item_level = weapon_item_level


class MagicalWeapon(Weapon):
    def __init__(self, weapon_name, weapon_class, weapon_item_level, magical_damage):
        super().__init__(weapon_name, weapon_class, weapon_item_level)
        self.magical_damage = magical_damage

    def __str__(self):
        return (f"Weapon name: {self.weapon_name}\n"
                f"Weapon class: {self.weapon_class}\n"
                f"Item level: {self.weapon_item_level}\n"
                f"Magic Damage: {self.magical_damage}\n")


class PhysicalWeapon(Weapon):
    def __init__(self, weapon_name, weapon_class, weapon_item_level, physical_damage):
        super().__init__(weapon_name, weapon_class, weapon_item_level)
        self.physical_damage = physical_damage

    def __str__(self):
        return (f"Weapon name: {self.weapon_name}\n"
                f"Weapon class: {self.weapon_class}\n"
                f"Item level: {self.weapon_item_level}\n"
                f"Physical Damage: {self.physical_damage}\n")


sophie = Avatar("Sophie", "Female", "Midlander", "Healer", "White Mage")
knee_height = Avatar("Mountain", "Male", "Lalafell", "Tank", "Dark Knight")

dark_knight_weapon = PhysicalWeapon("Shadowbringer", "Dark Knight", 530, 90)
white_mage_weapon = MagicalWeapon("Staff", "White Mage", 1, 20)
print(sophie)
print(white_mage_weapon)
print(knee_height)
print(dark_knight_weapon)