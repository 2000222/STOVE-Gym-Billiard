# -*- coding: utf-8 -*-
"""
Build a gym environment for Billard interaction env.

@author: Hanxiao(Sarah)
"""
import gym
from gym import error, spaces, utils
from gym.utils import seeding
import envs as env
import sys
import numpy as np
import interactive as ins

class BillardEnv(gym.Env):
    metadata = {'render.modes': ['human','rgb_array'],
	            'video.frames_per_second':50}
				
    def __init__(self):
            
        self.env = ins.make_env() #This could build the full billiard env with avoidance tasks
        config = {'res': 32, 'hw': 10, 'n': 3, 't': 1., 'm': 1.,'granularity': 50, 'r': 1, 'friction_coefficient': 0} #such config need to be the same as in the script “interactive.py” 
        angular = 1. / np.sqrt(2)
        self.actions =  [  
        np.array([0., 0.]),
        np.array([1., 0.]),
        np.array([0., 1.]),
        np.array([angular, angular]),
        np.array([-1., 0.]),
        np.array([0., -1.]),
        np.array([-angular, -angular]),
        np.array([-angular, angular]),
        np.array([angular, -angular])]    #Nine actions to be selected
        self.action_space = spaces.Discrete(9) #9
        self.original_env = env.BillardsEnv(**config)
        self.observation_space = self.original_env.get_obs_shape()  #（32,32,3）
        self.is_initialized = True
    
    '''def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]'''
        
    def step(self,action):
        img, state, r, done = self.env.step(_action=action)
        #img= self.original_env.step()
        obs = img
        reward = r
        return obs,state,reward,done
        
    def reset(self, frame_buffer=None):
        """
        Resets the environment in the gym environment
        Returns:
		
        """      
        assert self.is_initialized, "Env. initialization required!"
        self.original_env.reset()
        #self.task.reset()
        if frame_buffer:
            self.env.frame_buffer[:] = 0.
            for i in range(3):
                self.env.step_frame_buffer(0)
            return self.env.step_frame_buffer(0)
        else:
            img, state, _, _ = self.env.step(0)
            return img, state
    
    def render(self, mode='rgb_array'):
        "it will show the full screen of the interactive billard environment to avoid the red ball"
        return ins.play_game()
 
