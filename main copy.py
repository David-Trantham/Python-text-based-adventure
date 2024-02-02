player_name = input("Please enter your name: ")

default_directions = ["Left", "Right", "Forward", "Back"]
rooms = {0: default_directions}

room_number = 0
player_input = ""

if room_number == 0:
    print("Welcome to the game!")
    player_input = input("Do you want to go left or right? (L/R)")

if player_input.upper() == "R":
    room_number = 1
elif player_input.upper == "L":
    room_number = 2