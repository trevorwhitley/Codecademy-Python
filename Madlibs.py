"""
Name: Madlibs.py
Purpose: This program generates passages that are generated in mad-lib format
Author: Trevor
Date: 10/24/18
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %s ruled the world."

print('Mad Libs has started')

name1 = input("Enter a name: ")
name2 = input("Enter a name: ")
name3 = input("Enter a name: ")
name4 = input("Enter a name: ")
name5 = input("Enter a name: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter an adjective: ")
adjective3 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter a noun: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
superhero = input("Enter a superhero: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")

print(STORY % (name1, adjective1, adjective2, animal, food, verb, noun1, fruit, adjective3, name2, superhero, name3, country, name4, dessert, name5, year, noun2))
