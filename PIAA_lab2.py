import numpy as np
from  IO import *
from model import *
import matplotlib.pyplot as plt


def Optimize(plan):
    pass

def Gradient(Plan):
    D = plan.D
    gradient = []
    for i in plan.plan:
        f = plan.f(i.x)
        gradient.append(f.T@plan.D@f)
    return gradient

def Make_A(q,n):
    Aq = np.zeros((q + 1,n)).T
    Aq[n-1] = 1        
    for i in range(q+1):
        Aq[i][i] = -1
    return np.eye(n,n) - Aq.T@np.linalg.inv(Aq@Aq.T)@Aq

x = [-1 , -0.5 ,0 , 0.5 , 1]

plan = model(IO.auto_plan(1/25,x))
isCont = True
L = 0.001
iter = 1
while isCont:
    isCont = False
    q = 0
    n = plan.n_plan
    for i in plan.plan:
        if i.p <= 1e-5:
            q = q+1
        else:
            break
    grad = Gradient(plan)
    t_phi =  grad[q+1]
    for k in grad[q+1:]:
        if t_phi != k:
            isCont = True

    avg = sum(grad[q+1:])/(n-q)
    for k in range(0,q+1):
        if avg - grad[k] < 0:
            isCont = True
    

    Gq = grad - avg
    for k in range(q):
        Gq[k] *= -1
    plan_s = []
    if isCont:
        #Gg = Make_A(q,n)@Gq
        for k in range(n):
            plan_s.append(elem_plan(plan.plan[k].x,plan.plan[k].p+L*Gq[k]))
        a = 0
        plan = model(plan_s)
        print('n_iter {}'.format(iter))
        print(plan_s)
        print('\n\n')
        iter += 1
a = 0
