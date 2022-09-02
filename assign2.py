import sys
from collections import defaultdict

# class represents the graph
class Graph:

    # python constructor 
    def __init__(self, vertex):
        # number of vertices
        self.V = vertex 

        # dictionary to store graph
        self.graph = defaultdict(list)

    # add edge to graph
    def addEdge(self, s, d):
        self.graph[s].append(d)

    # depth first search
    def DFS(self, d, visited_vertex, plist):

        # mark current node as visited
        visited_vertex[d]= True
        
        # append d to list
        plist.append(d)

        # recurse for all vertices adjacent to this vertex
        for i in self.graph[d]:
            if not visited_vertex[i]:
                # added plist parameter
                self.DFS(i, visited_vertex, plist)

    def fixOrder(self, d, visited_vertex, stack):

        # mark the current node as visited
        visited_vertex[d]= True

        # recurse for all the vertices adjacent to this vertex
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fixOrder(i, visited_vertex, stack)
        stack = stack.append(d)

    # function returns transpose of this graph
    def getTranspose(self):
        g = Graph(self.V)

        # recurse for all vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def numComp(self):
        
        # create stack
        stack = []

        # NEW create list pass into DFS
        plist = []

        # number of strongly connected components
        numc = 0
        
        # mark all the vertices as not visited (for 1st DFS)
        visited_vertex =[False]*(self.V)

        # fill vertices in stack according to finishing times
        for i in range(self.V):
            if not visited_vertex[i]:
                self.fixOrder(i , visited_vertex, stack)

        #create a reversed graph
        gr = self.getTranspose()

        # mark all the vertices as not visited (for 2nd DFS)
        visited_vertex =[False]*(self.V)

        # process vertices in order defined by stack
        while stack:
            j = stack.pop()
            if not visited_vertex[j]:
                gr.DFS(j, visited_vertex, plist)

                # increment number of SCC 
                numc = numc + 1
        return numc
    
    def printSCC(self):
        
        # create stack
        stack = []

        # NEW create list pass into DFS
        plist = []
        
        # mark all the vertices as not visited (for 1st DFS)
        visited_vertex =[False]*(self.V)

        # fill vertices in stack according to finishing times
        for i in range(self.V):
            if not visited_vertex[i]:
                self.fixOrder(i , visited_vertex, stack)

        #create a reversed graph
        gr = self.getTranspose()

        # mark all the vertices as not visited (for 2nd DFS)
        visited_vertex =[False]*(self.V)

        # process vertices in order defined by stack
        while stack:
            j = stack.pop()
            if not visited_vertex[j]:

                # added plist parameter
                gr.DFS(j, visited_vertex, plist)

                # sort list
                plist.sort()

                # print list
                print(*plist, sep=", ")

                # clear list
                plist.clear()


# get text file argument
infile = sys.argv[1]

# open text file for reading
txtFile = open(infile, "r")

# create an empty edgeList
edgeList = []

# iterate through file add lines to edgeList
with open(infile, "r") as filobj:
    for line in filobj:
        edgeList.append(line.rstrip().split(","))

# create empty list fo vertices
listv = []

# iterate through edgeList and add vertices
for i in range(len(edgeList)):
    num1 = edgeList[i][0]
    num2 = edgeList[i][1]
    num1 = int(num1)
    num2 = int(num2)
    listv.append(num1)
    listv.append(num2)

# create set to delete duplicate vertices
vset = set(listv)

# number of vertices is length of set 
numvertices = len(vset)

# initialize number of vertices in graph 
g = Graph(numvertices)

# iterate through edgeList and add edges
for i in range(len(edgeList)):
    num1 = edgeList[i][0]
    num2 = edgeList[i][1]
    num1 = int(num1)
    num2 = int(num2)
    g.addEdge(num1, num2)

# find the number of components
sComponents = g.numComp()

# print header
print(sComponents, "Strongly Connected Component(s):")

# print strongly connected components
g.printSCC()


    
