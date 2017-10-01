import numpy as np
from  IO import *
from model import *
import matplotlib.pyplot as plt


x = [-1 , -0.5 ,0 , 0.5 , 1]
plan = IO.auto_plan(1/25,x)
pp = model(plan)
a = 1
