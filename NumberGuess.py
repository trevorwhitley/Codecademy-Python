"""
Name: NumberGuess.py
Purpose: Computer rolls dice and user guesses the value.
Author: Trevor Whitley
Date: 10/26/28
"""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(input("Guess a number: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print("The maximum value is %d" % max_val)
  guess = get_user_guess()
  
  if guess > max_val:
    print("Invalid Guess.")
  else:
    print("Rolling...")
    sleep(2)
    print("The first roll is %d" % first_roll)
    sleep(1)
    print("The second roll is %d" % second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print("The total roll is %d" % total_roll)
    print("Result...")
    sleep(1)
    if guess == total_roll:
      print("You won!")
    else:
      print("You lost.")
    
sides = int(input("Enter number of sides for the die: "))
roll_dice(sides)
