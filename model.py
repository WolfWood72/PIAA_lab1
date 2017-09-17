import numpy as np

class elem_plan(object):
    def __init__(self,x=None,p=None):
        self.x = x
        self.p = p




class model(object):
    """description of class"""
    class Criterium(object):
        D = None
        A = None
        E = None
        Ф = None
        Lymbda = None
        MV = None
        G = None
            


    def __init__(self,plan):
        self.plan = plan  
        self.n_plan = len(plan)
        self.m = len(self.f(0))  
        self.Make_M()
        self.Make_D()
        self.Calc_Criterium()
    def f(self,x):
        return np.array([1,x,x * x])
    
    def Make_M(self):
        M = np.zeros((self.m,self.m))
        for k in range(self.n_plan):
            f = self.f(self.plan[k].x)
            for i in range(self.m):
                    M[i] += self.plan[k].p * f[i] * f
        self.M = M
    def Make_D(self):
        self.D = np.linalg.inv(self.M)

    def Calc_Criterium(self):
        self.Criterium.D = self.Calc_D()
        self.Criterium.A = self.Calc_A()
        self.Criterium.E = self.Calc_E()
        self.Criterium.Ф = self.Calc_Ф()
        self.Criterium.Lymbda = self.Calc_Lymabda()
        self.Criterium.MV = self.Calc_MV()
        self.Criterium.G = self.Calc_G()

    def Calc_D(self):
        return  np.linalg.det(self.M)
    def Calc_E(self):
        return np.max(np.linalg.eig(self.D)[0])
    def Calc_A(self):
        return self.D.trace()
    #Допилить
    def Calc_Ф(self, p=2):
        return ((1.0 / self.m)* (self.D**p).trace())** (1.0/p)
    def Calc_Lymabda(self):
        return np.sum(np.linalg.eig(self.D)[0] - np.average(np.linalg.eig(self.D)[0])) ** 2
    def Calc_MV(self):
        return np.max(np.diag(self.D))
    def Calc_G(self):
        def d(x):
            return self.f(x).T @ self.D @ self.f(x)
        return np.max([ d(self.plan[i].x) for i in range(self.n_plan)])






'''
class OptimaCriterium(object):
    def __init__(self,plan_list,m,fx):
        self.plan_list = plan_list  
        self.cnt_plan = len(plan_list)  
        self.m = m
        self.fx = fx

    def Calc_D(self):
        return np.max([np.linalg.det(self.plan_list[i].M) for i in range(self.cnt_plan)])
    def Calc_E(self):
        return np.min([np.max(np.linalg.eig(plan_list[i].D)[0]) for i in range(self.cnt_plan)])
        
    def Calc_A():
        return np.min([plan_list[i].D.trace() for i in range(self.cnt_plan)])
    #Допилить
    def Calc_Ф(self):
        return np.min([(1.0 / self.m) * plan_list[i].D.trace() for i in range(self.cnt_plan)]) ** (1.0 / 2.0)
    def Calc_Lymabda(self):
        return np.min([np.sum(np.linalg.eig(plan_list[i].D)[0] - np.average(np.linalg.eig(plan_list[i].D)[0])) ** 2 for i in  range(self.cnt_plan)])
    def Calc_MV(self):
        return np.min([np.max(np.diag(plan_list[i].D)) for i in range(self.cnt_plan)])
    def Calc_G(self):
        def d(x,plan):
            return self.fx(x).T @ plan.D @ self.fx
       
        for i in range(self.cnt_plan):
            for j in self.plan_list[i].plan:
                d(j.x,self.plan_list[i].plan)
'''


    


    