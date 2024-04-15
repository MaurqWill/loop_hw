# 1. The Range Riddle
# Objective:
# The aim of this assignment is to deepen your understanding of Python's range() function and its application in loops. You will correct a code snippet, simulate moods for different days, and create a countdown timer.

# Task 1: Your Mood Today
# Write a program that prints off different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through the days of the week and for each day, randomly select a mood from the list and print it. Ensure that your program includes the use of the random module to select the mood.

# Example Outcome: An example output could be "On Wednesday, you were feeling happy." "On Thursday you were feeling sad."

import random
# 1. The Range Riddle
    # Task 1: Your Mood Today
moods = ["happy" , "sad", "energetic", "calm"]
days_of_the_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
for days in range(len(days_of_the_week)):
    feelings = random.choice(moods)
    print(f"on {days_of_the_week[days]}, you were feeling {feelings}" )

# Double Scoop

time_day = ["morning", "evening", "night"]
for days in range(len(days_of_the_week)):
    for time in range(len(time_day)):
        print(f"On {days_of_the_week[days]} {time_day[time]} I was feeling {random.choice(moods)}")

# Loop Condition Logic

iterations = 0
while True:
    print("can't go anywhere")
    iterations += 1
    if iterations >= 5:
        break

# random game night

gear = ['gun', 'vest', 'grenade', 'rocket']
selected = random.choice(gear)
choice = input("choose an item ")
if choice  == selected:
    print('you guessed correctly')
else:
    print("You guessed incorrectly!")

# Looping lists

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
#task1write a for loop that prints out each genre with a custom message
for genre in range(len(genres)):
    print("Track", genre + 1, " will be playin", genres[genre])

