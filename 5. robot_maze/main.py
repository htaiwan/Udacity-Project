#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 14:12:30 2018

@author: htaiwan
"""

from Maze import Maze
from Robot import Robot
from Runner import Runner

epoch = 20

epsilon0 = 0.7
alpha = 0.5
gamma = 0.9

maze_size = (6,6)
trap_number = 1

maze = Maze(maze_size=maze_size, trap_number=trap_number)
robot = Robot(maze, alpha=alpha, epsilon0=epsilon0, gamma=gamma)
robot.set_status(learning=True)

runner = Runner(robot, maze)
runner.run_training(epoch, display_direction=True)
#runner.generate_movie(filename = "final.avi") # 你可以注释该行代码，加快运行速度，不过你就无法观察到视频了。

runner.plot_results()