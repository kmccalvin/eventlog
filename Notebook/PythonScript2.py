from pythonnet import load
load("coreclr")
import sys
import os
import platform
sys.path.append(os.path.abspath(r"../Widget/bin/Debug/net6.0-windows10.0.22621.0"))

import clr
clr.AddReference("Widget")

from Widget import RobotCreator

print(os.name)
print(platform.system())
print(platform.release())

robotCreator = RobotCreator()
robot = robotCreator.CreateRobot()