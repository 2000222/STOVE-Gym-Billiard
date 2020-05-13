# STOVE-Gym-Billiard
Build a gym wrapper for the billard environment in ICLR paper STOVE.

# Instructions
git clone .....
cd STOVE-Gym-Billiard/STOVE-Ball-Env/gym-billard
pip install -e .
cd gym_biard/envs 
import gym
import gym_billard
env = gym.make('billard-v0')
env.observation_space
env.action_space
env.reset()
env.render()
