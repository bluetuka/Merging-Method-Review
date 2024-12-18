class FlowNetwork :
 
    def __init__(self) : 
        self.adj ={}

    #initialize, add nodes, edges, Time O(1), Space O(1)
    def addEdge(self, u, v, w):
        if (self.adj.get(u) is None) :		
             self.adj[u] = {}  #add node
        if(self.adj.get(v) is None):
            self.adj[v] = {}
        edge = self.adj.get(u)
        edge[v] = w
        self.adj[u] = edge


    #Time O(V2), Space O(E) 
    def fillEmptyEdge(self) :
        for  t in self.adj.keys() :
            map= self.adj[t]
            for t1 in self.adj.keys():
                if t1 not in map:
                    map[t1]= 0				
                				
    #Time O(EV), Space O(E+V)
    def cloneGraph(self) :
        clone = {}
        for t in self.adj.keys():
            clone[t] = {}
            edges1 = clone[t]
            edges = self.adj[t]
            for k,v in edges.items(): 
                edges1[k] = v
            clone[t] = edges1	 
        return clone
    
if __name__ == "__main__":
    g= FlowNetwork()
    g.addEdge(0, 1, 16)
    g.addEdge(0, 2, 13)	    
    g.addEdge(1, 2, 10) 
    g.addEdge(2, 1, 4) 	    
    g.addEdge(1, 3, 12) 
    g.addEdge(3, 2, 9) 
    g.addEdge(2, 4, 14) 
    g.addEdge(4, 3, 7) 	    
    g.addEdge(3,5, 20)  
    g.addEdge(4, 5, 4)	    
    g.fillEmptyEdge()
    print(g.adj)
    print(len(g.adj))
    clone =g.cloneGraph()
    print(clone)
