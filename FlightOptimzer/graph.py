# Graph class — directed, weighted adjacency list representing flight routes between airports.
# Loads airport/route data from data/flights.json and provides the core graph structure
# used by all algorithms in algorithms.py.
# Also provides to_undirected() conversion needed by Kruskal's MST in algorithms.py.
# Called by: main.py, experiments.py, algorithms.py (via graph instances)

import json

# Adjacency list
class AirportNetwork:
    # location is a dictionary that will store name and distance
    # it's the individual data within the slots in the list
    def __init__(self):
        self.locations = {}

    # equivalent to add vertex
    def add_location(self, name):
        if name not in self.locations:
            self.locations[name] = []
        else:
            print("Connection already exists")

    # equivalent to add edge, directed so only adds one direction
    def add_connecting_flight(self, location1, location2, distance):
        if distance < 0:
            print("Connecting flight must have a distance greater than 0")
            return

        if location1 not in self.locations:
            self.add_location(location1)
        if location2 not in self.locations:
            self.add_location(location2)

        self.locations[location1].append((location2, distance))

    def remove_connecting_flight(self, location1, location2):
        self.locations[location1] = [
            (loc, dist) for (loc, dist) in self.locations[location1]
            if loc != location2
        ]

    def neighbors(self, location):
        return self.locations[location]

    def get_weight(self, location1, location2):
        for (loc, dist) in self.locations[location1]:
            if loc == location2:
                return dist
        return None

    def vertices(self):
        return list(self.locations.keys())

    def edges(self):
        all_edges = []
        for location in self.locations:
            for (neighbor, distance) in self.locations[location]:
                all_edges.append((location, neighbor, distance))
        return all_edges

    def vertex_count(self):
        return len(self.locations)

    def edge_count(self):
        count = 0
        for location in self.locations:
            count += len(self.locations[location])
        return count

    # loads airport and route data from json file
    def from_json(path):
        graph = AirportNetwork()
        with open(path, "r") as f:
            data = json.load(f)

        for airport in data["airports"]:
            graph.add_location(airport)

        for route in data["routes"]:
            graph.add_connecting_flight(route["from"], route["to"], route["cost"])

        return graph

    # kruskal needs undirected edges, this creates a copy with both directions
    # keeps the lower weight if both directions already exist
    def to_undirected(self):
        undirected = AirportNetwork()
        for location in self.locations:
            undirected.add_location(location)

        added = {}
        for location in self.locations:
            for (neighbor, distance) in self.locations[location]:
                pair = tuple(sorted([location, neighbor]))
                if pair not in added or distance < added[pair]:
                    added[pair] = distance

        for (loc1, loc2), distance in added.items():
            undirected.locations[loc1].append((loc2, distance))
            undirected.locations[loc2].append((loc1, distance))

        return undirected