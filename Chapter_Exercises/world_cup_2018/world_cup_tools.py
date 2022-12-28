def load_goal_list():
    obj = open('goals.txt','r')
    info = []
    for line in obj:
        my_list = line.split(';')
        my_list.pop(-1)
        info.append(my_list)
    obj.close()
    return info

def all_country():
    '''
Returning all countries in the worldcup
as a list
'''
    world_cup = load_goal_list()
    country = []
    for value in world_cup:
        if value[1] not in country:
            country.append(value[1].lower())
    return country

def goal_by_country(country):
    '''(str)->int
returns the goal scored by a given
country. If country doesn't exist,
raise ValueError.
'''
    counter = 0
    country_list = all_country()
    world_cup = load_goal_list()
    if country.lower() not in country_list:
        raise ValueError("This country is not in the world cup, try another one")
    for value in world_cup:
        if value[1].lower() == country.lower():
            counter += 1
    return counter

def goal_by_player(player):
    '''
(str)->int
returns the goal scored by a given
player. If player doesn't exist,
raise ValueError.
'''
    counter = 0
    world_cup = load_goal_list()
    for value in world_cup:
        if value[0] == player:
            counter += 1
    return counter

def player_country(country):
    '''(str)->list
returns the players scoring for
a given country. If country doesn't
exist, raise ValueError.
'''
    player_list = []
    country_list = all_country()
    world_cup = load_goal_list()
    if country.lower() not in country_list:
        raise ValueError("This country is not in the world cup, try another one")
    for value in world_cup:
        if value[1].lower() == country.lower():
            if value[0] not in player_list:
                player_list.append(value[0])
    return player_list

def total_goal():
    '''
returns total goal scored by
all countries
'''
    world_cup = load_goal_list()
    return len(world_cup)

def half_goal(half):
    ''' (str)->int
Goal scored in the first half,second,
additional according to the user input
'''
    counter_first = 0
    counter_second = 0
    counter_addition = 0
    world_cup = load_goal_list()
    for value in world_cup:
        if int(value[2]) <= 45:
            counter_first += 1
        elif int(value[2]) <= 90:
            counter_second += 1
        else:
            counter_addition += 1
    if half == 'first':
        return counter_first
    elif half == 'second':
        return counter_second
    elif half == 'addition':
        return counter_addition

def goal_dict():
    '''
Goal scored by each country
'''
    world_cup = load_goal_list()
    goal_dict = dict.fromkeys(all_country(),0)
    for key in goal_dict:
        goal_dict[key] = goal_by_country(key)
    return goal_dict

def most_goal_country():
    '''
Returning which country scored the most goals
'''
    goal_d = goal_dict()
    max_goal = max(goal_d.values())
    for key in goal_d:
        if goal_d[key] == max_goal:
            return key
        
def golden_boot():
    '''
Returning the player name who won the golden boot
'''
    world_cup = load_goal_list()
    player_list = []
    for value in world_cup:
        if value[0] not in player_list:
            player_list.append(value[0])
    player_dict = dict.fromkeys(player_list,0)
    for key in player_dict:
        player_dict[key] = goal_by_player(key)
    player_dict.pop('OG')
    for key in player_dict:
        if player_dict[key] == max(list(player_dict.values())):
            return key