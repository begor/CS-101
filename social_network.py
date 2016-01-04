"""
Builds a simple data structure to hold all the connections passed as a string

Example input:
 "John is connected to Bryant, Debra, Walter.\
  John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\"

Example output:
 {'John': { 
		'connections': ['Bryant', 'Debra', 'Walter'], 
		'games': ['The Movie: The Game', 'The Legend of Corgi', 'Dinosaur Diner'] }
"""
def create_data_structure(connections_string):
    network = {}
    
    #Find first person's likes and connections sentences
    connections_sentence_end = connections_string.find(".")
    likes_sentence_end = connections_string.find(".", connections_sentence_end + 1)
    
    #While loop until there is no more people in our network
    while (connections_sentence_end != -1):
        person_connections = connections_string[:connections_sentence_end]
        person_likes = connections_string[connections_sentence_end+1:likes_sentence_end]
        
        #All of the work on parsing person's info is in this procedure
        name, person_info = get_person_info(person_connections, person_likes)
        network[name] = person_info
        
        #Now we remove parsed person from connections_string
        #And find next person to proceed
        connections_string = connections_string[likes_sentence_end + 1:]
        connections_sentence_end = connections_string.find(".")
        likes_sentence_end = connections_string.find(".", connections_sentence_end + 1)

    #Finally we return our data structure
    return network

"""
Procedure that parses given Connections and Games string
and returns person's name and info.
Given strings should be in following format:
	Connections: "John is connected to Bryant, Debra, Walter"
	Games: "John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner"
"""
def get_person_info(connections, games):
	name = connections[:connections.find(" ")]

	#Find people that connected to given person
	connected_position = connections.find('to ')
	connections = connections[connected_position + len('to') + 1:].split(', ')

	#Find games that given person likes
	games_position = games.find('play')
	games = games[games_position + len('play') + 1:].split(', ')

	info = {'connections': connections, 'games': games}
	
    return name, info

# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.
def get_connections(network, user):
    return network[user]['connections']

# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network,user):
    return network[user]['games']

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False

    if user_B in network[user_A]['connections']:
        return network

    network[user_A]['connections'].append(user_B)

    return network


# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#            ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def get_secondary_connections(network, user):
    if user not in network:
        return None

    secondary_connections = []

    for connection in network[user]['connections']:
        secondary = network[connection]['connections']
        if secondary not in secondary_connections:
            secondary_connections += secondary

    return secondary_connections


# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
    if user not in network:
        return None

    secondary_connections = []

    for connection in network[user]['connections']:
        secondary_connections += connection['Connections']

    return secondary_connections
    
        
        