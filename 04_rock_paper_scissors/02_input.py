import random

robot_choice = random.choice(['Rock', 'Paper', 'Scissors'])
user_input = input('Rock, Paper, Scissors, Go! : ')
rock_paper_scissors = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
user_choice = rock_paper_scissors[user_input.strip()[0].upper()]
print('I am ' + robot_choice)
print('You are ' + user_choice)
