class Character:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
        self.level = 2
        self.dungeon = 1

        #stuff about the character
class Mage(Character):
    def __init__(self, name, weapon, weapon_rarity, weapon_damage, type_of_magic):
        super().__init__(name, weapon)
        self.weapon_rarity = weapon_rarity
        self.weapon_damage = weapon_damage
        self.type_of_magic = type_of_magic
    def greeting(self):
        print("greetings fine mage")
    

mage1 = Mage("bart", "Magic orb", "Legendary", 100, "Fire")
print(f"{mage1.weapon}")