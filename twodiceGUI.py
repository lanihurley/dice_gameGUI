"""
Program: twodiceGUI.py
Author: Lani Hurley 11/21/2021

Simple Player vs Computer two dice game.

*** NOTE: the file "breezypythongui.py" MUST be in the same directory as the file for the application to work.***
**** NOTE: NEED IMAGE FILE: "dice.png". MUST be in the same directory as the file for the application to work.***
*** NOTE: Need to have mp3 file: "". MUST be in the same directory as the file for the application to work.***
***MUST install the pygame package by running: pip install pygame
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
from tkinter import PhotoImage
import random
import pygame

class TwoDice(EasyFrame):

	def __init__ (self):

		EasyFrame.__init__(self, title = "TWO DICE GAME", background = "#faf0de", resizable = False, width = 275, height = 430)

		# Label for the GUI tite widgets
		self.imageLabel = self.addLabel(text = "", row = 0, column = 0, columnspan = 2)
		# Load the image and associate it with the image label
		self.image = PhotoImage(file = "dice.png")
		self.imageLabel["image"] = self.image

		# create font variable
		font = Font(family = "verdana", size = 12, weight = "bold")

		# Labels and fields for the dice rolls
		self.addLabel(text = "  PLAYER", row = 1, column = 0, background = "#faf0de", sticky = "NSEW", font = font)
		self.playerRoll = self.addLabel(text = "", row = 4, column = 0, foreground = "orange", background = "white", sticky = "NSEW")
		self.addLabel(text = "Vs ", row = 2, column = 0, columnspan = 2, background = "#faf0de", sticky = "NSEW", font = font)

		# Labels and fields for the computer's roll
		self.addLabel(text = "COMPUTER", row = 1, column = 1, background = "#faf0de", sticky = "NSEW", font = font)
		self.compRoll = self.addLabel(text = "", row = 4, column = 1, sticky = "NSEW")

		# The command button
		self.addButton(text = "  Click to ROLL  ", row = 5, column = 0, columnspan = 2, command = self.playGame)

		# Label for the game final result
		self.instructions = self.addLabel(text = "ROLL the dice to see who\n has the HIGHER amount and WINS!. \nRoll the same amount and there is a TIE!", row = 3, column = 0, columnspan = 2, background = "white", foreground = "#bd4500", sticky = "NSEW")
		self.playerRoll["font"] = "times", "100"
		self.compRoll["font"] = "times", "100"


	def playGame(self):
		# adding the dice rolling sound to button
		pygame.mixer.init()
		pygame.mixer.music.load("diceroll.mp3")
		pygame.mixer.music.play(loops = 0)

		# Variables and Constants for dice
		dice = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
		playerDie = random.choice(dice)
		compDie = random.choice(dice)
		
		# Output phase of dice variable
		self.playerRoll["text"] = playerDie
		self.compRoll["text"] = compDie
		
# definition of the main()function for program entry
def main():
	"""Instantiates and pops up the window"""
	TwoDice().mainloop()

# global call to trigger the main() function
if __name__ == "__main__":
	main()