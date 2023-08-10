def select_character_tank_class():
    tank_classes = ["Paladin", "Warrior", "Dark Knight", "Gunbreaker"]
    tank_level = []
    minimum_level = 1
    maximum_level = 90

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
                            print("Not a valid range. Levels are from 1 - 90.")
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

            # try:

            #     if user_selected_tank_level < minimum_level or user_selected_tank_level > maximum_level:
            #         print("Invalid level range. Levels range from 1 to 90.")
            #     tank_level.append(user_selected_tank_level)
            # except ValueError:

            # not_selected_class = False


select_character_tank_class()