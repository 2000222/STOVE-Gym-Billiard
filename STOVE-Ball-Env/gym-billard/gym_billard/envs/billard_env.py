# -*- coding: utf-8 -*-
"""
Build a gym environment for Billard interaction env.
@author: Hanxiao
"""
import gym
from gym import error, spaces, utils
from gym.utils import seeding
import envs as env
import sys
import numpy as np
from gym.envs.classic_control import rendering

#script_args = sys.argv[2:]
#env.main(script_args)
'''env = env.BillardsEnv(n=NUM_BALLS, r=BALL_RADIUS, granularity=GRANU, t=0.1)
env_1 = env.BillardsEnv(n=3, r=1.2, granularity=50, t=0.1)
task = env.AvoidanceTask(env_1, 4, greyscale=False, action_force=0.3)
img = env_1.draw_balls()'''
class BillardEnv(gym.Env):
    metadata = {'render.modes': ['human','rgb_array'],
	            'video.frames_per_second':50}
				
    def __init__(self):
            
        self.env = env.BillardsEnv(n=3, r=1., m=1., hw=10, granularity=5, res=32, t=1.,init_v_factor=0, friction_coefficient=0., seed=None, sprites=False)
        self.task = env.AvoidanceTask(self.env, 4, greyscale=False, action_force=0.3) #num_stacked=4
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
        self.observation_space = self.env.get_obs_shape()  #（32,32,3）
        self.is_initialized = True
        
        
    def step(self,action):
        frame_buffer, state, r, done = self.task.step_frame_buffer(_action=action)
        img= self.env.step()
        obs = img
        reward = r
        return obs,reward,done,frame_buffer
        
    def reset(self, frame_buffer=False):
        """
        Resets the environment in the gym environment
        Returns:
		
        """      
        assert self.is_initialized, "Env. initialization required!"
        self.env.reset()
        #self.task.reset()
        if frame_buffer:
            self.task.frame_buffer[:] = 0.
            for i in range(3):
                self.task.step_frame_buffer(0)
            return self.task.step_frame_buffer(0)
        else:
            img, state, _, _ = self.task.step(0)
            return img, state
    
    def render(self, mode='human'):
        #screen_width = 600
        #screen_height = 400
        #self.viewer = rendering.Viewer(screen_width, screen_height)
        self.viewer = rendering.SimpleImageViewer()
		ball_img = self.env.draw_balls()
        #self.viewer.add_geom(ball)
		self.viewer.imshow(ball_img)
        return ball_img
		