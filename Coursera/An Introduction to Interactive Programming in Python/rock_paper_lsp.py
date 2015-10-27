# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    
    if name == "rock": return 0
    elif name == "Spock": return 1
    elif name == "paper": return 2
    elif name == "lizard": return 3
    elif name == "scissors": return 4
    else:
        return "Your input is not correct"

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    
    if number == 0: return "rock"
    elif number == 1: return "Spock"
    elif number == 2: return "paper"
    elif number == 3: return "lizard"
    elif number == 4: return "scissors"
    else:
        return "Your input is not correct"
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    
    
    
    print " "
    print "Player chooses %s" % player_choice
    player_number = name_to_number(player_choice)
    import random
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses %s" % comp_choice
    # compute difference of comp_number and player_number modulo five
    difference = (player_number - comp_number)%5
    if difference == 0:
        print "Player and computer tie!"
        print "" 
    elif difference == 3 or difference == 4:
        print "Computer wins!"
        print ""
    else: 
        print "Player wins!"
        print ""
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
"""
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
"""

print """***Rock-paper-scissors-lizard-Spock game*** 
"""

print """Rules:
Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
Rock crushes scissors
"""
  
print """
Now try by yourself, choose one of these:
"rock", "paper", "scissors", "lizard", "Spock"
press e to exit
"""
while True:
    try:
        inp = str(raw_input("Your choice is:"))
        if inp=='e':
            break
        rpsls(inp)
        
    except:
        print "Let's try again"
        print ""
