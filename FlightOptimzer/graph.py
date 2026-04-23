# Graph class — directed, weighted adjacency list representing flight routes between airports.
# Loads airport/route data from data/flights.json and provides the core graph structure
# used by all algorithms in algorithms.py.
# Also provides to_undirected() conversion needed by Kruskal's MST in algorithms.py.
# Called by: main.py, experiments.py, algorithms.py (via graph instances)

# Adjacency list
class AirportNetwork:
    # location is a dictionary that will store name and distance.
    # it's the individual data within the slots in the list
    def __init__(self):
        self.locations = {}

    # equivalent to add vertex
    def add_location(self, name):
        if name not in self.locations:
            self.locations[name] = []
        else: 
            print("Connection already exists")
    
    # equivalent to add edge
    def add_connecting_flight(self, location1, location2, distance):
        self.locations[location1].append((location2, distance))
        self.locations[location2].append((location1, distance))