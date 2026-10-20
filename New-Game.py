import random

def roll_weapon_rarity():
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

class Character:
    def __init__(self, name, weapon, weapon_rarity):
        self.name = name
        self.weapon = weapon
        self.level = 2
        self.dungeon = 1
        self.weapon_rarity = roll_weapon_rarity()
class Mage(Character):
    def __init__(self, name, weapon, weapon_damage, type_of_magic):
        super().__init__(name, weapon)
        self.weapon_damage = weapon_damage
        self.type_of_magic = type_of_magic
class Warrior(Character):
    def __init__(self, name, weapon, weapon_damage, sword_material):
        super().__init__(name, weapon)
        self.weapon_damage = weapon_damage
        self.sword_material = sword_material
    def greeting(self):
        print("greetings fine mage")



mage1 = Mage("bart", "Magic orb", "Legendary", 100, "Fire")
print(f"{mage1.weapon}")