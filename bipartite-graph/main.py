# -*- coding: utf-8 -*-
from graph import *

array1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
my_graph1 = Graph(array1)

# Exemplo 1: Grafo não bipartido

my_graph1.set_adjacence(0, 1)
my_graph1.set_adjacence(1, 2)
my_graph1.set_adjacence(1, 4)
my_graph1.set_adjacence(1, 5)
my_graph1.set_adjacence(2, 3)
my_graph1.set_adjacence(2, 6)
my_graph1.set_adjacence(3, 2)
my_graph1.set_adjacence(3, 7)
my_graph1.set_adjacence(4, 0)
my_graph1.set_adjacence(4, 5)
my_graph1.set_adjacence(5, 6)
my_graph1.set_adjacence(6, 5)
my_graph1.set_adjacence(6, 7)
my_graph1.set_adjacence(7, 7)

my_graph1.print_graph()

print('\n\nGrafo Bipartido:', my_graph1.graph_two_colors())

# Exemplo 2: Grafo bipartido

array2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
my_graph2 = Graph(array2)
# a  c  f
# b e d
my_graph2.set_adjacence(0, 1)
my_graph2.set_adjacence(0, 4)
my_graph2.set_adjacence(0, 3)
my_graph2.set_adjacence(2, 1)
my_graph2.set_adjacence(2, 4)
my_graph2.set_adjacence(2, 3)
my_graph2.set_adjacence(5, 1)
my_graph2.set_adjacence(5, 4)
my_graph2.set_adjacence(5, 3)
my_graph2.set_adjacence(1, 0)
my_graph2.set_adjacence(1, 2)
my_graph2.set_adjacence(1, 5)
my_graph2.set_adjacence(4, 0)
my_graph2.set_adjacence(4, 2)
my_graph2.set_adjacence(4, 5)
my_graph2.set_adjacence(3, 0)
my_graph2.set_adjacence(3, 2)
my_graph2.set_adjacence(3, 5)

my_graph2.print_graph()

print('\n\nGrafo Bipartido:', my_graph2.graph_two_colors())

