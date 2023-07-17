from gasp import *

begin_graphics()
finished = False

player_x = 30
player_y = 40

Circle({player_x}, {player_y}, 10, filled=True)

while True:
    key = update_when('key_pressed')
    c = Circle({player_x}, {player_y}, 10, filled=True)
    if 'w_pressed':
        player_x + 10
        player_y + 10
        move_to(c, ({player_x}, {player_y}))     

end_graphics()

def place_player():
        print("Here I am!")
def move_player():
        print("I'm moving...")

update_when('key_pressed')
end_graphics()
while not finished:
    place_player()
    move_player()