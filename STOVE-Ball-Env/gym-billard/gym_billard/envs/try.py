# -*- coding: utf-8 -*-
"""
Created on Mon May 11 07:36:15 2020

@author: Sarah

such a file just is used to restore some efficient python commands to have a good understanding of the STOVE environment.
"""

import envs as env
config = {
        'res': 32, 'hw': 10, 'n': 3, 'dt': 1, 'm': 1., 'fc': 0,
        'granularity': 10, 'r': 1.2, 'check_overlap': False, 'drift': True}
env.generate_data()
env = env.BillardsEnv(n=NUM_BALLS, r=BALL_RADIUS, granularity=GRANU, t=0.1)
env_1 = env.BillardsEnv(n=3, r=1.2, granularity=50, t=0.1)
task = env.AvoidanceTask(env_1, 4, greyscale=False, action_force=0.3)
img = env_1.draw_balls()
import matplotlib.pyplot as plt
plt.imshow(img)
plt.show()
img_1 = env_1.draw_sprites()
env_1.__init__(sprites=True)
img_1 = env_1.draw_sprites()
plt.imshow(img_1)
plt.show()

env_1.__init__()

#返回default的环境
env_2 = env.BillardsEnv(n=3, r=1., m=1., hw=10, granularity=5, res=32, t=1.,init_v_factor=0, friction_coefficient=0., seed=None, sprites=False)
img_2 = env_2.draw_balls()
plt.imshow(img_2)
plt.show()
viewer.imshow(img_2)

env_2.simulate_physics(2)
env_2.step()
img, state, done = env_2.step()
plt.imshow(img)
plt.show()

env_2.get_state_shape()
env.generate_fitting_run(env.BillardsEnv)

#在env基础上对task进行研究
env_0 = env.BillardsEnv(n=3, r=1., m=1., hw=10, granularity=5, res=32, t=1.,init_v_factor=0, friction_coefficient=0., seed=None, sprites=False)
task = env.AvoidanceTask(env_0, 4, greyscale=False, action_force=0.3)
task.get_action_space()



task.get_framebuffer_shape()
task.resolve_action(6)
task.resolve_action(8)
task.calculate_reward()
task.step(6)
img,state, r, done = task.step(8)
plt.imshow(img)
plt.show()

action = task.resolve_action(6,8)
#self.frame_buffer, state, r, done = task.step_frame_buffer(_action=action)
frame_buffer, state, r, done = task.step_frame_buffer(_action=6)
print(frame_buffer.shape)
frame_buffer, state, r, done = task.step_frame_buffer(_action=8)



import envs as env
env_2 = env.BillardsEnv(n=3, r=1., m=1., hw=10, granularity=5, res=32, t=1.,init_v_factor=0, friction_coefficient=0., seed=None, sprites=False)
task = env.AvoidanceTask(env_2, 4, greyscale=False, action_force=0.3)
from gym.envs.classic_control import rendering
img,state,r,done = task.step(8)
viewer = rendering.SimpleImageViewer()
#viewer.__init__(display)
img = zoom(img, [5, 5, 1], order=0)
viewer.imshow(img)
viewer.isopen
viewer.close()
import matplotlib.pyplot as plt
plt.imshow(img)
plt.show()
exit()

import pygame
screen = pygame.display.set_mode((200,200))
img = pygame.image.load(img)
screen.blit(img,(0,0))

screen_width = 600
screen_height = 400
viewer_2 = rendering.Viewer(screen_width, screen_height)
viewer_2.render()
import numpy as np
xs = np.linspace(-1.2, 0.6, 100)
ys = np.sin(3 * xs)*.45+.55
scale = 600/1.8
xys = list(zip((xs+1.2)*scale, ys*scale))
track = rendering.make_polyline(xys)
track.set_linewidth(4)
viewer_2.add_geom(track)
viewer_2.add_geom(img)

import gym
import gym_billard
env = gym.make('billard-v0')
env.observation_space
env.action_space
env.reset()
env.render()
##修改render function，首先呈现picture,其次是gif
'''import matplotlib.pyplot as plt
plt.imshow(ball_img)
plt.show()'''
env.step()
##Maybe we can create gif with imageio



