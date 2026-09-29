import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import poisson
from scipy.optimize import curve_fit

df = pd.read_excel("обработка_эксперимент.xlsx", sheet_name=2, header=None)

poisson_pmf = lambda k,lam: poisson.pmf(k,lam)
y= df.iloc[:28, 4].dropna().to_numpy().astype(float)
x = np.arange(len(y))
y/=sum(y)

p0 = [np.sum(x * y)] #средневзвешенное
cofs,pcov=curve_fit(poisson_pmf,x,y)
ldafit = cofs[0]
print(ldafit)
print("y.sum() =", y.sum())
print("y.max() =", y.max())
bx = np.linspace(0,28,100)
by= poisson_pmf(bx,ldafit)
print("y.sum() =", by.sum())
print("y.max() =", by.max())

#гистограмма 
#plt.bar(x,y,width=0.9)
#подогнанная кривая 
bx = np.linspace(0,28,100)
plt.plot(bx,poisson_pmf(bx,12.455668544202531),color='red')
plt.show()
#plt.savefig("poisson_fit.png")#, dpi=300, bbox_inches="tight")