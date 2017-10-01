import numpy as np

class elem_plan(object):
    def __init__(self,x=None,p=None):
        self.x = x
        self.p = p




class model(object):

          

    def __init__(self,plan):
        self.plan = plan  
        self.n_plan = len(plan)
        self.m = len(self.f((0,0)))  
        self.Make_M()
        self.Make_D()
        self.Calc_Criterium()
    '''def f(self,x):
        return np.array([1,x,x * x])'''

    def f(self,x):
        return np.array([1,x[0],x[1],x[0] * x[1],x[0] * x[0],x[1] * x[1]])
    
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
       self.crit_D = self.Calc_D()
       self.crit_A = self.Calc_A()
       self.crit_E = self.Calc_E()
       self.crit_Ф = self.Calc_Ф()
       self.crit_Lymbda = self.Calc_Lymabda()
       self.crit_MV = self.Calc_MV()
       self.crit_G = self.Calc_G()
       self.sum_crit = self.crit_D + self.crit_A + self.crit_E + self.crit_Ф + self.crit_Lymbda + self.crit_MV + self.crit_G

        
    
    def Gradient(self,plan):
        Grad = []
        for i in range(len(plan)):
            f = self.f(self.plan[k].x)
            M = np.zeros((self.m,self.m))
            for i in range(len(plan)):
                    M[i] +=  f[i] * f
            Grad.append(np.linalg.det(M))
        return np.array(Grad)

    def MakeG(self,n,q):
        Aq = np.zeros((q + 1,n))
        Aq[n-1] = 1        
        for i in range(q+1):
            Aq[i][i] = -1
      
        return np.eye(n,n) - Aq.T@np.linalg.inv(Aq@Aq.T)@Aq

    def NextPlan(self,plan,lyambda,gradient,n,q):
        G = self.MakeG(n,q)
        ps_1 = plan
        lyambda*G@gradient
        

    def optimize(self):
        plan = self.plan
        n = self.n_plan
        IcContinue = True
        while IcContinue:
            q = len([1 for i in self.plan if i.p == 0 ])
            grad = self.Gradient(plan)
            s_fi = 0
            for i in range(q + 1,n):
                s_fi = grad[i]
                for j in range(q + 1,n):
                    if grad[i] != grad[j]:
                         IcContinue = False
            s_fi = s_fi / (n - q)
            for j in range(q):
                if s_fi - grad[j] <= 0 :
                    IcContinue = False
            if not IcContinue:
                plan = self.NextPlan()



    def Calc_D(self):
        return  np.linalg.det(self.M)
    def Calc_E(self):
        return np.max(np.linalg.eig(self.D)[0])
    def Calc_A(self):
        return self.D.trace()
    def Calc_Ф(self, p=2):
        return ((1.0 / self.m) * (self.D ** p).trace()) ** (1.0 / p)
    def Calc_Lymabda(self):
        return np.sum((np.linalg.eig(self.D)[0] - np.average(np.linalg.eig(self.D)[0])) ** 2)
    def Calc_MV(self):
        return np.max(np.diag(self.D))
    def Calc_G(self):
        def d(x):
            return self.f(x).T @ self.D @ self.f(x)
        return np.max([ d(self.plan[i].x) for i in range(self.n_plan)])








