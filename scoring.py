from game.game import Game
import time

def example_network_generator(station_locations, feedback):
    network = {
        0: [0, 1, 2],
        1: [2, 3, 4, 2]
    }

    return network

if __name__ == '__main__':
    for board_num in range(8):
        BOARD_NAME = './board/board{}.yaml'.format(board_num+1)
        g = Game(BOARD_NAME)
        SIM_ATTEMPTS = g.getGameConstants('SIM_ATTEMPTS')

        station_locations = g.getStationLocations()
        feedback = None

        for i in range(SIM_ATTEMPTS):
            tic = time.perf_counter()
            
            """
            Call your network generator function here!
            """
            network = example_network_generator(station_locations, feedback)
            
            runtime = time.perf_counter() - tic 
            if runtime > 10.0:
                raise TimeoutError("Run time for your network generator cannot exceed 10 seconds.")

            feedback = g.simulate(network)
        feedback.print_score(runtime, only_numbers=True)
