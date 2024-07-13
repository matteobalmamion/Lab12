import networkx as nx

from database.DAO import DAO

class Model:
    def __init__(self):
        self._years=[]
        self._countries=[]
        self._retailers=[]
        self._sales=[]
        self._grafo=nx.Graph()
        self._percorsi=[]
        self._bestSolutions=(0,0)


    def fillDD(self):
        self._retailers=DAO.getRetailers()
        for retailer in self._retailers:
            if retailer.Country not in self._countries:
                self._countries.append(retailer.Country)
        self._sales=DAO.getAllSales()
        for sale in self._sales:
            if sale.date.year not in self._years:
                self._years.append(sale.date.year)

    def getYears(self):
        return self._years
    def getCountries(self):
        return self._countries

    def create_graph(self,country,year):
        self._grafo.clear()
        retailers=[]
        for retailer in self._retailers:
            if retailer.Country==country:
                self._grafo.add_node(retailer)
                retailers.append(retailer.Retailer_code)
        edges=[]
        for retailer1 in self._grafo.nodes():
            for retailer2 in self._grafo.nodes():
                if retailer1!=retailer2:
                    if (retailer1,retailer2) not in edges and (retailer2,retailer1) not in edges:
                        weight = DAO.getSalesYear(retailer1.Retailer_code, retailer2.Retailer_code, year)
                        if weight>0:
                            self._grafo.add_edge(retailer1,retailer2,weight=weight)
                        edges.append((retailer1,retailer2))

    def getNumNodes(self):
        return len(self._grafo.nodes())
    def getNumEdges(self):
        return len(self._grafo.edges())

    def getNodes(self):
        return self._grafo.nodes()
    def getEdges(self):
        return self._grafo.edges()

    def getVolumi(self):
        volumi=[]
        for node in self._grafo.nodes():
            volume=0
            for edge in self._grafo.edges(node):
                volume+=self._grafo.edges[edge[0],edge[1]]['weight']
            volumi.append((node.Retailer_name,volume))
        return volumi

    def find_path(self,nEdges):
        self._bestSolutions=(0,0)
        for node in self._grafo.nodes():
            nodiPercorso=[]
            percorso=[]
            self.recursive(nEdges,node,node,percorso,nodiPercorso)
        return self._bestSolutions




    def recursive(self,nEdges,node0,node,percorso,nodiPercorso):
        if len(percorso)==nEdges:
            if node0==node:
                self._percorsi.append(percorso.copy())
                somm=0
                for edge in percorso:
                    somm+=edge[2]
                if somm>=self._bestSolutions[1]:
                    self._bestSolutions=(percorso.copy(),somm)
            print(0)
            return
        nodiVicini=self._grafo.neighbors(node)
        for nodo in nodiVicini:
            if nodo not in nodiPercorso:
                percorso.append((node,nodo,self._grafo[node][nodo]["weight"]))
                nodiPercorso.append(nodo)
                self.recursive(nEdges,node0,nodo,percorso,nodiPercorso)
                percorso.pop(len(percorso) - 1)
                nodiPercorso.pop(len(nodiPercorso) - 1)





