# -*- coding: utf-8 -*-

class Vertice(object):
    def __init__(self, index, name):
        self.index = index
        self.name = name
        self.color = 'white'
        self.adjacents = []
        self.predecessors = []
        self.count = 0

class Graph(object):
    def __init__(self, names = None):
        self.time = 0
        self.vertices = []
        if names != None:
            for index,name in enumerate(names):
                self.append_vertice(Vertice(index,name))

    def append_vertice(self, vertice):
        self.vertices.append(vertice)

    def set_adjacence(self, source_index, target_index):
        self.vertices[source_index].adjacents.append(self.vertices[target_index])

    def print_graph(self):
        for vertice in self.vertices:
            print('\n', vertice.index, ' ', vertice.color, ' ', vertice.name, '-> ', end='')
            if vertice.adjacents:
                for adjacent in vertice.adjacents:
                    print(adjacent.name, ' ', end='')

    def dfs(self):
        for vertice in self.vertices:
            if vertice.color == 'white':
                self.dfs_visit(vertice)
    
    def dfs_visit(self, vertice):
        vertice.color = 'gray'
        self.time = self.time + 1
        for adjacent in vertice.adjacents:
            v = adjacent
            if v.color == 'white':
                v.predecessors.append(vertice)
                self.dfs_visit(v)
        vertice.color = 'black'
        final_time = self.time + 1
        vertice.time = final_time
        self.time = final_time
        print('Resposta: ', final_time)

    def gen_matrix(self):
        dimension = len(self.vertices)
        matrix = [[0 for x in range(dimension)] for y in range(dimension)]
        for x in range(dimension):
            for y in range(dimension):
                matrix[x][y] = 0
                for adjacent in self.vertices[x].adjacents:
                    if adjacent.index == y:
                        matrix[x][y] = 1
        return matrix
    
    def print_matrix(self, matrix):
        dimension = len(self.vertices)
        for x in range(dimension):
            print('\n', end='')
            for y in range(dimension):
                print(matrix[x][y],' ', end='')


    

