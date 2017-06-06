from graph import *

# read input
my_graph = Graph()
my_graph.read_grid('g1.in')
print(my_graph.grid_data)

my_graph.build_graph()
my_graph.print_graph()