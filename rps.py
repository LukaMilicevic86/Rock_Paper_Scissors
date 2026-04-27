

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
import random
import os

Builder.load_file('rps.kv')

#create class for the game window with all score variables set to zero at the beginning
class TheGame(FloatLayout):
    game_counter = 0
    your_points = 0
    opponent_points = 0

    #function for random selection of opponent's picture that's to be called when we click on ours
    def random_selection(self):
        number = random.randint(1,3)

        #randomly chosen path of pictures from the game folder are put into the "path" variable to be used later in comparison with the path of our picture
        if number == 1:
            self.path = "rps/stone.png"
        if number == 2:
            self.path = "rps/paper.png"
        if number == 3:
            self.path = "rps/scissors.png"    

        #the oponent selection picture in the kivy file gets that image
        self.ids.opponent_selection.background_normal = self.path

    #rock function that calls the random generator, calls the battle function and uses the stone picture as parameter
    def rock(self):
        self.random_selection()
        self.ids.your_selection.background_normal = "rps\stone.png"
        self.battle(self.ids.your_selection.background_normal, self.path)

    #paper function that calls the random generator, calls the battle function and uses the paper picture as parameter
    def paper(self):
        self.random_selection()
        self.ids.your_selection.background_normal = "rps\paper.png"
        self.battle(self.ids.your_selection.background_normal, self.path)
    
    #scissors function that calls the random generator, calls the battle function and uses the scissors picture as parameter
    def scissors(self):
        self.random_selection()
        self.ids.your_selection.background_normal = "rps\scussirs.png"
        self.battle(self.ids.your_selection.background_normal, self.path)

    #battle function that uses if statements that compare the picture names from the arguments to determine the outcome, keep score and update the UI
    def battle(self, your_selection, opponent_selection):
    
    #Outcomes when player's choice is Rock
        if os.path.basename(your_selection) == "stone.png" and os.path.basename(opponent_selection) == "stone.png":
            self.ids.instructions.text = "Draw"

        if os.path.basename(your_selection) == "stone.png" and os.path.basename(opponent_selection) == "scissors.png":
            self.ids.instructions.text = "You win"
            self.your_points += 1
            self.ids.label_your_points.text = str(self.your_points)

        if os.path.basename(your_selection) == "stone.png" and os.path.basename(opponent_selection) == "paper.png":
            self.ids.instructions.text = "You lose"
            self.opponent_points += 1
            self.ids.label_opponent_points.text = str(self.opponent_points)
        
    #Outcomes when player's choice is Paper
        if os.path.basename(your_selection) == "paper.png" and os.path.basename(opponent_selection) == "paper.png":
            self.ids.instructions.text = "Draw"

        if os.path.basename(your_selection) == "paper.png" and os.path.basename(opponent_selection) == "stone.png":
            self.ids.instructions.text = "You win"
            self.your_points += 1
            self.ids.label_your_points.text = str(self.your_points)

        if os.path.basename(your_selection) == "paper.png" and os.path.basename(opponent_selection) == "scissors.png":
            self.ids.instructions.text = "You lose"
            self.opponent_points += 1
            self.ids.label_opponent_points.text = str(self.opponent_points)

    #Outcomes when player's choice is Scissors
        if os.path.basename(your_selection) == "scissors.png" and os.path.basename(opponent_selection) == "scissors.png":
            self.ids.instructions.text = "Draw"

        if os.path.basename(your_selection) == "scissors.png" and os.path.basename(opponent_selection) == "paper.png":
            self.ids.instructions.text = "You win"
            self.your_points += 1
            self.ids.label_your_points.text = str(self.your_points)

        if os.path.basename(your_selection) == "scissors.png" and os.path.basename(opponent_selection) == "stone.png":
            self.ids.instructions.text = "You lose"
            self.opponent_points += 1
            self.ids.label_opponent_points.text = str(self.opponent_points)
            



