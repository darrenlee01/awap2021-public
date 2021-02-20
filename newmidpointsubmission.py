from game.game import Game
import time
import yaml
BOARD_NAME='./board/board1.yaml'

#distance between nodes
#conjestion in each node
#number of trains
#try to distribute each shape in new routes/lines
#1000 * served_ratio - 0.02*(avg_time + std_time) - 30*num_trains`. It is possible to recieve a negative score.

def get_board_contents(board_name):
    with open(board_name, 'r') as board_file:
        board_content = yaml.load(board_file, Loader=yaml.FullLoader)
            
        return board_content['num_stations'], board_content['station_locations'], board_content['station_shapes'], board_content['station_dist_mean']

def example_network_generator(station_locations, feedback, file):
    print()
    print("----------------------------------")
    print(get_board_contents(BOARD_NAME))

    '''
    network = {
        0: [0, 1, 2],
        1: [2, 3, 4, 2]
    }

    return network'''

    (stationNum, stationLoc, stationShapes, stationDistMean) = get_board_contents(BOARD_NAME)
    
    mostCongestedIndexes = []
    maximum = -1
    for i in range(stationNum):
        if (stationDistMean[i] > maximum):
            maximum = stationDistMean[i]
            mostCongestedIndexes = [i]
        elif (stationDistMean[i] > maximum):
            mostCongestedIndexes.append(i)

    # the number of trains will be determined by the number of stations for a shape
    eachShape = {}
    for i in range(stationNum):
        if (stationShapes[i] in eachShape):
            eachShape[stationShapes[i]] += 1
        else:
            maxShapeNum = stationShapes[i]
            eachShape[stationShapes[i]] = 1
    print("shapes ", eachShape)
    maxShapeNum = -1
    for i in eachShape:
        if (eachShape[i] > maxShapeNum):
            maxShapeNum = eachShape[i]


    numTrains = maxShapeNum
    print(maxShapeNum)
    routeLength = stationNum // numTrains
    network = {}
    for i in range(numTrains):
        network[i] = mostCongestedIndexes[:]
    print(network)
    for i in range(stationNum):
        print(i)
        if (i not in mostCongestedIndexes):
            network[i % numTrains].append(i)
    
    for i in range(numTrains):
        network[i].append(mostCongestedIndexes[-1])

    print(network)
    
    #network = {
    #    0: [0, 1, 2],
    #    1: [2, 3, 4, 2]
    #}

    return network

if __name__ == '__main__':
    g = Game(BOARD_NAME)
    # Load the board file with station locations/types
    # g = Game('./board/board1.yaml')
    SIM_ATTEMPTS = g.getGameConstants('SIM_ATTEMPTS')
    MAX_TRAINS = g.getGameConstants('MAX_TRAINS')

    """
    Get a dictionary that maps a location (x, y) to a tuple (stationID, shapeID),
    where (x, y) is a cartesian location of the station stationID with shape shapeID.
    """
    station_locations = g.getStationLocations()
    feedback = None

    #for i in range(SIM_ATTEMPTS):
    for i in range(1):
        tic = time.perf_counter() # Start a timer
        """
        Write your code here to take create a network! 
        The network should be a dictionary that maps (trainColorID)->[stationID1, 
        stationID2, stationID3...]. 
        Routes have to be path or single cycle (no "lollipops or figure 8's etc). 
        Hint: you may want to pass `station_locations` and `feedback` from the 
        previous run into your function.
        """
        network = example_network_generator(station_locations, feedback, g)
        
        # Get the run time of your code
        runtime = time.perf_counter() - tic 
        if runtime > 10.0:
            raise TimeoutError("Run time for your network generator cannot exceed 10 seconds.")

        """
        Simulate commute using your network, and get back a feedback object. You 
        can query the object to get helpful stats like feedback.get_avg_wait_time(). 
        """
        feedback = g.simulate(network)
        # Print your score from this run
        feedback.print_score(runtime) 

        """
        Display an animation of the simulation. You can comment this out if you 
        want to skip the animation
        """
        g.visualize(speed=10)
