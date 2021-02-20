# AWAP 2021 Starter Code

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

## Data Structures

## Feedback object

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


## Tips 
Comment out the line 
```
g.visualize()
```
to prevent the visualization window from popping up.

