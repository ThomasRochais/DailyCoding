from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices # Number of vertices
        self.adj = {i: [] for i in range(self.vertices)} # Adjacency list

    def addEdge(self, u, v, weight):
        self.adj[u].append((v, weight)) # Add u to v's list
        self.adj[v].append((u, weight)) # Add v to u's list, since the graph is undirected

    # Return farthest node and its distance from node u
    def BFS(self, u):
        # Marking all nodes as visited
        visited = [False for i in range(self.vertices + 1)]
        # Initialize all distances to -1
        distance = [-1 for i in range(self.vertices + 1)]
        # Distance of u from u is 0
        distance[u] = 0
        # built-in library for queue to perform fast operations on both ends
        queue = deque()
        queue.append(u)
        # mark node u as visited
        visited[u] = True
        while queue:
            # pop the front of the queue:
            front = queue.popleft()
            # loop for all adjacent nodes of node front
            for i, weight in self.adj[front]:
                if not visited[i]:
                    # mark the ith node as visited
                    visited[i] = True
                    # make distance of i, "weight" more than distance of front
                    distance[i] = distance[front] + weight
                    # push node into the stack only if it is not visited already
                    queue.append(i)
        # Get farthest node distance and its index
        maxDist = 0
        for i in range(self.vertices):
            if distance[i] > maxDist:
                maxDist = distance[i]
                nodeIdx = i
        return nodeIdx, maxDist
    
    # Prints longest path of given tree
    def LongestPathLength(self):
        # First BFS to find one end point of longest path
        node, Dist = self.BFS(0)
        # Second BFS to find the actual longest path
        node2, LongDist = self.BFS(node)
        print("Longest path is from", node, "to", node2, "of length", LongDist)

G = Graph(10)
G.addEdge(0, 1, 1)
G.addEdge(1, 2, 1)
G.addEdge(2, 3, 1)
G.addEdge(2, 9, 1)
G.addEdge(2, 4, 1)
G.addEdge(4, 5, 1)
G.addEdge(1, 6, 1)
G.addEdge(6, 7, 1)
G.addEdge(6, 8, 1)
G.LongestPathLength()

G = Graph(8)
G.addEdge(0, 1, 3)
G.addEdge(0, 2, 5)
G.addEdge(0, 3, 8)
G.addEdge(3, 4, 2)
G.addEdge(3, 5, 4)
G.addEdge(4, 6, 1)
G.addEdge(4, 7, 1)
G.LongestPathLength()