import random

def play():
    user = input("Choose an option: 'ro' for rock, 'pa' for paper or 'sc' for scissors.\n").lower()
    computer = random.choice(['ro', 'pa', 'sc'])

    if user == computer:
        return "This is a draw!"
    
    if won_by_the_player(user, computer):
        return "You won!"
    
    return "You loose!"


def won_by_the_player(player,opponent):
    # Return True if the player wins
    # Rock beats scissors ('ro'>'sc').
    # Scissors beats paper ('sc'>'pa').
    # Paper beats rock ('pa'>'ro').
    if ((player == 'ro' and opponent == 'sc')
        or (player == 'sc' and opponent == 'pa')
        or (player == 'pa' and opponent == 'ro')):
        return True 
    else:
        return False 

print(play())