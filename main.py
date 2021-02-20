from game.game import Game
import time

def example_network_generator(station_locations, feedback):
    network = {
        0: [0, 1, 2],
        1: [2, 3, 4, 2]
    }

    return network

if __name__ == '__main__':
    # Load the board file with station locations/types
    g = Game('./board/board6.yaml')
    SIM_ATTEMPTS = g.getGameConstants('SIM_ATTEMPTS')
    MAX_TRAINS = g.getGameConstants('MAX_TRAINS')

    """
    Get a dictionary that maps a location (x, y) to a tuple (stationID, shapeID),
    where (x, y) is a cartesian location of the station stationID with shape shapeID.
    """
    station_locations = g.getStationLocations()
    feedback = None

    for i in range(SIM_ATTEMPTS):
        tic = time.perf_counter() # Start a timer
        """
        Write your code here to take create a network! 
        The network should be a dictionary that maps (trainColorID)->[stationID1, 
        stationID2, stationID3...]. 
        Routes have to be path or single cycle (no "lollipops or figure 8's etc). 
        Hint: you may want to pass `station_locations` and `feedback` from the 
        previous run into your function.
        """
        network = example_network_generator(station_locations, feedback)
        
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