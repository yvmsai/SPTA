# importing the needed libraries and algorithms
from functools import reduce
import matplotlib.pyplot as plt
import time
import numpy
from BellmanFord_Algorithm import BellmanFord
from Dijikstra_Algorithm import Dijkstra


# Function to read the data from input file
def read_data(input_file, n_size):
    with open(input_file, 'r') as file_object:
        file_data = file_object.readlines()
        file_content = file_data[0:n_size]
        # calculating the vertexes from the readed file
        vertexes = [row_node_data.strip().split() for row_node_data in file_content]
        # calculating the weights
        edge_weights_list = [list(map(int, vertex)) for vertex in vertexes]
        weights = []
        for vertex in vertexes:
            weights.append(int(vertex[2]))
        edges = [tuple(map(int, vertex[0:2])) for vertex in vertexes]
        # returning the edges and their weights
        return edges, weights, edge_weights_list


def getEdgeWeightsList(edges, weights):
    edges_list = []
    for edge in edges:
        edges_list.append(list(edge))
    for weight in range(len(weights)):
        edges_list[weight].append(weights[weight])
    return edges_list


# finding the adjacency Matrix based on the edges as a graph
def getMatrix(edges, weights):
    edges = edges
    weights = weights
    nodes = reduce(lambda x, y: x.union(y), edges, set())
    m = len(edges)
    n = len(nodes)
    graph = numpy.zeros((n, n))
    for i, (x, y) in enumerate(edges):
        graph[x, y] = int(weights[i])
        graph[y, x] = int(weights[i])
    return graph


def algorithmTrigger(filename):
    # Initializing the variables to plot the graph
    x_nodes = []
    y_dij = []
    y_bellman = []
    size = 10
    source = 0
    destination = 10
    # loop to iterate over the chucks of dataset to calculate
    # the performance of each algorithms
    for val in range(0, 8):
        edges, weights, edges_weights = read_data(filename, size)
        nodes = len(reduce(lambda x, y: x.union(y), edges, set()))
        size = size * 3
        x_nodes.append(nodes)
        graph = getMatrix(edges, weights)
        g = Dijkstra(nodes, graph)
        print("Dijkstra Algorithm")
        print("Number of nodes :", nodes)
        print("Number of edges", len(edges))
        tot_dij = 0.0
        distance = []
        for i in range(10):
            # Object Initialization for Dijkstra Algorithm class
            start_time = time.time_ns() / 1000
            # Trigger the dijkstra algorithm
            distance = g.dijkstra(source, destination)
            end_time = time.time_ns() / 1000
            duration = (end_time - start_time)/25
            tot_dij = tot_dij + duration
        print("Distance from Source: {} to destination : {} is {}".format(source, destination, distance[destination]))
        avg_time_dij = tot_dij/10
        print("Time taken for Dijkstra Algorithm is ", avg_time_dij, "seconds")
        y_dij.append(avg_time_dij)

        # Object Creation for Bellman_ford Algorithm
        g = BellmanFord(nodes, edges_weights)
        print("BellmanFord")
        print("Number of nodes :", nodes)
        print("Number of edges", len(edges))
        tot_bellman = 0.0
        distance_b = []
        for j in range(10):
            start_time = time.time_ns() / 1000
            # Triggering Bellman_ford Algorithm
            distance_b = g.BellmanFord(0, 10)
            end_time = time.time_ns() / 1000
            duration_b = (end_time - start_time)/2
            tot_bellman = tot_bellman + duration_b
        print("Distance from Source: {} to destination : {} is {}".format(source, destination, distance_b[destination]))
        avg_time_bellman = tot_bellman/10
        print("Time take for Bellman-ford Algorithm is ", avg_time_bellman, "seconds")
        y_bellman.append(avg_time_bellman)
    return x_nodes, y_dij, y_bellman


def calculateTime():
    x_nodes = []
    y_dij = []
    y_bellman = []
    neg_y_dij = []
    neg_y_bellman = []
    for val in range(2):
        if val == 0:
            x_nodes, y_dij, y_bellman = algorithmTrigger("Updated_Input.csv")
        elif val == 1:
            x_nodes, neg_y_dij, neg_y_bellman = algorithmTrigger("Updated_Negative_Input.csv")

    # Plotting the graph for Dijkstra and Bellman- ford Algorithms
    plt.plot(x_nodes, y_dij, label="Dijkstra")
    plt.plot(x_nodes, y_bellman, label="Bellman")
    # naming the x-axis
    plt.xlabel('Number of Nodes')
    # naming the y-axis
    plt.ylabel('Execution Time (seconds)')

    # giving a title to the graph
    plt.title('Graph to compare the execution times of Algorithms[Positive Weights]')

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()

    # Plotting the graph for Dijkstra and Bellman- ford Algorithms
    plt.plot(x_nodes, neg_y_dij, label="Dijkstra")
    plt.plot(x_nodes, neg_y_bellman, label="Bellman")
    # naming the x-axis
    plt.xlabel('Number of Nodes')
    # naming the y-axis
    plt.ylabel('Execution Time (seconds)')

    # giving a title to the graph
    plt.title('Graph to compare the execution times of Algorithms[Negative Weights]')

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()


#Driver trigger

calculateTime()