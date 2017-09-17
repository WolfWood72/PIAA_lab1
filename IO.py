from model import *


class IO(object):
    """description of class"""

    def input_plans_from_file(filename):
        plan = []
        file = open(filename, "r")
        n = int(file.readline())
        for i in range(n):
            x = file.readline().replace('\n','').split('\t')
            p = file.readline().replace('\n','').split('\t')
            plan.append(list(map(lambda x: elem_plan(float(x[0]),float(x[1])), list(zip(x,p)))))
            #plan.append(list(elem_plan(float(x[0]),float(x[1])) for x in zip(x,p)))
        print(plan)
        return plan


