from game.game import Game


MAX_ATTEMPTS = 4
MAX_TRAINS = 4

def example_network_generator(station_locations, feedback):
    network = {
            0: [0, 1],
            1: [1, 2, 3, 4]
    }
    return network

if __name__ == '__main__':
    # Load the board file with station locations/types
    g = Game('./board/board1.yaml')

    """
    Get a dictionary that maps a location (x, y) to a tuple (stationID, shapeID),
    where (x, y) is a cartesian location of the station stationID with shape shapeID.
    """
    station_locations = g.getStationLocations()
    feedback = None

    for i in range(MAX_ATTEMPTS):
        """
        Write your code here to take create a network! 
        The network should be a dictionary that maps (trainColorID)->[stationID1, stationID2,
        stationID3...]. 
        Routes have to be path or single cycle (no "lollipops or figure 8's etc). 
        Hint: you may want to pass `station_locations` and `feedback` from the 
        previous run into your function.
        """
        network = example_network_generator(station_locations, feedback)

        """
        Simulate commute using your network, and get back a feedback object. You can
        query the object to get helpful stats like feedback.get_avg_wait_time(). 
        """
        feedback = g.simulate(network)
        
        """
        Display an animation of the simulation. 
        """
        g.visualize()