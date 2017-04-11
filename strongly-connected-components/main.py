# -*- coding: utf-8 -*-
from graph import *

my_graph = Graph()
names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for index,name in enumerate(names):
    my_graph.append_vertice(Vertice(index,name))

my_graph.set_adjacence(0, 1)
my_graph.set_adjacence(1, 2)
my_graph.set_adjacence(1, 4)
my_graph.set_adjacence(1, 5)
my_graph.set_adjacence(2, 3)
my_graph.set_adjacence(2, 6)
my_graph.set_adjacence(3, 2)
my_graph.set_adjacence(3, 7)
my_graph.set_adjacence(4, 0)
my_graph.set_adjacence(4, 5)
my_graph.set_adjacence(5, 6)
my_graph.set_adjacence(6, 5)
my_graph.set_adjacence(6, 7)
my_graph.set_adjacence(7, 7)
my_graph.print_graph()


