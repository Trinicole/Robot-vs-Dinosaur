from unicodedata import name
from robot import Robot
from dinosaur import Dinosaur 
class Battlefield: 
    def __init__(self) :
        self.robot = Robot("Q", 70 )
        self.dinosaur = Dinosaur("San", 50, 10 )

    def run_game(self):
        print("Loading...")

    def display_welcome(self):
        print("Welcome and get ready for an exciting battle, only one will come out on top!!")

    def battle_phase(self):
        print ("Phase One Begin")


    def display_winner(self):
        print ("The winner is Q!!")


