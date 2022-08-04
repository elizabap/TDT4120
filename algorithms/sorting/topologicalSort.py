# Topological sort is a sorting algorithm that works by creating a graph of the elements in the array. Then, it traverses the graph in a topological order.
# The running time of Topological sort is O(V + E), where V is the number of vertices and E is the number of edges.
# The worst case is O(V^2).
# Easy explaination of topological sort: Topological sort is an algorithm that can be used to sort a graph in topological order.

def topologicalSort(arr):
    # create a graph
    graph = {}
    for i in range(len(arr)):
        graph[i] = []
    # add edges to the graph
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                graph[i].append(j)
    # create a list of visited nodes
    visited = []
    # create a list of sorted nodes
    sorted = []
    # traverse the graph
    for i in range(len(arr)):
        if i not in visited:
            topologicalSortHelper(i, visited, sorted, graph)
    # reverse the list
    sorted.reverse()
    return sorted

def topologicalSortHelper(i, visited, sorted, graph):
    visited.append(i)
    for j in graph[i]:
        if j not in visited:
            topologicalSortHelper(j, visited, sorted, graph)
    sorted.append(i)
  
print(topologicalSort([5, 2, 4, 6, 1, 3]))



# Python program to print topological sorting of a DAG
from collections import defaultdict

# Class to represent a graph
 
 
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):
 
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Push current vertex to stack which stores result
        stack.append(v)
 
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Print contents of the stack
        print(stack[::-1])  # return list in reverse order
 
 
# Driver Code
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
 
print ("Following is a Topological Sort of the given graph")
 
# Function Call
g.topologicalSort()
