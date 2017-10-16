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
        cur_plan = model(plan)
        for k in range(len(plan)):
            f = self.f(self.plan[k].x)
            M_xk = np.zeros((self.m,self.m))
            '''for i in range(self.m):
                    M_xk[i] +=  f[i] * f * plan[k].p'''
            Grad.append(f.T@cur_plan.D@f)

        return np.array(Grad)

    def MakeG(self,n,q):
        '''Aq = np.zeros((q + 1,n)).T
        Aq[n-1] = 1        
        for i in range(q+1):
            Aq[i][i] = -1
        tt = np.linalg.det(Aq@Aq.T)
        if tt == 0:
            return np.eye(n,n)
        else:
            return np.eye(n,n) - Aq.T@np.linalg.inv(Aq@Aq.T)@Aq
        '''
        pass


    def phi(self,p_x,p_ksi):
        x = model(p_x)
        ksi = model(p_ksi)
        return (ksi.D@x.M).trace()
    def NextPlan(self,plan,lyambda,gradient,n,q):
        G = self.MakeG(n,q)
        ps_1 = plan
        tt = lyambda*G@gradient
        for i in range(n):
            ps_1[i].p = plan[i].p + tt[i]
        return ps_1

    def optimize(self):
        plan = self.plan
        n = self.n_plan
        IcContinue = True
        while IcContinue:
            IcContinue = True
            q = len([1 for i in self.plan if np.abs(i.p) <= 1e-5 ])
            grad = self.Gradient(plan)
            
            s_fi = np.sum(grad[q+1:])/(n-q)
            Gp_Grad = np.zeros(n)
            for j in range(q+1,n):
                Gp_Grad[j] = grad[j] - s_fi
            flag = False
            for i in range(q + 1,n):
                for j in range(q + 1,n):
                    if grad[i] != grad[j]:
                        flag = True                            
            if not flag:
                IcContinue = False
            for j in range(q):
                if s_fi - grad[j] <= 0 :
                    IcContinue = True
            if  IcContinue:
                for i in range(n):
                    plan[i].p = plan[i].p + 1* Gp_Grad[i]
        return plan



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








