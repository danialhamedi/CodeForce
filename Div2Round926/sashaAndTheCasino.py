from functools import reduce


# Function to add an edge to the graph
def add_edge(graph, vertex1, vertex2):
    new_graph = graph.copy()
    new_graph[vertex1] = new_graph.get(vertex1, []) + [vertex2]
    new_graph[vertex2] = new_graph.get(vertex2, []) + [vertex1]
    return new_graph


# Function to get all vertices in the graph
def get_vertices(graph):
    return list(graph.keys())


# Function to get all edges in the graph
def get_edges(graph):
    return reduce(lambda acc, x: acc + [(x, y) for y in graph[x]], graph, [])


# Function to check if there is an edge between two vertices
def has_edge(graph, vertex1, vertex2):
    return vertex2 in graph.get(vertex1, [])


# Function to get all neighbors of a vertex
def get_neighbors(graph, vertex):
    return graph.get(vertex, [])


# Example graph creation and manipulation
graph = {}

graph = add_edge(graph, "A", "B")
graph = add_edge(graph, "B", "C")
graph = add_edge(graph, "C", "D")
graph = add_edge(graph, "D", "A")

print("Vertices:", get_vertices(graph))
print("Edges:", get_edges(graph))
print("Does graph contain edge between A and B?", has_edge(graph, "A", "B"))
print("Neighbors of vertex A:", get_neighbors(graph, "A"))
