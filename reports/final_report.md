# Analysis of the spread of hipster products throughout a network
### Authors: Victoria McDermott and Emily Lepert

## Abstract
How do anti-establishment ideas spread throughout a network? What factors into the success of one idea over another? In this paper, we use Python to explore the influence of "hipsters" on "conformists." We consider "hipsters" to be anti-establishment people in a network who adopt the idea or product that is least popular at some given prior time in the simulation and "conformists" to be people who adopt the idea that most of their neighbors have adopted. We start out with one idea that "conformists" adopt and one idea that will originally only be adopted by "hipsters." We soon see that the idea that starts out only with the "hipsters" can gain almost equivalent popularity to the idea that started only with "conformists" with certain values of starting conditions and parameters. We investigate how the length of a time delay for when the hipsters are considering a product to be popular or unpopular affects which product gains popularity at a final steady state.

_________________________________________________________

We are replicating and extending the experiment done by Juul and Porter([1](#Bibliography)). They analyzed "hipsterness" in a network and the effect it had on ideas spreading throughout a Facebook network. A hipster adopts the least popular idea in a network, while a conformist adopts the most popular idea amongst its neighbors. Juul and Porter were interested in the implications the spread of ideas had on networks, particularly elections, and how many anti-establishment nodes (hipsters) needed to be present in a network for the anti-establishment idea to gain popularity. We also investigate how different time delay values for when hipsters are considering products affect the distribution of products at the steady state. We later extend our work by applying our model to Barabasi and Albert models to see how the spread of ideas is different from a real Facebook network.

### Ideas spreading throughout a Facebook network
We replicate the experiment done by Juul and Porter([1](#Bibliography)). We create a network based on data collected from Facebook([2](#Bibliography)). Our Facebook dataset is different than the one used in the paper, so our results are quantitatively different, but qualitatively similar.

We assign four values to each node that will determine each node's behavior. These four values are:
- the status of the node (active or inactive)
- a threshold value φ that determines what percentage of a node’s neighbors need to be active for it to become active (we use 1/33 to replicate the threshold value used in Juul and Porter's paper)
- a value H<sub>i</sub> that designates whether the node is a hipster or conformist
- and a value p that designates the product the node has adopted

Nodes all start out in an inactive state. This is similar to how people generally all start out be politically inactive if none or few of their neighbors are politically active, but the more someone is surrounded by politically active people, the more likely that person is to become politically active themselves. In this model, a node becomes active when a percentage of its neighbors greater than its φ value are active. As soon as a node is activated, it adopts a product (or idea, in the political sense).

We start the simulation by determining which nodes are conformists and which nodes are hipsters. We iterate through all nodes in the network, assigning a node a hipster personality with probability p, or a conformist personality with probability 1-p. We then randomly assign one node product 1, the conformist (traditional) product regardless of whether this starting node is a conformist or hipster. From there on, each time step happens in two stages. Synchronously, each node updates its activity status by evaluating the percentage of neighbors that are active. If the percentage is greater than or equal to the nodes' φ value, then the node becomes active. After becoming activated, each node evaluates which product it should adopt based on its identity (hipster or conformist). The first time a hipster is activated (not including the starting node if that node was a hipster) it will automatically be assigned to product 2, the anti establishment product. In the future, after this initial hipster has been assigned product 2, a hipster node will look at the adoption fraction of the network at timestep t-τ, where t is the current time step and τ is the time delay. The hipster will adopt whichever product was least popular in the general population at the timestep t-τ. A conformist node will find which product is adopted by the majority of its neighbors and adopt that product. Once a node becomes active and adopts a product, the status of that node as activated and the product that node has adopted will never change.

We run 200 simulations of our model on a Facebook dataset and average the adoption fraction of each product at every time step over the 200 simulations. The result is Figure 1.
We then sweep our model for different values of p (the probability that a node is a hipster) and record the fraction of nodes that have adopted each of the two products at the time when the product distribution has reached a steady state (Figures 2-5). The distribution eventually reaches a steady state because nodes don't change products after they become active. We generate several graphs in this manner for different values of τ. We run this model on a real Facebook data set([4](#Bibliography)) just as Juul and Porter did in their experiment.

#### Single 

| <img src="https://github.com/Elepert/HipsterNetworks/blob/master/images/labelReplicationT1.png" width="70%">| <img src="https://github.com/Elepert/HipsterNetworks/blob/master/images/FBOriginalSingle.png" width="250%">|
|--|-------|
*Figure 1a) A graph of the adoption fraction at each time step with τ = 1 and p value equal to 0.3. At each time step we calculate the percentage of nodes that have adopted product 1 and product 2 (adoption fraction). We take the average values over 200 simulations with 20 time steps each and plot those values against each time step. The red line is the product 1 adoption fraction and the blue line is product 2. Eventually the network reaches a steady state (indicated by the horizontal line at the top right of the graph).*|*Figure 1b) Juul and Porter's graph of the adoption fraction at teach time step with τ = 1 and τ = 4 with p = 0.3. The red and purple triangles on the graph is what Fig 1a) is replicating.*|

Figure 1a approximately matches the behavior expected from the network based on Juul and Porter’s paper (Fig 1b). In Fig 1a, the steady state for both products is between 0.4 and 0.5, while in Fig 1b, both products reach a steady state value of 0.5. Since we are not using the same exact data set as the paper and we see similar behavior as the paper, we can attribute this error to the difference in each data set. From 0< t <10, each product spreads throughout the network evenly. That is, the hipster nodes manage to spread product 2 sufficiently enough that the conformist nodes start spreading product 2 as well as product 1.

#### Sweep of p values

To observe the behavior of the model over a variety of parameters we plot the values of the adoption fraction at the last time step over a sweep of p values (the percentage likelihood that a node will be a hipster), over different values of τ.

| <img src="https://github.com/Elepert/HipsterNetworks/blob/master/images/labelFBSweepT1.png" width="70%"> | <img src="https://github.com/Elepert/HipsterNetworks/blob/master/images/OriginalFBT1.png" width="250%">|
|--|-------|
*FIGURE 2a): τ = 1. A graph of steady state adoption fractions of the model with τ equal to 1 and a sweep of p values. For each value of p, we ran 100 simulations with time step 20 and averaged the adoption fractions at a steady state.* | *Figure 2b): Juul and Porter graph of the steady state adoption fractions of their model with τ = 1.*|

If we compare Figure 2a to Juul and Porter’s graph (Fig 2b), we can see that the trends are similar. By the time p is equal to 0.2 the adoption fractions oscillate around 0.45. Fig 2b shows a smoother line, but our values remain within the maximum and minimum values the graph bounds. We attribute the difference in values to the difference in data set. When τ is equal to 1, the likelihood that the hipster product (product 2) will overtake the conformist one is small when p<0.2, but is almost equivalent to the likelihood that the conformist product will be more popular when p>0.2. This means that when hipsters have current knowledge about the products spreading throughout network as a whole, there is little advantage given to either Product 1 or 2.

When the steady state is reached in our graphs there is an adoption fraction of about 40% for each product whereas in the original graph there was an adoption fraction of about 50% for each of the two products at steady state. Further, when p = 0, we should expect to see 100% Product 1 in the network, but we only see about 85%. This is because we used a different Facebook data set in which some of the nodes are isolated and not connected to the larger network. This means that there will never be enough nodes active around them for them to become activated. Because some of the nodes in our data set never become activated the adoption fractions of each product do not necessarily add up to 1 at steady state.

| <img src="https://github.com/Elepert/HipsterNetworks/blob/master/images/labelFBSweepT4.png" width="70%"> | <img src="https://github.com/Elepert/HipsterNetworks/blob/master/images/OriginalFBT4.png" width="150%"> |
|--|-------|
|*Figure 3a) τ = 4. A graph of steady state adoption fractions of the model with τ = 4 and a sweep of p values. For each value of p, we ran 100 simulations with time step 20 and averaged the adoption fractions at a steady state.*|*Figure3b) Juul and Porter graph of the steady state adoption fractions of their model with τ = 4.*|

When we compare Figure 3a to Juul and Porter's graph (Fig 3b), we see similar qualitative and quantitative behavior. Product 2 overtakes Product 1 early on and then Product 1 overtakes Product 2. The graph indicates that there is a small window (0.2< p <0.5) in which Product 2 will end up more popular than Product 1. This indicates that with a delay in knowledge of τ = 4, the hipster product does not win out when there is a majority of hipsters in the network (p>0.5).

| <img src="https://github.com/Elepert/HipsterNetworks/blob/master/images/labelFBSweepT6.png" width="70%"> | <img src="https://github.com/Elepert/HipsterNetworks/blob/master/images/OriginalFBT6.png" width="150%"> |
|--|-------|
|*Figure 4a) τ = 6. A graph of steady state adoption fractions of the model with τ = 6 and a sweep of p values. For each value of p, we ran 100 simulations with time step 20 and averaged the adoption fractions at a steady state.*|*Figure 4b) Juul and Porter graph of the steady state adoption fractions of their model with τ = 6.*|

When we compare Figure 4a to Juul and Porter's graph (Fig 4b), the trends are similar. Product 2 overtakes Product 1 early on and then the adoption fraction slowly decreases but Product 1 never regains popularity. The graph indicates that there is a large window (p>0.2) in which Product 2 will end up more popular than Product 1. This indicates that with a large delay in knowledge, the hipster product can win out even when there is a majority of hipsters in the network.

There needs to be at least 20% of the network to be hipster nodes for product 2 to even have a chance at becoming more popular than product 1 no matter what τ is. The bigger the time delay in knowledge hipsters have, the more likely the hipster or anti-establishment idea is to become more popular than product 1.

#### Relevance of τ values

To summarize our findings on the importance of τ values on the spread of network ideas, we generated a graph of adoption fractions vs τ values to see the general trend in adoption fractions.

![](https://github.com/Elepert/HipsterNetworks/blob/master/images/tausweepp3.png)

*Figure 5) Sweep of τ values vs adoption fraction. p= 0.3, φ=1/33.*

Juul and Porter do not generate a similar graph, but the behavior shown by this graph is consistent with our results. As τ becomes bigger, Product 2 has becomes more and more popular.

### Extending the work:

To extend on the work done by Juul and Porter([1](#Bibliography)), we also run the model on a Barabasi and Albert model. Additionally, we play around with different φ (threshold) values. We are interested in seeing if anti-establishment nodes play as large a role in a Barabasi and Albert model. We are also interested in seeing if there are starting condition values that can cause "hipster" nodes to have little or no effect on the remainder of the network.

#### Investigating φ values

We ran a sweep of threshold values (φ) from 0, to 0.35 on the Facebook model to investigate the impact of the activation threshold (φ) on the spread.

| <img src="https://github.com/Elepert/HipsterNetworks/blob/master/images/FBSweepThT4P04.png"> | <img src="https://github.com/Elepert/HipsterNetworks/blob/master/images/FBSweepThT4P3.png"> |
|--|-------|
| *Figure 6a) A graph of the adoption fraction vs φ (threshold) values on the Facebook dataset. τ = 5, p = 0.04. For each value of φ, we ran 100 simulations with time step 20 and averaged the adoption fractions at a steady state.*|*Figure 6b) A graph of the adoption fraction vs φ (threshold) values on the Facebook dataset. τ = 5, p = 0.3. For each value of φ, we ran 100 simulations with time step 20 and averaged the adoption fractions at a steady state.*|

As shown in the replication portion, when p=0.04, Product 1 always dominates no matter what τ value, so it makes sense that in Fig 6a, no matter what φ value each node has, product 1 will always be more popular than product 2. Similarly, when p=0.3, Product 2 tends to dominate for τ = 3,4,5,6 and is even with Product 1 when τ=1,2.

Fig 6b shows that when φ>=0.07, both products have the same adoption fraction. Generally, both Fig 6a and Fig 6b show that when the φ>=0.15, no product wins. Intuitively this makes sense because each node needs 15% of its neighbors to be active for it to become active, meaning that it is hard for node activity to spread. The starting node must be neighbors with nodes with few other neighbors for any product to gain a foothold in the network. The likelihood that a random selection from all of the graph nodes to yield such a node is small. 

#### Applying the model to BA graphs

| <img src="https://github.com/Elepert/HipsterNetworks/blob/master/images/labelrealBAT1.png"> | <img src="https://github.com/Elepert/HipsterNetworks/blob/master/images/labelrealBAT3.png"> |
|--|-------|
| *Figure 7a) A graph of the adoption fraction vs p values on a Barabasi and Albert model. τ = 1. For each value of p, we ran 100 simulations with time step 20 and averaged the adoption fractions at a steady state.*|*Figure 7b) A graph of the adoption fraction vs p values on a Barabasi and Albert model. τ = 3. For each value of p, we ran 100 simulations with time step 20 and averaged the adoption fractions at a steady state.*|

In our investigation of Barabasi and Albert models we learn that the anti establishment "hipster" nodes in fact have an even larger impact than they do on the regular Facebook data. This is probably because Barabasi and Albert models are created with preferential attachment in mind, meaning that when a hipster node is a hub node, it has a large impact on the network. Certain nodes have high concentrations of neighbors, meaning one hipster can have a much larger impact than they would if they had fewer neighbors. As can be seen in the above graph, we only need about a 20% probability of hipsters for product 2 to always win out over product 1. This is different from the Facebook graph where product 2 was gaining popularity when the probability of hipsters was between 20% and 40% but not when it was over 40%.

## Conclusion
The replication of the Juul and Porter paper([1](#Bibliography)) on Facebook data shows that when hipsters are less updated on the current ideas spreading throughout a network, the originally unpopular idea has a greater chance of becoming and remaining popular. Hipsters adopt the least popular product so a delay in information means that they believe that the originally unpopular idea is unpopular even when it is actually popular.

Additionally, we learned that "hipsters" have an even larger effect when considered as part of a Barabasi and Albert model and we suspect that the reason for the increased influence of hipsters on these types of networks has to do with the increase in preferential attachment. We also learned that with large threshold values (φ), neither product will gain popularity because the lack of active neighbors will result in all nodes not becoming active. This makes sense in that neighborhoods which are not politically active with people who are stubborn (represented by nodes with high threshold values who need a very high percentage of active neighbors for themselves to become active) will generally not become politically active and neither idea or product will become active.

## Bibliography
1. [Hipsters on Networks: How a Small Group of Individuals Can Lead to an Anti-Establishment Majority](https://arxiv.org/pdf/1707.07187.pdf),
*Jonas S. Juul, Mason A. Porter*; July 25, 2017.

The authors analyzed the impact of non conformists on two competing products by using a hipster threshold model and examining it in different types of networks including a Erdos-Renyi network. They were looking into how ideas that originated in a small subpopulation can spread to a large fraction of the nodes in a network. In this theoretical system there are multiple competing products and anti conformists spreading unusual products to the majority. After developing this model, the authors mathematically analyzed the conclusions and simulated the model on various synthetic networks. This model is interesting because it shows how anti establishment forces can gain power in politics and society. It also shows how unexpected parties, like Donald Trump in the most recent U.S. presidential election, might win elections and take office. There was not much validation of the model given in this paper, but it did draw some interesting conclusions. The results of the experiment show that even with a small number of non conformists, the products that originate with the non conformists or "hipsters" can become comparably or even more popular than other products. This led the authors to conclude that the anti establishment can in fact have a very large impact on the majority in a network.

2. Dataset collected from [SNAP](https://snap.stanford.edu/data/egonets-Facebook.html)
Leskovec, Jure, Stanford University(2012)
[https://snap.stanford.edu/data/facebook_combined.txt.gz](https://snap.stanford.edu/data/facebook_combined.txt.gz)
