from replication import Hipster, read_graph
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

'''
fb = read_graph('facebook_combined.txt')
hipster = Hipster(fb, 1, .3)
hipster.run_simulation_num(20, 10)
hipster.graph()'''
# fb = read_graph('facebook_combined.txt')
graph = nx.erdos_renyi_graph(5000, 5/5000)


def sweep(tau):
    end1_values = []
    end2_values = []
    ps = np.arange(0, 1, .05)
    pplot = list(ps)
    for p in ps:
        hipster = Hipster(graph, tau, p, threshold=.2)
        hipster.run_simulation_num(20, 50)
        ratios = hipster.get_ratios()
        end1_values.append(ratios[0][-1])
        end2_values.append(ratios[1][-1])
        print('pass done: ' + str(p))
    print('end1_values: '+str(end1_values))
    print('end2_values: '+str(end2_values))
    plt.plot(pplot, end1_values, 'r--')
    plt.plot(pplot, end2_values, 'b--')
    plt.xlabel('P Hipster')
    plt.ylabel('Adoption Fraction at Steady State')
    print('show')
    plt.show()



def threshold_sweep(tau):
    end1_values = []
    end2_values = []
    ts = np.arange(0, 0.35, .02)
    pplot = list(ts)
    for t in ts:
        hipster = Hipster(graph, tau, 0.3, t)
        hipster.run_simulation_num(20, 50, er=False, ba=False)
        ratios = hipster.get_ratios()
        end1_values.append(ratios[0][-1])
        end2_values.append(ratios[1][-1])
        print('pass done: ' + str(t))
    print('end1_values: '+str(end1_values))
    print('end2_values: '+str(end2_values))
    plt.plot(pplot, end1_values, 'r--')
    plt.plot(pplot, end2_values, 'b--')
    plt.xlabel('Threshold')
    plt.ylabel('Adoption Fraction at Steady State')
    print('show')
    plt.show()

sweep(4)
