# imports
from sarsaPoly import Sarsa
from cartPole import CartPole
import sys
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

# arg1 = float(sys.argv[1])

# Initializing the gridworld
env = CartPole()

# predefined parameters
gamma = 1.0
state_space = 24 #not used in this code
actions = 2
steps = 25 #not used in this code
episodes =100
e = 0.2
discount=1.0
plot = True
trails = 100
type = "poly"


# best parameter, order 3, e 0.2, alpha 0.5
# best parameter, order 5, e 0.2, alpha 0.5
for e in [0.1, 0.2, 0.4]:
    for order in [2, 3, 5]:
        for alpha in [0.0001, 0.0005, 0.0009, 0.001, 0.005, 0.009, 0.01, 0.05, 0.09, 0.1, 0.5, 0.9]:
            rewards = []
            print("Alpha: ", alpha)
            for t in tqdm(range(trails)):
                # print("Alpha: %s, Trail: %s" %(alpha, t))
                td = Sarsa(gamma, alpha, env, state_space, steps, e, plot=plot, order=order, discount=discount)
                td.train(episodes)
                rewards.append(td.reward)

            avg = np.average(np.array(rewards), axis=0)
            std = np.std(np.array(rewards), axis=0)
            maximumEpisodes = avg.shape[0]
            plt.errorbar(np.array([i for i in range(maximumEpisodes)]), avg, std, marker='^', ecolor='g')
            name = "Sarsa/figures/poly/cartPole_type_%s_order%s_alpha%s_e%s.jpg" %(type, order, alpha, e)
            plt.xlabel("Number of episodes")
            plt.ylabel("Total Reward")
            plt.savefig(name)
            plt.close()