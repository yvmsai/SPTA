

class Dijkstra:
    # Initializing the values when object creation
    def __init__(self, vertices, graph):
        self.V = vertices
        self.graph = graph
    # Utility for print
    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    # function to calculate minimum distance among the vertices
    def minDistance(self, dist, sptSet):

        # Initializing minimum distance for next node
        min = 1e7
        # finding the next shortest node
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    # Function to perform Dijkstra's algorithm to calculate the shortest
    # path among the given values
    def dijkstra(self, src, dest):

        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Finding the minimum value for the nodes
            u = self.minDistance(dist, sptSet)
            # Appending the minimum distance vertex in the shortest path set
            sptSet[u] = True

            # Updating the distance of current vertex compared to
            # other vertex if it is greater
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                        sptSet[v] == False and
                        dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
                elif (self.graph[u][v] < 0 and
                        sptSet[v] == False and
                        dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
        return dist


