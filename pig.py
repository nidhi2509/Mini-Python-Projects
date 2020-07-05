"""
Make sure to fill in the following information before submitting your
assignment. Your grade may be affected if you leave it blank!
For usernames, make sure to use your Whitman usernames (i.e. exleyas). 
File name: pig.py
Author username(s): harristr jaltarnr
Date: October 9, 2017

As part of the "Finishing Touches for this asignment, we have implemented:
    - Accept a broader range of inputs beyond "y" and "n"
    - Ask the players for their names, and use them when announcing whose turn it is.
"""

import random

def roll_die(sides):
    """
    Generates a die roll result from the possible values on the n-sided die.
    
    Parameters: sides: Specifies the number of sides on the die being used.
    
    Returns: The value of the die roll.
    """
    return(random.randint(1, sides))    #Calls a random integer in range of permissible values


def take_turn():
    """
    Calculates the total number of points that a player acquires on their turn based on their choices.
    
    Parameters: None
    
    Returns: The number of turn points acquired by a player during the turn.
    """
    turnpoints = 0  #Initializes points gained by the player on this turn
    keeproll = True #Initializes the player's choice to continue rolling this turn
    
    while keeproll == True:    #Checks that player has chosen and is permitted to keep rolling
        print()
        roll = roll_die(6)  #Gets roll value
        
        if roll == 1:
            print("You rolled a 1 and got no points this turn.")
            return(0)
        
        else:
            turnpoints = turnpoints + roll  #Adds roll value to gained points
            print("You rolled a " + str(roll) + ".")
            print("This turn, you have gained " + str(turnpoints) + " points.")
            query = ''  #Initializes their response to empty string
            while query != 'y' and query != 'n' and query != 'yes' and query != 'no':    #Checks if response is yes or no and only quits looping when yes or no is received
                print()
                initquery = input("Do you want to continue playing?  ")   #Asks the player to answer yes or no to continuing to play.
                query = initquery.lower()   #Changes player's input to lower-case for ease of conditional checking.
                if query == 'y' or query == 'yes':    #Lets player keep rolling
                    keeproll = True
                else:
                    keeproll = False
                    
    print()
    print("Your turn is ending. You have gained " + str(turnpoints) + " points.")   #Prints points gained in the turn.
    return(turnpoints)


def show_instructions():
    """
    Prints game instructions.
    
    Parameters: None
    
    Returns: None
    """
    print("\n\
    Welcome to the Game of Pig. To win, be the\n\
    player with the most points at the end of the\n\
    game. The game ends at the end of a round where\n\
    at least one player has 100 or more points.\n\
    \n\
    On each turn, you may roll the die as many times\n\
    as you like to obtain more points. However, if\n\
    you roll a 1, your turn is over, and you do not\n\
    obtain any points that turn.\n\
    ")


def play_game():
    """
    Plays the game of pig with 2 players.
    
    Parameters: None
    
    Returns: None
    """
    player_1 = 0    #Initializes player 1's total points to 0.
    player_2 = 0    #Initializes player 2's total points to 0.
    
    p1 = str(input("Enter your name, Player 1:  "))
    p2 = str(input("Enter your name, Player 2:  "))
    
    while player_1 < 100 and player_2 < 100:    #Checks that neither player has exceeded game-ending score limit.
        print()
        print("Points Summary:   " + p1 + " has " + str(player_1) + " points and " + p2 + " has " + str(player_2) + " points.") #Prints points summary
        
        print()
        print("---------------------------------------------------------------")
        print()
        input("It's " + p1 + "'s turn to play. Press enter when ready to play.")
        player_1 = player_1 + take_turn()   #Adds points gained in a turn to player 1's total points.
        
        print()
        print("Points Summary:   " + p1 + " has " + str(player_1) + " points and " + p2 + " has " + str(player_2) + " points.") #Prints points summary
        
        print()
        print("---------------------------------------------------------------")
        print()
        input("It's " + p2 + "'s turn to play. Press enter when ready to play.")
        player_2 = player_2 + take_turn()   #Adds points gained in a turn to player 2's total points. 
    
    print()
    print("Points Summary:   " + p1 + " has " + str(player_1) + " points and " + p2 + " has " + str(player_2) + " points.") #Prints points summary
    
    if player_1 > player_2:
        print()
        print(p1 + " wins the game!")
    elif player_2 > player_1:
        print()
        print(p2 + " wins the game!")
    else:
        print()
        print("The game is a tie.")
        
    
def main():
    show_instructions()
    play_game()
    

main()

def test():
    for i in range(20):
        print(roll_die(10))
    
    print()

    points = take_turn()
    print("Returned points:", points)
