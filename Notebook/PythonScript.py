from pythonnet import load
load("coreclr")
import sys
import os
import platform
sys.path.append(os.path.abspath(r"../Widget/bin/Debug/net6.0"))

import clr
clr.AddReference("Widget")

from Widget import Robot

print(os.name)
print(platform.system())
print(platform.release())

robot = Robot()
eventLog = robot.CreateEventLog()