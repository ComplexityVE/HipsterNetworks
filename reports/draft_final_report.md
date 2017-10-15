# Analysis of the spread of hipster products throughout a network
### Authors: Victoria McDermott and Emily Lepert

## Abstract
Different people adopt ideas and products in a social network for different reasons. In this paper, we use Python to explore the influence of "hipsters" on "conformists." We consider "hipsters" to be people in a network who adopt the idea or product that is least popular at some given prior time in the simulation and "conformists" to be people who adopt the idea that most of their neighbors have adopted. We start out with one idea that "conformists" adopt and one idea that will originally only be adopted by "hipsters." We soon see that the idea that starts out only with the "hipsters" can gain almost equivalent popularity to the idea that started only with "conformists" with certain values of starting conditions and parameters. We investigate how the length of a time delay for when the hipsters are considering a product to be popular or unpopular affects which product gains popularity at steady state. 

## Introduction
We are replicating and extending the experiment done by Juul and Porter([1](#Bibliography)). They analyzed "hipsterness" in a network and the effect it had on ideas spreading throughout the network. A hipster adopts the least popular idea in a network, while a conformist adopts the most popular idea amongst its neighbors. Juul and Porter were interested in the implications the spread of ideas had on networks particularly elections, and how many anti-establishment nodes (hipsters) needed to be present in a network for the anti-establishment idea to gain popularity. We also investigate how different time delay values for when hipsters are considering products affect the distribution of products at the steady state. 

## Replication
We replicate the experiment done by Juul and Porter([1](#Bibliography)). We create a network based on data collected from Facebook([4](#Bibliography)). We assign four values to each node that will determine each node's behavior. These four values are: the status of the node (active or inactive); a threshold value phi that determines what percentage of a node’s neighbors need to be active for it to become active; a value Hi that designates whether the node is hipster or conformist (0 for conformists and 1 for hipster); the probability that any given node is a hipster; and a value P that designates the product the node has adopted (0 for no product, 1 for product 1, or 2 for product 2). Nodes all start out in an inactive state. You can think of this as how people generally all start out be politically inactive if none or very few of their neighbors are politically active. In this model, a node becomes active when a percentage of its neighbors greater than some threshold value are active. At this point in time, the newly activated node adopts a product (or idea, in the political sense) and then never changes. 

We start the simulation by randomly assigning a node product 1. From there each time step happens in two stages. Synchronously, each node updates its activity status by evaluating its neighbors and determining if there are enough that are active for that node to become active (threshold value). After, each newly activated node evaluates which product it should adopt based on its identity (hipster or conformist). A hipster node will look at the adoption fraction of the network at timestep t-\( \tau \ T \), where t is the current time step and \( \tau \ T \) is the time delay. Once a node becomes active and adopts a product, the status of that node and the product it adopts do not change.

We run 200 simulations and average the adoption fraction at each time step over the 200 simulations. The result is figure 1.
We then sweep our model for different values of p (the probability that a node is a hipster) and record the fraction of nodes that have adopted each of the two products at the time when the product distribution has reached a steady state. We generate several graphs in this manner for different values of tau. We run this model on a real Facebook data set([4](#Bibliography)) just as Juul and Porter did in their experiment.

![](https://github.com/Elepert/HipsterNetworks/blob/master/images/ReplicationT1.png)
*FIGURE 1: A graph on the adoption fraction at each time step with tau equal to 1 and P hipster equal to 0.3. At each time step we calculate the percentage of nodes that have adopted product 1 and product 2 (adoption fraction). We take the average values over 200 simulations with 20 time steps each and plot those values against each time step. The red line is the product 1 adoption fraction and the blue line is product 2. Eventually the network reaches a steady state (indicated by the horizontal line at the top right of the graph).*

Figure 1 approximately matches the behavior expected from the network based on Juul and Porter’s paper (Fig 2). The steady state for both products is between 0.4 and 0.5, while for the Juul and Porter paper, both products reach a steady state value of 0.5. Since we’re not using the same exact data set as the paper and we see similar behavior as the paper, we can attribute this error to the difference in each data set.
To observe the behavior of the model over a variety of parameters we plot the values of the adoption fraction at the last time step over a sweep of the percentage likelihood that a node will be a hipster and over different values of tau.

![](https://github.com/Elepert/HipsterNetworks/blob/master/images/FBSweepT1.png)
*FIGURE 2: Tau = 1. A graph of steady state adoption fractions of the model with tau equal to 1 and a sweep of P hipster values. For each value of P, we ran 100 simulations with time step 20 and averaged the adoption fractions at a steady state. Product 1 is in red and product 2 is in blue.*

If we compare Figure 2 to Juul and Porter’s Fig6a graph, we can see that the trends are similar. By the time P is equal to 0.2 the adoption fractions oscillate around 0.45. Juul and Porter’s graph shows a smoother line, but our values remain within the maximum and minimum values their graph bounds. We attribute the difference in values to the difference in data set. When tau is equal to 1, the likelihood that the hipster product (product 2) will overtake the conformist one is small when P<0.2, but is almost equivalent to the likelihood that the conformist product will be more popular when P>0.2. This means that when hipsters have current knowledge about the products spreading throughout network as a whole, there is little advantage given to either Product 1 or 2.

![](https://github.com/Elepert/HipsterNetworks/blob/master/images/FBSweepT4.png)
*Figure 3: Tau = 4. A graph of steady state adoption fractions of the model with tau equal to 4 and a sweep of P hipster values. For each value of P, we ran 100 simulations with time step 20 and averaged the adoption fractions at a steady state. Product 1 is in red and product 2 is in blue.*

When we compare Figure 3 to Juul and Porter's Fig6d graph, the trends are also similar. Product 2 overtakes Product 1 early on and then Product 1 overtakes Product 2. The graph indicates that there is a small window (0.2<p<0.5) in which Product 2 will end up more popular than Product 1. This indicates that with a delay in knowledge of four time steps, there cannot be a majority of hipsters in the network.

![](https://github.com/Elepert/HipsterNetworks/blob/master/images/FBSweepT5.png)
*Figure 4: Tau = 5. A graph of steady state adoption fractions of the model with tau equal to 4 and a sweep of P hipster values. For each value of P, we ran 100 simulations with time step 20 and averaged the adoption fractions at a steady state. Product 1 is in red and product 2 is in blue.*

When we compare Figure 3 to Juul and Porter's Fig6d graph, the trends are  similar. Product 2 overtakes Product 1 early on and then Product 1 overtakes Product 2. The graph indicates that there is a window (0.2<p<0.65) in which Product 2 will end up more popular than Product 1. This indicates that with a delay in knowledge of five time steps, there Product 2 is most successful when there is a slight minority or majority of hipsters in the network.

![](https://github.com/Elepert/HipsterNetworks/blob/master/images/FBSweepT6.png)
*Figure 5: Tau = 6. A graph of steady state adoption fractions of the model with tau equal to 4 and a sweep of P hipster values. For each value of P, we ran 100 simulations with time step 20 and averaged the adoption fractions at a steady state. Product 1 is in red and product 2 is in blue.*

When we compare Figure 5 to Juul and Porter's Fig6f graph, the trends are similar. Product 2 overtakes Product 1 early on and then the adoption fraction slowly decreases but Product 1 never regains popularity. The graph indicates that there is a large window (0.2<p) in which Product 2 will end up more popular than Product 1. This indicates that with a large delay in knowledge, there can be a majority of hipsters in the network.

Figure 3 shows that Product 2 overtakes Product 1 in popularity soon, and with a tau valu eof 4, the hipsters become aware of it later so they still adopt product 2 for several time steps before adopting Product 1 again (this is why Product 1 becomes popular again). Figures 4 and 5 show that Product 2 overtakes Product 1 in popularity quickly again, but with a tau value of 6, the hipsters' knowledge about the network is so delayed that they continue to adopt Product 2 even though it's popular for a long time, which is why Product 1 never becomes popular again.

## Extension:
To extend on the work done by Juul and Porter([1](#Bibliography)), we also run the model on a Barabasi and Albert model. Additionally, we play around with different starting conditions and values for percentage of hipsters, tau values, and threshold values. We are interesting in seeing if anti establishment nodes play as large a role in a Barabasi and Albert model. We are also interested in seeing if there are starting condition values that can cause "hipster" nodes to have little or no effect on the remainder of the network. 

![](https://github.com/Elepert/HipsterNetworks/blob/master/images/realBAT3.png)
*Figure 6: A graph of the adoption fraction vs P values on a Barabasi and Albert model. Tau is 3. For each value of P, we ran 100 simulations with time step 20 and averaged the adoption fractions at a steady state. Product 1 is in red and product 2 is in blue.*

(Needs analysis of extension)

We ran a sweep of threshold values from 1/20, to 1/50 on the Facebook model to investigate the impact of the threshold on the spread and found x (to be filled out).

(Graph to be generated)
*Figure 7: A graph of the adoption fraction vs threshold values. Tau is 3, P is 0.3. For each threshold value, we ran 100 simulations with time step 20 and averaged the adoption fractions at a steady state. Product 1 is in red and product 2 is in blue.*

(Needs analysis of extension)

## Conclusion
(To be edited with extension results)
The replication of the Juul and Porter paper([1](#Bibliography)) on Facebook data shows that when hipsters are less updated on the current ideas spreading throughout a network, the originally unpopular idea has a greater chance of becoming and remaining popular. Hipsters adopt the least popular product so a delay in information means that they believe that the originally unpopular idea is unpopular even when it is actualy popular.

## Bibliography
1. [Hipsters on Networks: How a Small Group of Individuals Can Lead to an Anti-Establishment Majority](https://arxiv.org/pdf/1707.07187.pdf),
*Jonas S. Juul, Mason A. Porter*; July 25, 2017.

The authors analyzed the impact of non conformists on two competing products by using a hipster threshold model and examining it in different types of networks including a Erdos-Renyi network. They were looking into how ideas that originated in a small subpopulation can spread to a large fraction of the nodes in a network. In this theoretical system there are multiple competing products and anti conformists spreading unusual products to the majority. After developing this model, the authors mathematically analyzed the conclusions and simulated the model on various synthetic networks. This model is interesting because it shows how anti establishment forces can gain power in politics and society. It also shows how unexpected parties, like Donald Trump in the most recent U.S. presidential election, might win elections and take office. There was not much validation of the model given in this paper, but it did draw some interesting conclusions. The results of the experiment show that even with a small number of non conformists, the products that originate with the non conformists or "hipsters" can become comparably or even more popular than other products. This led the authors to conclude that the anti establishment can in fact have a very large impact on the majority in a network.

2. [How the science of complex networks can help developing strategies against terrorism](http://www.sciencedirect.com/science/article/pii/S0960077903004296)
*Latora, Marchiori*, Chaos, Solitons & Fractals(April 2004) 69-75

This paper discusses how identifying the "critical components of a given communication-transportation network" could diminish the impact of terrorist attacks as well as disrupting the terrorist organization. The paper models the communication network as a graph. Each location is a node and the links are Internet channels between each location. They measure the importance of a node by measuring the drop in the network perfomance when they remove that node. Through analysis and simulation they predict the importance of each location to a terrorist network. They use the execution and aftermath of 9/11 to validate their model.


3. [Joint estimation of preferential attachment and node fitness in growing complex networks](https://www.nature.com/articles/srep32558.pdf),
*Thong Pham, Paul Sheridan, & Hidetoshi Shimodaira*; September 7, 2016.

This paper discusses the interplay of node fitness or the qualitative features of nodes which make them more likely to gain neighbors with preferential attachment or the idea that nodes which have lots of neighbors will gain neighbors at a rate faster than those that have fewer. Specifically, the authors discuss how preferential attachment and node fitness interplay in a Facebook wall-post network. They make use of a PAFit model and a Barabasi and Albert model. The purpose of the paper is to explain the coexistence of node fitness and preferential attachment and discuss how node fitness actually dominates preferential attachment. The authors analyze the model and compare it to a real world network of data on Facebook user wall posts. The real world curves agree well with the theoretical curves produced by their model. The model and output graphs support the idea that node fitness dominates preferential attachment in complex networks.

4. Dataset collected from [SNAP](https://snap.stanford.edu/data/egonets-Facebook.html)
Leskovec, Jure, Stanford University(2012)
[https://snap.stanford.edu/data/facebook_combined.txt.gz](https://snap.stanford.edu/data/facebook_combined.txt.gz)
