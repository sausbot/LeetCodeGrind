"""
In rock paper scissors lizard Spock: 
scissors cut paper, scissors decapitates lizard,
paper covers rock, paper disproves Spock, 
rock crushes lizard, rock crushes scissors,
lizard poisons Spock, lizard eats paper, 
Spock smashes scissors, Spock vaporizes rock
"""


def return_winner(player_one, player_two):
    wins = {
        "scissors": ["paper", "lizzard"],
        "paper": ["rock", "spock"],
        "rock": ["lizzard", "scissors"],
        "lizzard": ["spock", "paper"],
        "spock": ["scissors", "rock"],
    }

    # Check for valid selections
    options = list(wins.keys())
    if player_one not in options or player_two not in options:
        return "invalid"

    # Check for tie
    if player_one == player_two:
        return "tie"

    # Check if player one wins
    defeats = wins[player_one]
    if player_two in defeats:
        return player_one

    return player_two
    # Check if player two wins
    # win_option_list_player_two = wins[player_two]
    # if player_one in win_option_list_player_two:
    #     return player_two
    # return "error"


val = return_winner("rock", "spock")
print(val)
val = return_winner("lizzard", "lizzard")
print(val)
val = return_winner("scissors", "rock")
print(val)
val = return_winner("spock", "scissors")
print(val)
