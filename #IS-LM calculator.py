#IS-LM calculator
import numpy as np
import matplotlib.pyplot as plt

class ISLM_Model:
    def __init__(self, C0, G0, I0, c, t, i, M, P, k, l):
        self.C0 = C0
        self.G0 = G0
        self.I0 = I0
        self.c = c
        self.t = t
        self.i = i
        self.M = M
        self.P = P
        self.k = k
        self.l = l
        self.autonomous_spending = self.C0 + self.G0 + self.I0
        self.multiplier_effect = 1-self.c*(1-self.t)
    def Calculate_IS_Curve(self):
        IS_intercept_Y = self.autonomous_spending/self.multiplier_effect
        IS_intercept_r = self.autonomous_spending/self.i  
        return IS_intercept_Y, IS_intercept_r 
    def Calculate_LM_Curve(self):
        LM_intercept_Y = self.M/(self.P*self.k)
        LM_intercept_r = -self.M/(self.P*self.l)
        return LM_intercept_Y, LM_intercept_r
    def Calculate_Equilibrium(self):
        Coefficient_r_IS = self.i / self.multiplier_effect
        Coefficient_r_LM = -self.l / self.k    
        Intercept_IS = self.autonomous_spending / self.multiplier_effect
        Intercept_LM = self.M/(self.P*self.k)
        A = np.array([[1,Coefficient_r_IS], [1, Coefficient_r_LM]])
        B = np.array([[Intercept_IS],[Intercept_LM]])
        Solution = np.linalg.solve(A, B)
        return Solution[0], Solution[1]

model = ISLM_Model(500, 600, 700, 0.8, 0.25, 3000, 900, 1, 0.5, 1000)
print(model.Calculate_IS_Curve())
print(model.Calculate_LM_Curve())
print(model.Calculate_Equilibrium())

Y_axis = np.linspace(0, 5000, 100)

r_IS = (model.autonomous_spending - Y_axis * model.multiplier_effect) / model.i

r_LM = (model.k / model.l) * Y_axis - model.M / (model.P * model.l)
Y_eq, r_eq = model.Calculate_Equilibrium()

plt.ylim(0, 1)
plt.xlim(0, 5000)   
plt.plot(Y_axis, r_IS, label="IS Curve", color='blue')
plt.plot(Y_axis, r_LM, label="LM Curve", color='red')
plt.plot(Y_eq, r_eq, 'ko', markersize=8, label="Equilibrium Point")
plt.vlines(x=Y_eq, ymin=0, ymax=r_eq, color='gray', linestyle='--')
plt.hlines(y=r_eq, xmin=0, xmax=Y_eq, color='gray', linestyle='--')
plt.title("Equilibrium in IS-LM Model")
plt.xlabel("National Income (Y)")
plt.ylabel("Interest Rate (r)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()