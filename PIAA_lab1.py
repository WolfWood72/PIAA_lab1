import numpy as np
from  IO import *
from model import *
plan_list = IO.input_plans_from_file('input.txt')
pp = [model(plan) for plan in plan_list ]


graphic_info = []
for q in np.arange(0.01,0.99,0.01):
    if q != 0.5:
        plan = np.array([elem_plan(-1, q),
                            elem_plan(-0.5, (1 - 2 * q) / 2),
                            elem_plan(0.5, (1 - 2 * q) / 2),
                            elem_plan(1, q)])
        D_crit = model(plan).Criterium.D
        graphic_info.append((q,D_crit))
a = 1


