#Phoebe Corwin
#2/19/2023
#Graph Theory Practice

class Node:
    def __init__(self, n):
        self.num = n                            #Index for node
        self.edges = []                         #List of connection indices

    def connect(self, nodes):                   #One-way connect
        if isinstance(nodes, list):
            for i in nodes:
                if i.num not in self.edges:
                    self.edges.append(i.num)        #Appends indices of connections to Node edge list
        else:
            print("Input is not of type list")

    def disconnect(self, nodes):                #One-way disconnect
        if isinstance(nodes, list):
            for i in nodes:
                if i.num in self.edges:
                    self.edges.remove(i.num)        #Removes indices of connections from Node edge list
        else:
            print("Input is not of type list")

    def biconnect(self, nodes):                 #Two-way connect
        if isinstance(nodes, list):
            for i in nodes:
                if i.num not in self.edges:
                    self.edges.append(i.num)        #Appends indices of connections to both Nodes edge lists
                    i.edges.append(self.num)
        else:
            print("Input is not of type list")

    def disbiconnect(self, nodes):              #Two-way disconnect
        if isinstance(nodes, list):
            for i in nodes:
                if i.num in self.edges:
                    self.edges.remove(i.num)        #Appends indices of connections to both Nodes edge lists
                    i.edges.remove(self.num)
        else:
            print("Input is not of type list")

    def print(self):
        print(f"{self.num}: {self.edges}")

class Graph:
    def __init__(self, l):
        self.nodes = l

    def print(self):
        s = ""
        for n in self.nodes:
            s += f'{n.num}: {sorted(n.edges)}\n'
        print(s)

def main():
    N0 = Node(0)
    N1 = Node(1)
    N2 = Node(2)
    N3 = Node(3)

    G = Graph([N0, N1, N2, N3])

    N0.connect([N0, N1, N3])
    N0.biconnect([N2])

    G.print()


main()



