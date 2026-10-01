import os
import random
import time

dungeon = 1
level = 1

RARITY_MULTIPLIERS = {
    'Common': 1.0,
    'Uncommon': 1.3,
    'Rare': 1.6,
    'Epic': 2.0,
    'Legendary': 3.0
}
quests = [
{},
{}
]



def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Weapon:
    def __init__(self, weapon_type, rarity, power, speed):
        self.type = weapon_type
        self.rarity = rarity
        self.power = power
        self.speed = speed


class Character:
    def __init__(self, dungeon=1, level=1):
        self.dungeon = dungeon
        self.level = level
        self.name = "Hero"
        self.role = None
        self.weapon = None
        self.create_character()

    def roll_weapon_rarity(self):
        rarity_roll = random.randint(1, 100)
        if 1 <= rarity_roll <= 40:
            return 'Common'
        elif 41 <= rarity_roll <= 70:
            return 'Uncommon'
        elif 71 <= rarity_roll <= 90:
            return 'Rare'
        elif 91 <= rarity_roll <= 99:
            return 'Epic'
        else:
            return 'Legendary'

    def calculate_stat(self, base_min, base_max, rarity):
        base_stat = random.randint(base_min, base_max * self.level * self.dungeon)
        multiplier = RARITY_MULTIPLIERS.get(rarity, 1.0)
        return int(base_stat * multiplier)

    def create_character(self):
        clear_screen()
        self.name = input("What is your name young traveler:\n")
        print("This land has been plagued by an ultimate demon lord", flush=True)
        time.sleep(1)
        print("He has been summoned after peace in this kingdom for 100 years", flush=True)
        time.sleep(1)
        print(f"It is your job young hero {self.name} to defeat the demon lord", flush=True)
        time.sleep(1)
        print("I wish great luck upon you. May the gods be with you...", flush=True)
        time.sleep(1)

        while True:
            print("\nWhat Class do you choose?")
            print("1.) Warrior\n2.) Ranged\n3.) Mage")
            try:
                class_input = int(input("> "))
            except ValueError:
                class_input = 0

            if class_input in (1, 2, 3):
                break
            print("\nInvalid selection! Please pick option 1, 2, or 3.")

        if class_input == 1:
            self.role = "Warrior"
            print("\nYou have chosen the Warrior class!")
            while True:
                print("Choose your weapon path:\n1.) Assassin (Daggers)\n2.) Greatsword Wielder (Greatsword)\n3.) Knight (Shortsword)")
                try:
                    class_selection = int(input("> "))
                except ValueError:
                    class_selection = 0
                
                if class_selection == 1:
                    weapon_config = ('Daggers', 8, 12, 12, 16)
                    break
                elif class_selection == 2:
                    weapon_config = ('Greatsword', 18, 25, 4, 8)
                    break
                elif class_selection == 3:
                    weapon_config = ('Shortsword', 12, 18, 8, 12)
                    break
                else:
                    print("\nInvalid weapon choice. Pick 1, 2, or 3.\n")

        elif class_input == 2:
            self.role = "Ranged"
            print("\nYou have chosen the Ranged class!")
            while True:
                print("Choose your weapon path:\n1.) Archer (Longbow)\n2.) Gunslinger (Dual Pistols)\n3.) Sniper (Crossbow)")
                try:
                    class_selection = int(input("> "))
                except ValueError:
                    class_selection = 0

                if class_selection == 1:
                    weapon_config = ('Longbow', 14, 20, 8, 12)
                    break
                elif class_selection == 2:
                    weapon_config = ('Dual Pistols', 9, 14, 15, 20)
                    break
                elif class_selection == 3:
                    weapon_config = ('Crossbow', 22, 30, 3, 6)
                    break
                else:
                    print("\nInvalid weapon choice. Pick 1, 2, or 3.\n")

        elif class_input == 3:
            self.role = "Mage"
            print("\nYou have chosen the Mage class!")
            while True:
                print("Choose your weapon path:\n1.) Elementalist (Arcane Staff)\n2.) Necromancer (Grimoire)\n3.) Battlemage (Magic Orb)")
                try:
                    class_selection = int(input("> "))
                except ValueError:
                    class_selection = 0

                if class_selection == 1:
                    weapon_config = ('Arcane Staff', 16, 24, 6, 10)
                    break
                elif class_selection == 2:
                    weapon_config = ('Grimoire', 20, 28, 4, 7)
                    break
                elif class_selection == 3:
                    weapon_config = ('Magic Orb', 10, 16, 10, 15)
                    break
                else:
                    print("\nInvalid weapon choice. Pick 1, 2, or 3.\n")

        w_type, min_p, max_p, min_s, max_s = weapon_config
        rarity = self.roll_weapon_rarity()
        final_power = self.calculate_stat(min_p, max_p, rarity)
        final_speed = self.calculate_stat(min_s, max_s, rarity)

        self.weapon = Weapon(w_type, rarity, final_power, final_speed)
        print(f"\nYou equipped: {self.weapon.type}")
        time.sleep(1.5)

    def display_stats(self):
        clear_screen()
        print(f"--- {self.name} ---")
        print(f"Class: {self.role}")
        print(f"Level: {self.level} | Dungeon Depth: {self.dungeon}")
        print("\n--- Weapon Stats ---")
        print(f"Type: {self.weapon.type}")
        print(f"Rarity: {self.weapon.rarity}")
        print(f"Attack Power: {self.weapon.power}")
        print(f"Attack Speed: {self.weapon.speed}")

def explore():
    print("Where would you like to explore?\n")
    choice_of_exploration = input("1.)")

def view_quests(quests):
    if not quests or all(not q for q in quests):
        print("There are no quests.")
    else:
        print("=== Quests ===")
        side_or_main = input("Would you like to view (1) Main Quests or (2) Side Quests?\n> ")
        if side_or_main == '1':
            print("\n--- Main Quests ---")
            side_quests = quests["mainquests"] if "mainquests" in quests else {}
            if not side_quests:
                print("There are no main quests.")
                return
        elif side_or_main == '2':
            print("\n--- Side Quests ---")
            side_quests = quests["sidequests"] if "sidequests" in quests else {}
            if not side_quests:
                print("There are no side quests.")
            print("\n--- Side Quests ---")
        else:
            print("Invalid selection. Please choose 1 or 2.")
            return
        
# Main Execution
player = Character(dungeon=dungeon, level=level)

game_running = True
while game_running:
    clear_screen()
    print("=== MAIN MENU ===")
    print("1.) View Stats")
    print("2.) Explore")
    print("3.) View Quests")
    print("4.) Exit Game")
    
    try:
        choice_of_action = int(input("\nWhat would you like to do now young hero?\n> "))
    except ValueError:
        choice_of_action = 0

    if choice_of_action == 1:
        player.display_stats()
        input("\nPress Enter to return to the menu...")
    elif choice_of_action == 2:
        explore()
        input("\nPress Enter to return to the menu...")
    elif choice_of_action == 3:
        clear_screen()
        view_quests(quests)
        input("\nPress Enter to return to the menu...")
    elif choice_of_action == 4:
        print("\nThank you for playing!")
        game_running = False
    else:
        print("\nSorry, that is not a valid input.")
        time.sleep(1)


