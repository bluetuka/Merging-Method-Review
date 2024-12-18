import FlowNetwork

class MiniCut:

    #Time O(1), Space O(1)
    def __init__(self, graph):
        self.graph = graph   

    #Time O(V+E), Space O(V)
    def bfs(self, rGraph, s, t, parent):
        visited ={}
        for x in rGraph.keys():
            visited[x] = False
        queue=[]
        parent[s] = None; 
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for v in rGraph.keys():
                if visited[v] == False and rGraph[u][v] > 0 :
                    queue.append(v)
                    parent[v] = u
                    visited[v] = True                  
        return True if visited[t] else False
         
    #Time O(V+E), Space O(V)  
    def dfs(self, rgraph,s,visited):
        visited[s]=True
        for v in rgraph.keys():
            if rgraph[s][v]>0 and visited[v] == False:
                self.dfs(rgraph,v,visited)

    #Time O(V2+E), Space O(V)
    def cut_partition(self, g, source, sink):
        parent = {}
        rGraph = self.graph.cloneGraph()
        for x in rGraph.keys():
            parent[x] = None

        #use bfs to find path and update capacity
        while self.bfs(rGraph, source, sink, parent) :
            path_flow = float("Inf")
            v = sink
            while(v != source):
                u= parent[v]
                path_flow = min (path_flow, rGraph[u][v])
                v= parent[v]
            v = sink
            while(v != source):
                u = parent[v]
                rGraph[u][v] -= path_flow
                rGraph[v][u] += path_flow
                v = parent[v]

        #use dfs to find the vertices reachable from source
        visited ={}
        for x in rGraph.keys():
            visited[x]=False
        self.dfs(rGraph, source, visited)   

        # define result
        upStream=set()
        downStream = set()
        central = set()
        upStream.add(source)
        downStream.add(sink)
        for x in rGraph.keys():
            if x!=source and x!=sink:
                central.add(x)

        #find min s-t cut-set
        for i  in rGraph.keys():
            for j in rGraph.keys() : 
                if g[i][j]>0 and visited[i] and visited[j] == False :
                    print (str(i) + " - " + str(j))
                    upStream.add(i)
                    downStream.add(j)
                    if i in central:
                        central.remove(i)
                    if j in central:
                        central.remove(j)
        print("upstream: "+ str(upStream))
        print("downstream: "+str(downStream))
        print("central: "+ str(central))
    

g= FlowNetwork.FlowNetwork()
g.addEdge(0, 1, 16) 
g.addEdge(0, 2, 13) 	    
g.addEdge(1, 2, 10) 
g.addEdge(2, 1, 4) 	    
g.addEdge(1, 3, 12) 
g.addEdge(3, 2, 9) 
g.addEdge(2, 4, 14) 
g.addEdge(4, 3, 7) 	    
g.addEdge(3, 5, 20)   
g.addEdge(4, 5, 4) 	    
g.fillEmptyEdge()	  

m = MiniCut(g); 
m.cut_partition(g.adj, 0, 5)
print()

g1= FlowNetwork.FlowNetwork()
g1.addEdge("S", "A", 7); 
g1.addEdge("S", "B", 5); 
g1.addEdge("A", "C", 4); 
g1.addEdge("A", "B", 4); 	    	       
g1.addEdge("C", "T", 6); 
g1.addEdge("B", "T", 7); 
g1.fillEmptyEdge();   

m1 = MiniCut(g1); 
m1.cut_partition(g1.adj,  "S", "T")
print()