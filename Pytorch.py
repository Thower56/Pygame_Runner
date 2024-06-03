import numpy as np
import torch
from torch.distributions import Categorical
import torch.nn as nn
import torch.optim as optim

import gym

env = gym.make('CartPole-v1')

# Define the policy network
class Policy(nn.Module):
    def __init__(self):
        super(Policy, self).__init__()
        self.state_space = env.observation_space.shape[0]
        self.action_space = env.action_space.n

        self.l1 = nn.Linear(self.state_space, 128, bias=False)
        self.l2 = nn.Linear(128, self.action_space, bias=False)

    def forward(self, x):    
        model = torch.nn.Sequential(
            self.l1,
            nn.Dropout(p=0.6),
            nn.ReLU(),
            self.l2,
            nn.Softmax(dim=-1)
        )
        return model(x)

# Define the function to generate an episode
def generate_episode(policy, max_steps):
    state = env.reset()
    log_probs = []
    rewards = []
    
    for steps in range(max_steps):
        state = torch.from_numpy(state).float().unsqueeze(0)  # Convert state to a PyTorch tensor
        probs = policy(state)
        m = Categorical(probs)
        action = m.sample()
        next_state, reward, done, _ = env.step(action.item())
        log_probs.append(m.log_prob(action))
        rewards.append(reward)
        state = next_state
        if done:
            break
    return log_probs, rewards

# Define the function to update the policy
def update_policy(policy, optimiser, log_probs, rewards, gamma):
    discounted_rewards = []
    for t in range(len(rewards)):
        Gt = 0 
        for r in rewards[t:]:
            Gt = Gt * gamma + r
        discounted_rewards.append(Gt)
    discounted_rewards = torch.tensor(discounted_rewards)
    discounted_rewards = (discounted_rewards - discounted_rewards.mean()) / (discounted_rewards.std() + 1e-9) # normalise discounted rewards
    policy_loss = []
    for log_prob, Gt in zip(log_probs, discounted_rewards):
        policy_loss.append(-log_prob * Gt)
    optimiser.zero_grad()
    policy_loss = torch.cat(policy_loss).sum()
    policy_loss.backward()
    optimiser.step()

# Train the agent
policy = Policy()
optimiser = optim.Adam(policy.parameters(), lr=1e-2)
max_episode_num = 5000
max_steps = 10000
gamma = 0.99

for episode in range(max_episode_num):
    log_probs, rewards = generate_episode(policy, max_steps)
    update_policy(policy, optimiser, log_probs, rewards, gamma)
    if episode % 50 == 0:
        print('Episode {}\tLast reward: {}\tAverage reward: {:.2f}'.format(episode, rewards[-1], np.mean(rewards[-100:])))