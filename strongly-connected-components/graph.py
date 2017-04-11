# -*- coding: utf-8 -*-

class Vertice(object):
    def __init__(self, index, name):
        self.index = index
        self.name = name
        self.adjacents = []
        self.color = 'white'
        self.count = 0

class Graph(object):
    def __init__(self, vertices = None):
        if vertices == None:
            self.vertices = []
        else:
            self.vertices = vertices
    
    def append_vertice(self, vertice):
        self.vertices.append(vertice)

    def set_adjacence(self, source_index, target_index):
        self.vertices[source_index].adjacents.append(self.vertices[target_index])

    def print_graph(self):
        for vertice in self.vertices:
            print('\n', vertice.index, ' ', vertice.name, '-> ', end='')
            if vertice.adjacents:
                for adjacent in vertice.adjacents:
                    print(adjacent.name, ' ',end='')
        print('\n-------------')
    

