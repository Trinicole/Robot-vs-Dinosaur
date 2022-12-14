class Dinosaur : 



    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = 50
        self.attack_power = attack_power
    def attack(self, robot):
        self.health = robot.health 
        robot.health -= self.active_weapon.attack_power


