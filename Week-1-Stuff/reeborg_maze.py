#This code involves while and if loops to control a robot through a maze.
# URL - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#Below is the code I created to get the robot through the maze. Test it for yourself !

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while at_goal() == False:
    if front_is_clear():
        move()
        if right_is_clear():
            turn_right()
    elif wall_on_right():
        turn_left()
    elif wall_in_front():
        turn_left()
    elif turn_right() == False:
        turn_left()
