# Analysis of the spread of hipster products throughout a network
### Authors: Victoria McDermott and Emily Lepert

## Abstract
Different people adopt ideas and products in a social network for different reasons. In this paper, we use Python to explore the influence of "hipsters" on "conformists." We consider "hipsters" to be people in a network who adopt the idea or product that is least popular at some given prior time in the simulation and "conformists" to be people who adopt the idea that most of their neighbors have adopted. We start out with one idea that "conformists" adopt and one idea that will originally only be adopted by "hipsters." We soon see that the idea that starts out only with the "hipsters" can gain almost equivalent popularity to the idea that started only with "conformists" with certain values of starting conditions and parameters. 

## Introduction

## Replication
	We replicate the experiment done by Juul and Porter. We create a network based on the Facebook Data. We assign to each node four values that will determine the behavior of each node and the spread of the products throughout the network. These four values are: the status of the node (active or inactive); a threshold value phi that determines what percentage of a node’s neighbors need to be active for it to become active; a value Hi that designates whether the node is hipster or conformist (0 for conformists and 1 for hipster); the probability that any given node is a hipster; and a value P that designates the product the node has adopted (0 for no product, 1 for product 1, or 2 for product 2).
	We start the simulation by randomly assigning a node product 1. From there each time step happens in two stages. Synchronously, each node updates its activity status by evaluating its neighbors and determining if there are enough that are active for that node to become active (threshold value). After, each newly activated node evaluates which product it should adopt based on its identity (hipster or conformist). A hipster node will look at the adoption fraction of the network at timestep t-tau, where t is the current time step and tau is the time delay. Once a node becomes active and adopts a product, the status of that node and the product it adopts do not change.
	We run 200 simulations and average the adoption fraction at each time step over the 200 simulations. The result is figure 1.

FIGURE:
	At each time step we calculate the percentage of nodes that have adopted product 1 and product 2 (adoption fraction) and plot it.

To observe the behavior of the model over a variety of parameters we plot the values of the adoption fraction at the last time step over a sweep of the percentage likelihood that a node will be a hipster and over different values of tau.

FIGURE:
	Sweep

## Extension:
Barabasi and Albert:
playing around with values and trying to break it:

## Conclusion

## Bibliography
[Hipsters on Networks: How a Small Group of Individuals Can Lead to an Anti-Establishment Majority](https://arxiv.org/pdf/1707.07187.pdf),
*Jonas S. Juul, Mason A. Porter*; July 25, 2017.

The authors analyzed the impact of non conformists on two competing products by using a hipster threshold model and examining it in different types of networks including a Erdos-Renyi network. They were looking into how ideas that originated in a small subpopulation can spread to a large fraction of the nodes in a network. In this theoretical system there are multiple competing products and anti conformists spreading unusual products to the majority. After developing this model, the authors mathematically analyzed the conclusions and simulated the model on various synthetic networks. This model is interesting because it shows how anti establishment forces can gain power in politics and society. It also shows how unexpected parties, like Donald Trump in the most recent U.S. presidential election, might win elections and take office. There was not much validation of the model given in this paper, but it did draw some interesting conclusions. The results of the experiment show that even with a small number of non conformists, the products that originate with the non conformists or "hipsters" can become comparably or even more popular than other products. This led the authors to conclude that the anti establishment can in fact have a very large impact on the majority in a network. 

[How the science of complex networks can help developing strategies against terrorism](http://www.sciencedirect.com/science/article/pii/S0960077903004296)
*Latora, Marchiori*, Chaos, Solitons & Fractals(April 2004) 69-75

This paper discusses how identifying the "critical components of a given communication-transportation network" could diminish the impact of terrorist attacks as well as disrupting the terrorist organization. The paper models the communication network as a graph. Each location is a node and the links are Internet channels between each location. They measure the importance of a node by measuring the drop in the network perfomance when they remove that node. Through analysis and simulation they predict the importance of each location to a terrorist network. They use the execution and aftermath of 9/11 to validate their model. 


[Joint estimation of preferential attachment and node fitness in growing complex networks](https://www.nature.com/articles/srep32558.pdf),
*Thong Pham, Paul Sheridan, & Hidetoshi Shimodaira*; September 7, 2016.

This paper discusses the interplay of node fitness or the qualitative features of nodes which make them more likely to gain neighbors with preferential attachment or the idea that nodes which have lots of neighbors will gain neighbors at a rate faster than those that have fewer. Specifically, the authors discuss how preferential attachment and node fitness interplay in a Facebook wall-post network. They make use of a PAFit model and a Barabasi and Albert model. The purpose of the paper is to explain the coexistence of node fitness and preferential attachment and discuss how node fitness actually dominates preferential attachment. The authors analyze the model and compare it to a real world network of data on Facebook user wall posts. The real world curves agree well with the theoretical curves produced by their model. The model and output graphs support the idea that node fitness dominates preferential attachment in complex networks.

Links to look at for formatting/style:
https://sites.google.com/site/allendowney/style-guide
https://sites.google.com/site/complexityscience17/lectures/lecture-08

