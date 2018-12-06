# Imports
import torch
import torch.nn as nn
from torch.distributions import Categorical


class ActorCritic(nn.Module):
    def __init__(self,  num_inputs, num_outputs, hidden_size, std=0.0):
        super(ActorCritic, self).__init__()

        self.critic = nn.Sequential(nn.Linear(num_inputs, hidden_size),
                                    nn.ReLU(),
                                    nn.Linear(hidden_size, 1)
                                    )

        self.actor = nn.Sequential(nn.Linear(num_inputs, hidden_size),
                                    nn.ReLU(),
                                    nn.Linear(hidden_size, 1)
                                    )

    def forward(self, x):
        value = self.critic(x)
        probs = self.actor(x)
        dist = Categorical(probs)
        return dist, value

