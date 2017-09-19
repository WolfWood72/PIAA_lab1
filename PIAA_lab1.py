import numpy as np
from  IO import *
from model import *
import matplotlib.pyplot as plt
plan_list = IO.input_plans_from_file('input.txt')
pp = [model(plan) for plan in plan_list ]

for i in range(len(pp)):
    print('plan №' + str(i))
    print('M-matrix:')
    print(pp[i].M)
    print('D-matrix:')
    print(pp[i].D)

print('№\t\tD\t\tA\t\tE\t\tF2\t\tLyambda\t\tMV\t\tG')
for i in range(len(pp)):
    print('{}\t{:08.4f}\t{:08.4f}\t{:08.4f}\t{:08.4f}\t{:08.4f}\t{:08.4f}\t{:08.4f}\t{}'.format(i,
                                                 pp[i].crit_D,
                                                 pp[i].crit_A,
                                                 pp[i].crit_E,
                                                 pp[i].crit_Ф,
                                                 pp[i].crit_Lymbda,
                                                 pp[i].crit_MV,
                                                 pp[i].crit_G,
                                                 pp[i].sum_crit))

plot_x = [0]
plot_y = [0]
for q in np.arange(0,0.51,0.01):
    if q not in (0.5,-0.5,0):
        plan = np.array([elem_plan(-1, q),
                         elem_plan(-0.5, (1 - 2 * q) / 2.0),
                         elem_plan(0.5, (1 - 2 * q) / 2.0),
                         elem_plan(1, q)])
        D_crit = model(plan).crit_D
        #graphic_info.append((q,D_crit))
        plot_x.append(q)
        plot_y.append(D_crit)
a = 1

print("q")
print((plot_y.index(max(plot_y)) + 1) * 0.01)
print("value")
print(max(plot_y))


fig = plt.figure()
plt.plot(plot_x, plot_y)

plt.scatter((plot_y.index(max(plot_y)) + 1) * 0.01, max(plot_y))
plt.ylabel('D-crit')
plt.xlabel('q')
plt.grid(True)
plt.text((plot_y.index(max(plot_y)) + 1) * 0.01 + 0.01, max(plot_y), 'max', fontsize=12)
plt.show()

