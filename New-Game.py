class Game:

    def __init__(self):
        self.players = []
        self.active_player = None

    # =====================================================================
    # SIMPLIFIED CHARACTER CREATION
    # =====================================================================
    def create_character(self):
        print("\n=== CHARACTER CREATION ===")
        name = input("Enter your character's name: ").strip()

        print("\nChoose a Main Class:")
        print("[1] Mage  [2] Warrior  [3] Heavy Weapon Wielder  [4] Archer")
        class_choice = input("Select (1-4): ").strip()

        if class_choice == "1":
            print("\nSelect Mage Subclass:")
            print("[1] ArcMage  [2] Elementalist  [3] Necromancer  [4] Healer")
            sub = input("Select (1-4): ").strip()
            player_cls = (
                self.Elementalist
                if sub == "2"
                else (
                    self.Necromancer
                    if sub == "3"
                    else self.Healer if sub == "4" else self.ArcMage
                )
            )

        elif class_choice == "2":
            print("\nSelect Warrior Subclass:")
            print(
                "[1] ShortSword  [2] Assassin  [3] HolyWarrior  [4] Barbarian"
            )
            sub = input("Select (1-4): ").strip()
            player_cls = (
                self.Assassin
                if sub == "2"
                else (
                    self.HolyWarrior
                    if sub == "3"
                    else self.Barbarian if sub == "4" else self.ShortSword
                )
            )

        elif class_choice == "3":
            print("\nSelect Heavy Weapon Wielder Subclass:")
            print(
                "[1] Juggernaut  [2] SkullSplitter  [3] MorningStar  [4]"
                " Halberd"
            )
            sub = input("Select (1-4): ").strip()
            player_cls = (
                self.SkullSplitter
                if sub == "2"
                else (
                    self.MorningStar
                    if sub == "3"
                    else self.Halberd if sub == "4" else self.Juggernaut
                )
            )

        else:
            print("\nSelect Archer Subclass:")
            print("[1] LongBow  [2] Crossbow  [3] Sniper  [4] Hunter")
            sub = input("Select (1-4): ").strip()
            player_cls = (
                self.Crossbow
                if sub == "2"
                else (
                    self.Sniper
                    if sub == "3"
                    else self.Hunter if sub == "4" else self.LongBow
                )
            )

        player = player_cls(name)
        self.players.append(player)
        print(
            f"\nSuccessfully created {player.name} ({player.__class__.__name__})!"
        )
        return player

    # =====================================================================
    # CHARACTER SELECTION
    # =====================================================================
    def select_character(self):
        if not self.players:
            print(
                "\nNo characters available! Please create a character first."
            )
            return None

        print("\n=== SELECT YOUR CHARACTER ===")
        for index, p in enumerate(self.players, start=1):
            print(f"[{index}] {p.name} - Class: {p.__class__.__name__}")

        choice = input(f"Choose a character (1-{len(self.players)}): ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(self.players):
            selected = self.players[int(choice) - 1]
            self.active_player = selected
            print(f"\nActive player set to {selected.name}!")
            return selected
        else:
            print("\nInvalid choice.")
            return None

    # =====================================================================
    # PLAY GAME LOOP (MAIN ACTIONS)
    # =====================================================================
    def play_game(self):
        if not self.active_player:
            print("\nYou must select a character before starting the game!")
            return

        print(
            f"\n=== GAME STARTED: Playing as {self.active_player.name} ("
            f"{self.active_player.__class__.__name__}) ==="
        )

        while True:
            print(f"\n--- {self.active_player.name}'s Actions ---")
            print("[1] Explore")
            print("[2] Quest")
            print("[3] Shop")
            print("[4] Return to Main Menu")

            choice = input("Select an action (1-4): ").strip()

            if choice == "1":
                pass  # Explore functionality (where battles originate) to be added later

            elif choice == "2":
                pass  # Quest functionality to be added later

            elif choice == "3":
                pass  # Shop functionality to be added later

            elif choice == "4":
                print(f"\nReturning to main menu from {self.active_player.name}'s session.")
                break

            else:
                print("\nInvalid option. Please enter 1-4.")

    # =====================================================================
    # MAIN MENU LOOP
    # =====================================================================
    def start_game_loop(self):
        print("Welcome to the RPG Game!")

        while True:
            print("\n=== MAIN MENU ===")
            print("[1] Create Character")
            print("[2] Select Active Character")
            print("[3] Start Game")
            print("[4] View All Characters")
            print("[5] Exit Game")

            choice = input("Select an option (1-5): ").strip()

            if choice == "1":
                self.create_character()

            elif choice == "2":
                self.select_character()

            elif choice == "3":
                self.play_game()

            elif choice == "4":
                if not self.players:
                    print("\nNo characters created yet.")
                else:
                    print("\n--- Current Roster ---")
                    for p in self.players:
                        active_status = (
                            " (Active)" if p == self.active_player else ""
                        )
                        print(
                            f"- {p.name} | Class: {p.__class__.__name__} |"
                            f" Weapon: {p.weapon_name} ({p.weapon_damage} DMG)"
                            f"{active_status}"
                        )

            elif choice == "5":
                print("\nThanks for playing!")
                break

            else:
                print("\nInvalid choice. Please pick 1-5.")

    # =====================================================================
    # BASE CLASS & SUBCLASSES
    # =====================================================================
    class Player:

        def __init__(self, name):
            self.name = name
            self.max_health = 100
            self.current_health = 100
            self.weapon_name = "Unarmed"
            self.weapon_damage = 0

    # 1. Mage Branch
    class Mage(Player):

        def __init__(self, name):
            super().__init__(name)
            self.max_health = 80
            self.current_health = 80

    class ArcMage(Mage):

        def __init__(self, name):
            super().__init__(name)
            self.weapon_name = "Starlight Staff"
            self.weapon_damage = 25

    class Elementalist(Mage):

        def __init__(self, name):
            super().__init__(name)
            self.weapon_name = "Elemental Orb"
            self.weapon_damage = 20

    class Necromancer(Mage):

        def __init__(self, name):
            super().__init__(name)
            self.weapon_name = "Bone Wand"
            self.weapon_damage = 18

    class Healer(Mage):

        def __init__(self, name):
            super().__init__(name)
            self.weapon_name = "Sacred Scepter"
            self.weapon_damage = 12

    # 2. Warrior Branch
    class Warrior(Player):

        def __init__(self, name):
            super().__init__(name)
            self.max_health = 120
            self.current_health = 120

    class ShortSword(Warrior):

        def __init__(self, name):
            super().__init__(name)
            self.weapon_name = "Short Sword"
            self.weapon_damage = 15

    class Assassin(Warrior):

        def __init__(self, name):
            super().__init__(name)
            self.weapon_name = "Dual Daggers"
            self.weapon_damage = 22

    class HolyWarrior(Warrior):

        def __init__(self, name):
            super().__init__(name)
            self.weapon_name = "Blessed Longsword"
            self.weapon_damage = 20

    class Barbarian(Warrior):

        def __init__(self, name):
            super().__init__(name)
            self.weapon_name = "Battleaxe"
            self.weapon_damage = 24

    # 3. Heavy Weapon Wielder Branch
    class HeavyWeaponWielder(Player):

        def __init__(self, name):
            super().__init__(name)
            self.max_health = 150
            self.current_health = 150

    class Juggernaut(HeavyWeaponWielder):

        def __init__(self, name):
            super().__init__(name)
            self.weapon_name = "Tower Shield & Warhammer"
            self.weapon_damage = 18

    class SkullSplitter(HeavyWeaponWielder):

        def __init__(self, name):
            super().__init__(name)
            self.weapon_name = "Greatsword"
            self.weapon_damage = 35

    class MorningStar(HeavyWeaponWielder):

        def __init__(self, name):
            super().__init__(name)
            self.weapon_name = "Morningstar Flail"
            self.weapon_damage = 14

    class Halberd(HeavyWeaponWielder):

        def __init__(self, name):
            super().__init__(name)
            self.weapon_name = "Heavy Halberd"
            self.weapon_damage = 26

    # 4. Archer Branch
    class Archer(Player):

        def __init__(self, name):
            super().__init__(name)
            self.max_health = 90
            self.current_health = 90

    class LongBow(Archer):

        def __init__(self, name):
            super().__init__(name)
            self.weapon_name = "Longbow"
            self.weapon_damage = 22

    class Crossbow(Archer):

        def __init__(self, name):
            super().__init__(name)
            self.weapon_name = "Heavy Crossbow"
            self.weapon_damage = 18

    class Sniper(Archer):

        def __init__(self, name):
            super().__init__(name)
            self.weapon_name = "Precision Bow"
            self.weapon_damage = 30

    class Hunter(Archer):

        def __init__(self, name):
            super().__init__(name)
            self.weapon_name = "Hunting Bow"
            self.weapon_damage = 16


if __name__ == "__main__":
    game = Game()
    game.start_game_loop()