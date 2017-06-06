# -*- coding: utf-8 -*-

class Vertice(object):
# A Vertice is a node in a graph
    def __init__(self, index, name):
        self.index = index
        self.name = name
        self.adjacents = []

class Graph(object):
# A Graph is a set of vertice objects
    def __init__(self):
        self.vertices = []
        self.grid_data = []
        self.grid_dimensions = 0

    def read_grid(self, filename):
        with open(filename) as file:
            next(file)
            self.grid_data = [i.split() for i in file.readlines()]
        self.grid_dimensions = len(self.grid_data)

    def build_graph(self):
        for index in range(1, self.grid_dimensions+1):
            vertice = Vertice(index-1, str(index))
            self.vertices.append(vertice)

    def set_adjacence(self, source_index, target_index):
    # Sets adjacence between a source and target vertice
        self.vertices[source_index].adjacents.append(self.vertices[target_index])

    def print_graph(self):
    # Prints graph as a list of vertices and its adjacence lists
        for vertice in self.vertices:
            print('\n', vertice.name, '-> ', end='')
            if vertice.adjacents:
                for adjacent in vertice.adjacents:
                    print(adjacent.index, ' ', end='')
