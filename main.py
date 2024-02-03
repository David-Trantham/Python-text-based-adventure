# An example mapping of the rooms, represented as a 2d list:
room_map = [[15, 16, 17, 18, 19, 20],
            [14, 0, 0, 0, 0, 0],
            [13, 12, 11, 10, 0, 0],
            [0, 9, 8, 7, 6, 0],
            [0, 0, 3, 4, 5, 0],
            [0, 0, 2, 1, 0, 0]]
current_room = 1
current_room_location = (5,3)

#This function returns the index of the specified room within the room map.
def find_room(room_id):
    for i, x in enumerate(room_map):
        if room_id in x:
            return (i,x.index(room_id))

def check_room_at_location(room_location):
    return room_map[room_location[0]][room_location[1]]

def move(direction):
    global current_room_location
    global current_room
    new_room_location = (-1, -1)
    new_room = 0
    try:
        match direction:
            case "Forward": 
                new_room_location = (current_room_location[0]-1, current_room_location[1])
                new_room = check_room_at_location(new_room_location)
            case "Back": 
                new_room_location = (current_room_location[0]+1, current_room_location[1])
                new_room = check_room_at_location(new_room_location)
            case "Left": 
                new_room_location = (current_room_location[0], current_room_location[1]-1)
                new_room = check_room_at_location(new_room_location)
            case "Right": 
                new_room_location = (current_room_location[0], current_room_location[1]+1)
                new_room = check_room_at_location(new_room_location)
        if new_room == 0: raise ValueError
    except:
        print("Nope, can't move that way! Better try something else...\n")
        return
    else:
        current_room_location = new_room_location
        current_room = new_room
        return
    
def main():
    move("Back")
    print(current_room)
    move("Forward")
    print(current_room)
    move("Left")
    print(current_room)
    move("Right")
    print(current_room)
    # player_name = input("Please enter your name: ")

    # default_directions = ["Left", "Right", "Forward", "Back"]
    # rooms = {0: default_directions}

    # room_number = 0
    # player_input = ""

#After initializing global variables, start the program at the main function
if __name__ == '__main__':
    main()