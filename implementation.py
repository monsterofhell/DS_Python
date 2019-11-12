'''A graph is an abstract mathematical construct that is used for modeling a real-world problem by 
dividing the problem into a set of connected nodes.'''
from collections import defaultdict
class Graph:
    def __init__(self,directed=False,weighted=False):
        self.directed = directed
        self.weighted = weighted
        if(weighted):
            self.vertices = defaultdict(defaultdict)
        else:
            self.vertices = defaultdict(set)
        
    def add_edge(self,src,dst,weight=None):
        if(self.weighted):
            self.vertices[src][dst] = weight
            if(not self.directed):
                self.vertices[dst][src] = weight
        else:
            self.vertices[src] =dst
            if(not self.directed):
                self.vertices[dst] = src    
    def __str__(self):
        result = ''
        if(not self.weighted):
            for i in self.vertices:
                result += str(i) + '-> ['
                for j in self.vertices[i]:
                    result += str(j) + ' '
                result += ']' +'\n'
        else:
            for i in self.vertices:
                result += str(i) + '-> ['
                for k,l in self.vertices[i].items():
                    result += str(k) + ":" + str(l) +","
                result = result[:-1]
                result += ']' +'\n'
        result = result[:-1]
        
        return result    

g1 = Graph(weighted=True)
g1.add_edge(1,2,45)
g1.add_edge(2,3,78)
g1.add_edge(2,6,98)
g1.add_edge(3,4,64)
g1.add_edge(4,2,87)
g1.add_edge(4,9,89)

print(g1)