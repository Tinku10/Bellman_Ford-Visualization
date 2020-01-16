from node import Node
from collections import deque

class makeEdge:
    def __init__(self, node_from, node_to):
        self.node_from = node_from
        self.node_to = node_to
        self.wt = 1

class Graph:
    def __init__(self, sx, sy, dx, dy):
        self.nodes = [[None for i in range(50)] for j in range(50)]
        self.path = [[None for i in range(50)] for j in range(50)]
        self.edges = []
        self.i = 0
        self.close = []
        self.open = []
        self.sx = sx
        self.sy = sy
        self.dx = dx
        self.dy = dy

    

    def insertEdges(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                node = arr[i][j]
                if node.wall == False:
                    if i-1 >= 0:
                        if arr[i-1][j].wall == False:
                            node.edges[0] = arr[i-1][j]
                            self.edges.append(makeEdge(node, arr[i-1][j]))
                    if i+1 <= len(arr)-1:
                        if arr[i+1][j].wall == False:
                            node.edges[1] = arr[i+1][j]
                            self.edges.append(makeEdge(node, arr[i+1][j]))
                    if j-1 >= 0:
                        if arr[i][j-1].wall == False:
                            node.edges[2] = arr[i][j-1]
                            self.edges.append(makeEdge(node, arr[i][j-1]))
                    if j+1 <= len(arr)-1:
                        if arr[i][j+1].wall == False:
                            node.edges[3] = arr[i][j+1]
                            self.edges.append(makeEdge(node, arr[i][j+1]))
                    # for diagonal movement
                    # if j-1 >= 0 and i-1 >= 0:
                    #     if arr[i-1][j-1].wall == False:
                    #         node.edges[4] = arr[i-1][j-1]
                    # if j-1 >= 0 and i+1 <= len(arr)-1:
                    #     if arr[i+1][j-1].wall == False:
                    #         node.edges[5] = arr[i+1][j-1]
                    # if j+1 <= len(arr)-1 and i-1 >= 0:
                    #     if arr[i-1][j+1].wall == False:
                    #         node.edges[6] = arr[i-1][j+1]
                    # if j+1 <= len(arr)-1 and i+1 <= len(arr)-1:
                    #     if arr[i+1][j+1].wall == False:
                    #         node.edges[7] = arr[i+1][j+1]

    def createGraph(self):
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                self.nodes[i][j]=Node(i, j)
                if random(1) < 0.2:
                    if i != self.sx and j != self.sy or i != self.dx and j != self.dy:
                        self.nodes[i][j].wall=True
        self.insertEdges(self.nodes)


    def displayGraph(self):
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):	
                if self.nodes[i][j].wall:
                    self.nodes[i][j].findColour(48, 45, 46)
                else:
                    self.nodes[i][j].findColour(255, 255, 255)


    def helperBFS(self):
        self.nodes[self.sx][self.sy].distance = 0
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                self.path[i][j]=[self.nodes[self.sx][self.sy]]
                
                
    def bellman_ford(self):
        dest=self.nodes[self.dx][self.dy]
        if self.i < 2*len(self.nodes)-1:    # V-1 times relaxing
            
            for j in range(len(self.edges)):
                if self.edges[j].node_from.distance + self.edges[j].wt < self.edges[j].node_to.distance:
                    self.edges[j].node_to.distance=self.edges[j].node_from.distance + self.edges[j].wt
                    
                    self.path[self.edges[j].node_to.i][self.edges[j].node_to.j] = [
                        self.edges[j].node_to]
                    self.path[self.edges[j].node_to.i][self.edges[j].node_to.j].extend(
                        self.path[self.edges[j].node_from.i][self.edges[j].node_from.j])
                    
                    self.close.append(self.edges[j].node_from)
                    self.open.append(self.edges[j].node_to)
            self.i += 1
        else:
            noLoop()
            return self.path[self.dx][self.dy]





    def show(self):
        for j in range(len(self.close)):
            self.close[j].findColour(173, 203, random(200, 230))
        
            self.open[j].findColour(156, random(200, 230), 87)
            
        
            # if j == 0:
            #     self.close[j].findColour(105, 105, 105)
