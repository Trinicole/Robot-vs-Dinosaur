
import random
from dinosaur import Dinosaur
from weapon import Weapon
class Robot:
    def __init__(self, name, health):
        self.name = "Q"
        self.health = 70 
        self.active_weapon =""
        self.weapons_list = []
        self.creating_attacks()

    def creating_attacks(self):
        weapon1 = Weapon("Bow and Arrow", 15)
        weapon2 = Weapon("Knife", 20)
        weapon3 = Weapon("Hammer", 10)
        self.weapons_list.extend([weapon1, weapon2, weapon3])
    def attack(self, dinosaur):
        self.active_weapon = random.choice(self.weapons_list)
        dinosaur.health -= self.active_weapon.attack_power

