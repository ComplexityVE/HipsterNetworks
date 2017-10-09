import matplotlib.pyplot as plt
import scipy.io

import random
import networkx as nx
import numpy as np

from networkx.algorithms.approximation import average_clustering


def read_graph_mat(filename):
    G = nx.Graph()
    contents = scipy.io.loadmat(filename)
    array = (contents['A']).astype(int)
    edges_list = []
    for user in array:
        for edge in user:
            edges_list.append(edge)
    print(edges_list)
    G.add_edges_from(array)
    return G

def read_graph(filename):
    G = nx.Graph()
    array = np.loadtxt(filename, dtype=int)
    G.add_edges_from(array)
    G = max(nx.connected_component_subgraphs(G), key=len)
    return G

class Hipster:
    def __init__(self, G, tau, p):
        self.product_ratio = 0
        self.product_ratios = [self.product_ratio]
        self.hipsterexists = False
        self.firstrun = True
        self.tau = tau
        self.nodes_dict = {}
        self.G = G
        self.p = p
        self.totalprods = [(1,0)]
        self.alltotalprods = []
        self.totalprod1sum = {}
        self.totalprod2sum = {}
        self.master_dict= {}

        self.end_ratios_prod1 = []
        self.end_ratios_prod2 = []

    def flip(p):
        """Returns True with probability `p`."""
        return np.random.random() < p

    def initialize_hipsters(self):
        for node in self.G.nodes():
            single_node_dict = {}
            single_node_dict['state'] = 0
            single_node_dict['threshold'] = 1/33
            single_node_dict['H'] = np.random.choice([0, 1], 1, p=[1-self.p, self.p])
            single_node_dict['S'] = 0
            self.nodes_dict[node] = single_node_dict
        starting_node = int(np.random.choice(self.G.nodes(), 1))
        self.nodes_dict[starting_node]['state'] = 1
        self.nodes_dict[starting_node]['S'] = 1
        for node in self.G.nodes():
            node_dict = {0:[],1:0,2:0}
            for neighbor in self.G[node]:
                if self.nodes_dict[neighbor]['S']==1:
                    node_dict[1] += 1
                elif self.nodes_dict[neighbor]['S']==2:
                    node_dict[2] += 2
                else:
                    node_dict[0].append(neighbor)
            self.master_dict[node] = node_dict
        self.master_dict['master'] = {0:len(self.G.nodes())-1,1:1,2:0}
        #print(self.master_dict)

    def time_step(self):
        self.states_list = []
        self.stuff_changing = False

        for node in self.G.nodes():
            
            prod1 = self.master_dict[node][1]
            prod2 = self.master_dict[node][2]
            neighbors_alive = prod1+prod2  
            
            if self.nodes_dict[node]['S'] == 1:
                pass
            elif self.nodes_dict[node]['S'] == 2:
                pass
            
            #TODO fix so that it handles situation where len G.neighbors = 0
            elif neighbors_alive / len(self.G.neighbors(node)) >= self.nodes_dict[node]['threshold']:
                if self.nodes_dict[node]['H'] == 1:
                    if not self.hipsterexists:
                        product = 2
                        self.hipsterexists = True
                    elif self.product_ratio < .5:
                        product = 2
                    elif self.product_ratio > .5:
                        product = 1
                    else:
                        if Hipster.flip(.5):
                            product = 1
                        else:
                            product = 2
                else:
                    if prod1 > prod2:
                        product = 1
                    elif prod1 < prod2:
                        product = 2
                    else:
                        if Hipster.flip(.5):
                            product = 1
                        else:
                            product = 2

                self.states_list.append((node, product))

        

        for item in self.states_list:
            neighbors_list_dead = self.master_dict[item[0]][0]
            if item[1] == 1:
                self.master_dict['master'][1] += 1
            elif item[1] == 2:
                self.master_dict['master'][2] += 1
            self.master_dict['master'][0] -= 1
            for neighbor in self.G[item[0]]:
                if item[1] == 1:
                    self.master_dict[neighbor][1] += 1
                    
                elif item[1] == 2:
                    self.master_dict[neighbor][2] += 1
                index_item =self.master_dict[neighbor][0].index(item[0])
                self.master_dict[neighbor][0].pop(index_item)
            self.nodes_dict[item[0]]['state'] = 1
            self.nodes_dict[item[0]]['S'] = item[1]
            self.stuff_changing = True

        self.totalprod2 =self.master_dict['master'][2]
        self.totalprod1 = self.master_dict['master'][1]
        curr_product_ratio =  self.totalprod2/ (self.totalprod2+self.totalprod1)
        #print(curr_product_ratio)
        self.product_ratios.append(curr_product_ratio)
        self.totalprods.append((self.totalprod1, self.totalprod2))

    def run_simulation_num(self, time, num):
        self.count = 0
        for i in range(time):
            self.totalprod1sum[i] = 0
            self.totalprod2sum[i] = 0

        mini_value = 0
        for k in range(num):

            self.master_dict = {}
            self.product_ratio = 0
            self.product_ratios = [self.product_ratio]
            self.hipsterexists = False
            self.nodes_dict = {}
            self.totalprods = [(1,0)]
            self.initialize_hipsters()
            
            firsti = True
            for i in range(time):
                if i-self.tau < 0:
                    self.product_ratio = self.product_ratios[0]
                else:
                    self.product_ratio = self.product_ratios[i-self.tau]
                self.time_step()
                self.totalprod1sum[i]+=self.totalprods[i][0]
                self.totalprod2sum[i]+=self.totalprods[i][1]
                if self.master_dict['master'][0] == 0 and firsti == True:
                
                    if i > mini_value:
                        mini_value = i
                    firsti = False
            self.alltotalprods.append(self.totalprods)
            

        '''self.current_t_prod1 = []
        self.current_t_prod2 = []
        self.prod1_attimes = []
        self.prod2_attimes = []
        for k in range(time):
            for totalprods in self.alltotalprods:
                self.current_t_prod1.append(totalprods[k][0])
                self.current_t_prod2.append(totalprods[k][1])'''

        self.prod1_attimes = [self.totalprod1sum[i]/num for i in range(mini_value+1)]
        self.prod2_attimes = [self.totalprod2sum[i]/num for i in range(mini_value+1)]

    def get_ratios(self):
        prod1_ratios = [x/len(self.G.nodes()) for x in self.prod1_attimes]
        prod2_ratios = [x/len(self.G.nodes()) for x in self.prod2_attimes]
        return [prod1_ratios, prod2_ratios]

    def graph(self):
        print('done')
        ratios = self.get_ratios()
        prod1_ratios = ratios[0]
        prod2_ratios = ratios[1]

        plt.plot(prod1_ratios, 'r--', prod2_ratios, 'b--')
        plt.ylabel('Adoption Fraction')
        plt.xlabel('Time Step')
        plt.show()


'''graph = nx.watts_strogatz_graph(100, 15, 0)
hipster = Hipster(graph, 1, .9)
hipster.run_simulation(10)
hipster.graph()
fb = read_graph('facebook_combined.txt')
hipster = Hipster(fb, 1, .0)
hipster.run_simulation_num(20, 10)
hipster.graph()'''
