# imports
from policy.q_learning import Q_learning
from environment.GridWorld import gridWorld
import sys
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import pickle

# Initializing the gridworld
env = gridWorld()

# predefined parameters
gamma = 0.9
state_space = 24
actions = 4
steps = 25
episodes = 100
# e = 0.5
plot = True
discount=1.0
trails = 100
rewards = []

# best parameter, order 5, e 0.2, alpha 0.5
for e in [1.0]:#, 0.2, 0.3, 0.4]:
    for alpha in [0.1]:#, 0.3, 0.4, 0.0001, 0.0005, 0.0009, 0.001, 0.005, 0.009, 0.01, 0.05, 0.09, 0.1, 0.5, 0.9]:
        for lambda_ in [0.3]:
            rewards = []
            print("Alpha: ", alpha)
            for t in tqdm(range(trails)):
                td = Q_learning(gamma, alpha, env, state_space, steps, e, plot=plot, discount=discount,lambda_=lambda_)
                td.train(episodes)
                rewards.append(td.reward)

            avg = np.average(np.array(rewards), axis=0)
            std = np.std(np.array(rewards), axis=0)
            maximumEpisodes = avg.shape[0]
            plt.errorbar(np.array([i for i in range(maximumEpisodes)]), avg, std, marker='^', ecolor='g')
            name = "return/GridQ_alpha%s.jpg" %(alpha)
            pickle.dump(avg, open(name, "wb"))
            plt.xlabel("Number of episodes")
            plt.ylabel("Total Reward")
            plt.show()
            # plt.savefig(name)
            # plt.close()