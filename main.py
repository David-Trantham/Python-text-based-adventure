# An example mapping of the rooms, represented as a 2d list:
current_room = 1
room_map = [[15, 16, 17, 18, 19, 20],
            [14, 0, 0, 0, 0, 0],
            [13, 12, 11, 10, 0, 0],
            [0, 9, 8, 7, 6, 0],
            [0, 0, 3, 4, 5, 0],
            [0, 0, 2, 1, 0, 0]]

#This function returns the index of the specified room within the room map.
def find_room(room_id):
    for i, x in enumerate(room_map):
        if room_id in x:
            return (i,x.index(room_id))

def move(direction):
    try:
        room_location = find_room(current_room)
        print(room_location(1))
    except:
        print("wow")

def main():
    print(find_room(1))
    print(room_map[5][3])
    player_name = input("Please enter your name: ")

    default_directions = ["Left", "Right", "Forward", "Back"]
    rooms = {0: default_directions}

    room_number = 0
    player_input = ""

#After initializing global variables, start the program at the main function
if __name__ == '__main__':
    main()