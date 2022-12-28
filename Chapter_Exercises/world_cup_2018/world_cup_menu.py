from world_cup_tools import *
def menu():
    print("*********************************************")
    print("*                                           *")
    print("*      2018 World Cup: Goals Analysis       *")
    print("*                                           *")
    print("*********************************************")
    print("")
    print("> Select an option:")
    print("       > A: Total number of goals scored by a given country")
    print("       > B: Total number of goals scored by a given player")
    print("       > C: List the name of all the players who scored for a given country")
    print("       > D: Total number of goals by all countries")
    print("       > E: Total number of goals scored during the first half (45 minutes)")
    print("       > F: Total number of goals scored during the second half (45 minutes to 90 minutes)")
    print("       > G: Total number of goals scored during extra time (after 90 minutes of play)")
    print("       > H: Total number of goals scored per country")
    print("       > I: Top goal scoring country")
    print("       > J: Top goal scorer")
    print("       > X: Exit")
    print("")
    userchoice = input("Select an option: ")
    while userchoice != 'X':      
        if userchoice == 'A':
            country = input("Input a country: ")
            return goal_by_country(country)
        elif userchoice == 'B':
            player = input("Input a player: ")
            return goal_by_player(player)
        elif userchoice == 'C':
            country = input("Input a country: ")
            return player_country(country)
        elif userchoice == 'D':
            return total_goal()
        elif userchoice == 'E':
            return half_goal('first')
        elif userchoice == 'F':
            return half_goal('second')
        elif userchoice == 'G':
            return half_goal('addition')
        elif userchoice == 'H':
            return goal_dict()
        elif userchoice == 'I':
            return most_goal_country()
        elif userchoice == 'J':
            return golden_boot()
        else:
            print("Select a valid option")
            print("Thanks for playing")
            print("Quitting...")
            print("Finished")
            return None
          