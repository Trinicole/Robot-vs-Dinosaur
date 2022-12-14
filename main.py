
from unicodedata import name
from battlefield import Battlefield
import random
from robot import Robot

from weapon import Weapon
from dinosaur import Dinosaur
battlefield_1 = Battlefield()
battlefield_1.run_game()
battlefield_1.display_welcome()
battlefield_1.battle_phase()



robot = {"name": "Q", "health": 70, "attack": 10}
dinosaur = {"name": "San", "health": 50, "attack": 5}

while robot["health"]> 0 and dinosaur["health"] > 0:
    dinosaur["health"] -= robot["attack"]
    if dinosaur["health"] > 0:
        robot["health"] -= dinosaur["attack"]
    print (robot["name"],robot ["health"])
    print(dinosaur["name"], dinosaur["health"])  

battlefield_1.display_winner() 

 