# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import numpy as np
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.core.problem import ElementwiseProblem
from pymoo.core.sampling import Sampling
from pymoo.optimize import minimize


import preprocessing
import accuracy


class MyProblem(ElementwiseProblem):

    def __init__(self):
        p = preprocessing.Preprocessor()
        min_arr = p.min_array('dataset.csv')
        max_arr = p.max_array('dataset.csv')
        #min_arr = np.append(min_arr,[0])
        #max_arr = np.append(max_arr,[6])

        super().__init__(n_var=7,
                         n_obj=2,
                         n_ieq_constr=0,
                         xl=min_arr,
                         xu=max_arr)

    def _evaluate(self, x, out, *args, **kwargs):
        p = preprocessing.Preprocessor()
        initial_array = p.read('dataset.csv')
        input_array = initial_array[0:99999]
        num_columns = len(input_array[0])
        TP = 0
        FP = 0
        TN = 0
        FN = 0
        for i in range(len(input_array)):
            point = 0
            for j in range(len(x)-1):
                if(input_array[i][j+3] < x[j]):
                    point = point + 1
            if(point >= x[len(x)-1]):
                if(input_array[i][num_columns-1] == 'TRUE'):
                    TP = TP + 1
                else:
                    FP = FP + 1
            else:
                if (input_array[i][num_columns - 1] == 'TRUE'):
                    FN = FN + 1
                else:
                    TN = TN + 1
        if ( TP+FP == 0 ):
            f1 = 0
        else:
            f1 = TP / (TP + FP)
        if ( TP+FN == 0 ):
            f2 = 0
        else:
            f2 = TP / (TP + FN)

        #g1 = 2*(x[0]-0.1) * (x[0]-0.9) / 0.18
        #g2 = - 20*(x[0]-0.4) * (x[0]-0.6) / 4.8
        #print(TP)
        #print(TN)
        #print(FP)
        #print(FN)

        out["F"] = [-f1, -f2]
        #out["G"] = [g1, g2]

class MySampling(Sampling):
    def _do(self, problem, n_samples, **kwargs):
        return np.random.rand(n_samples, problem.n_var)

problem = MyProblem()

algorithm = NSGA2 (pop_size=10,
                   sampling=MySampling())

res = minimize(problem,
               algorithm,
               ("n_gen", 5),
               verbose=False,
               seed=1)

best_solution = np.array(res.X)
#print(best_solution[0][6])

print("Best Solution (Decision Variables):")
print(best_solution)

best_objectives = res.F
print("\nBest Objectives:")
print(best_objectives[0])

acc = accuracy.Accuracy()
#acc.measure_accuracy(best_solution)
print("F1 score")
print(acc.measure_f1_score(best_objectives))
