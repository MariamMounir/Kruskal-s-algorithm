class Graph:
    def __init__(self,vertices): 
        self.v=vertices #node
        self.graph=[]

    def add_edge(self,u,v,w):
        self.graph.append([u,v,w]) 

    #search function
    def find(self,parent,i):
        if parent[i]==i:
            return i
        return self.find(parent,parent[i])

    def apply_union(self,parent,rank,x,y):
        xroot=self.find(parent,x)
        yroot=self.find(parent,y)
        if rank[xroot]<rank[yroot]:
            parent[xroot]=y
        elif rank[xroot]>rank[yroot]:
            parent[yroot]=xroot
        else:
            parent[yroot]=xroot
            rank[xroot]+=1

    #Applying kruskal alg
    def Kruskal_algo(self):
        result=[]
        i,e=0,0
        self.graph=sorted(self.graph,key=lambda item: item[2])
        parent=[]
        rank=[]
        for node in range(self.v):
            parent.append(node)
            rank.append(0)
        while e<self.v -1:
            u,v,w=self.graph[i]
            i=i+1
            x=self.find(parent,u)
            y=self.find(parent,v)
            if x != v:
                e=e+1
                result.append([u,v,w])
                self.apply_union(parent,rank,x,y)
            for u,v,weight in result:
               print("Edge:",u, v,end =" ")
               print("-",weight)
        


g_input=int(input("Enter the number of Node:"))
g=Graph(g_input)
end=True
while end== True:
    s=int(input("Enter source: "))
    d=int(input("Enter destination: "))
    w=int(input("Enter weight: "))
    g.add_edge(s,d,w)
    add=(input("do u want to add another node y/n: "))
    if add == "n":
        end=False

g.Kruskal_algo()
