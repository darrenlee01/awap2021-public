# AWAP 2021 Starter Code

## Update!

Either clone this repo, or just download `dist\awap-2021-0.0.1.tar.gz`.

Then, run
```
pip uninstall awap-2021
pip install awap-2021-0.0.1.tar.gz   
```

Or 
```
pip uninstall awap-2021
pip install {PATH TO REPO}\dist\awap-2021-0.0.1.tar.gz   
```

## Getting Started
You will need Python 3.

From within the folder run
```
pip install -r requirements.txt
```
to install all the dependencies.

Run
```
python main.py
```
to execute the game

### Modifying the code
Everything you need should be in `main.py`.  
Change the line `network = example_network_generator(station_locations, feedback)` to take in your network generating function.  
Load different maps by changing `g = Game('./board/board1.yaml')` to a different board yaml.

## Data Structures
All IDs used in the game are ints. Each station is given a unique **stationID**.
Each "shape" (for passengers and stations) is represented by a **shapeID**.
Each "color" for train lines is represented by a **colorID**.

### station_locations
`station_locations`: A dictionary that maps a location (x, y) to a tuple (stationID, shapeID), where (x, y) is a cartesian location of the station stationID with shape shapeID.  

Example:
```
{(5, 12) : (0, 1),
(3, 4) : (1, 0),
(10, 10): (2, 2),
(-5, 6): (3, 1)}
```
The first item represents a station located at (5, 12) with stationID = 0 and shapeID = 1.

### network
`network`:  a dictionary that maps trainColorID to a list [stationID1, stationID2, stationID3...].
Routes have to be path or single cycle (no "lollipops or figure 8's etc).  Cycles must start and end on the same station.

Example:
```
{0: [0, 1, 2, 0],
1:[2, 3, 4],
2:[4, 5] }
```
The first item represents train 0 with a route that passes through stations 0->1->2->0.


## Feedback object
The Feedback object is returned by simulate() and can be queried to get metrics
on the last run.  

All `get_...` functions do not require any arguments.  

The following metrics can be quered by calling `feedback.get_avg_{METRIC NAME}()`, 
`feedback.get_std_{METRIC NAME}()`, `feedback.get_min_{METRIC NAME}()`, 
`feedback.get_max_{METRIC NAME}()`.   
For example `feedback.get_avg_wait_time()` or `feedback.get_max_travel_distance()`.

```
'wait_time': Time from passenger spawn to boarding the train
'travel_time': Time spent traveling from source to destination
'total_time': wait_time + travel_time
'num_intermediate_stations': Number of stations passenger goes 
through before reaching destination (non-inclusive of start and stop station)
'travel_distance': Distance passenger travels as it traverses from
start to stop station along train route, i.e., a sum of the lengths
of each segment between stations along the passenger's route.
'displacement': Euclidean distance between start and end stations 
```

The following functions return aggregate data.
`get_passenger_spawns`: Returns a list, sorted by time of passenger spawn tuples with elements (timestamp, shapeID, spawn stationID).
Includes all passengers that are spawned.  
`get_passenger_arrivals`: Returns a list, sorted by time of passenger spawn tuples with elements (timestamp, shapeID, arrival stationID).
Includes all passengers that are spawned.  
`get_passenger_log`: Returns a dataframe where each row is an entry for a passenger, 
and the columns are as listed below. NOTE: only includes passengers that reach their 
final destinations; if a passenger is spawned but never reaches its destination, it is not logged.  
```
'wait_time': Time from passenger spawn to boarding the train
'travel_time': Time spent traveling from source to destination
'total_time': wait_time + travel_time
'num_intermediate_stations': Number of stations passenger goes 
through before reaching destination (non-inclusive of start and stop station)
'travel_distance': Distance passenger travels as it traverses from
start to stop station along train route, i.e., a sum of the lengths
of each segment between stations along the passenger's route.
'displacement': Euclidean distance between start and end stations 
'spawn_time': Tiemstamp when passenger spawned
'arrival_time': Timestamp when passenger arrived at destination
'contains_transfer': Boolean if route contained transfer or not
```

You can display a plot of passenger count over time.  
`plot_passenger_count`: Plots time unit vs passenger count, where passenger count refers to the number of passengers
in the system, i.e., passengers that have spawned and are waiting for a train or are in transit.
Once passengers reach their final destination, they are no longer in the system.
Returns list of passenger counts, where count[i] is the number of passenger counts at the ith time unit. 

Print the score for a run using `print_score(runtime)`. This will also return the score. 

### Scoring
The score is calculated based on the ratio of passengers served, average and standard deviation passenger time and number of trains used in the network
- Greater ratio of passengers served topassengers spawned => Higher Score
- Lower average passenger time (wait time + travel time) => Higher Score
- Lower standard deviation passenger time (wait time + travel time) => Higher Score
- Less trains used in the network => Higher Score

The formula used is `1000 * served_ratio - 0.02*(avg_time + std_time) - 30*num_trains`. It is possible to recieve a negative score.

## Tips 
Comment out the line 
```
g.visualize()
```
to prevent the visualization window from popping up.

You can speed up the visualization by increasing the argument `speed` to `g.visualize`.

Use feedback from the previous run to improve your network for the next run. You get 5 attempts and only the last run is kept for scoring.

## Constants
A few constants (you don’t need to worry about these, but they may be useful for algorithm)
```
SIM_ATTEMPTS = 5
MAX_TRAINS = 6
NUM_SHAPES = 8
TRAIN_SPEED = 5
TRAIN_CAPACITY = 30
SPAWN_DURATION = 5000
SIM_DURATION = 10000
These can be accessed via g.getGameConstants
```

### Access the board file from your code

**In `main.py`:**
1. At the top of the file, create variable `BOARD_NAME='./board/board1.yaml'`
2. replace the first line after `if __name__ == '__main__':`
with
```
g = Game(BOARD_NAME)
```
3. In your code, you can write a function like this. 
```
def get_board_contents(board_name):
    with open(board_name, 'r') as board_file:
        board_content = yaml.load(board_file, Loader=yaml.FullLoader)
            
        return 
        board_content['num_stations'],
        board_content['station_locations'],
        board_content['station_shapes'],
        board_content['station_dist_mean']
```
Pass in your `BOARD_NAME` variable to this function.

**In `scoring.py`:**
Replace the line
```
g = Game('./board/board{}.yaml'.format(board_num+1))
```
with
```
BOARD_NAME = './board/board{}.yaml'.format(board_num+1)
g = Game(BOARD_NAME)
```
Similarly, pass in `BOARD_NAME` to your function that reads the board file.