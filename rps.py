

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