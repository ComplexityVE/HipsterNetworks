from replication import Hipster, read_graph
import numpy as np
import matplotlib.pyplot as plt

'''
fb = read_graph('facebook_combined.txt')
hipster = Hipster(fb, 1, .3)
hipster.run_simulation_num(20, 10)
hipster.graph()'''
fb = read_graph('facebook_combined.txt')

def sweep(tau):
    end1_values = []
    end2_values = []
    ps = np.arange(0, 1, .05)
    pplot = list(ps)
    for p in ps:
        hipster = Hipster(fb, tau, p)
        hipster.run_simulation_num(20, 100)
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

sweep(1)
