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
    return G

class Hipster:
    def __init__(self, G, tau, p):
        self.product_ratio = 0
        self.product_ratios = [self.product_ratio]
        self.hipsterexists = False
        self.tau = tau
        self.nodes_dict = {}
        self.G = G
        self.p = p
        self.totalprods = [(1,0)]
        self.alltotalprods = []
        self.totalprod1sum = {}
        self.totalprod2sum = {}

    def flip(p):
        """Returns True with probability `p`."""
        return np.random.random() < p

    def initialize_hipsters(self):
        for node in self.G.nodes():
            single_node_dict = {}
            single_node_dict['state'] = 0
            single_node_dict['threshold'] = 1/33
            single_node_dict['H'] = np.random.choice([0, 1], 1, p=[self.p, 1-self.p])
            single_node_dict['S'] = 0
            self.nodes_dict[node] = single_node_dict

    def time_step(self):
        self.totalprod1 = 0
        self.totalprod2 = 0
        self.states_list = []

        for node in self.G.nodes():
            neighbors_alive = 0
            prod1 = 0
            prod2 = 0
            for neighbor in self.G.neighbors(node):
                if self.nodes_dict[neighbor]['state'] == 1:
                    neighbors_alive+=1
                    if self.nodes_dict[neighbor]['S'] == 1:
                        prod1+=1
                    else:
                        prod2+=1
            if self.nodes_dict[node]['S'] == 1:
                self.totalprod1 +=1
            elif self.nodes_dict[node]['S'] == 2:
                self.totalprod2 +=1
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

        curr_product_ratio = self.totalprod2 / (self.totalprod2+self.totalprod1)
        self.product_ratios.append(curr_product_ratio)
        self.totalprods.append((self.totalprod1, self.totalprod2))

        for item in self.states_list:
            self.nodes_dict[item[0]]['state'] = 1
            self.nodes_dict[item[0]]['S'] = item[1]

    def run_simulation_num(self, time, num):
        for i in range(time):
            self.totalprod1sum[i] = 0
            self.totalprod2sum[i] = 0
        for k in range(num):
            self.product_ratio = 0
            self.product_ratios = [self.product_ratio]
            self.hipsterexists = False
            self.nodes_dict = {}
            self.totalprods = [(1,0)]
            self.initialize_hipsters()
            starting_node = int(np.random.choice(self.G.nodes(), 1))
            self.nodes_dict[starting_node]['state'] = 1
            self.nodes_dict[starting_node]['S'] = 1
            for i in range(time):
                if i-self.tau < 0:
                    self.product_ratio = self.product_ratios[0]
                else:
                    self.product_ratio = self.product_ratios[i-self.tau]
                self.time_step()
                self.totalprod1sum[i]+=self.totalprods[i][0]
                self.totalprod2sum[i]+=self.totalprods[i][1]
            self.alltotalprods.append(self.totalprods)
        '''self.current_t_prod1 = []
        self.current_t_prod2 = []
        self.prod1_attimes = []
        self.prod2_attimes = []
        for k in range(time):
            for totalprods in self.alltotalprods:
                self.current_t_prod1.append(totalprods[k][0])
                self.current_t_prod2.append(totalprods[k][1])'''
        self.prod1_attimes = [self.totalprod1sum[i]/num for i in range(time)]
        self.prod2_attimes = [self.totalprod2sum[i]/num for i in range(time)]


    def graph(self):
        prod1_ratios = [x/len(self.G.nodes()) for x in self.prod1_attimes]
        prod2_ratios = [x/len(self.G.nodes()) for x in self.prod2_attimes]

        plt.plot(prod1_ratios, 'r--', prod2_ratios, 'bs')

        plt.show()


'''graph = nx.watts_strogatz_graph(100, 15, 0)
hipster = Hipster(graph, 1, .9)
hipster.run_simulation(10)
hipster.graph()'''
fb = read_graph('facebook_combined.txt')
hipster = Hipster(fb, 1, .3)
hipster.run_simulation_num(40, 10)
hipster.graph()
