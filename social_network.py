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


        
        