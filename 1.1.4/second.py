#try 2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.special import gammaln
from scipy.optimize import curve_fit

df = pd.read_excel("обработка_эксперимент.xlsx", sheet_name=2, header=None)

poisson_pmf = lambda k,lam: np.exp(k * np.log(lam) - lam - gammaln(k + 1))
y= df.iloc[:28, 4].dropna().to_numpy().astype(float)
x = np.arange(len(y))
y/=sum(y)

cofs,pcov=curve_fit(poisson_pmf,x,y)
ldafit = cofs[0]

bx = np.linspace(0,28,100)
by= poisson_pmf(bx,ldafit)

#гистограмма 
plt.bar(x,y,width=0.9)
#подогнанная кривая 
bx = np.linspace(0,28,100)
plt.plot(bx,poisson_pmf(bx,12.455668544202531),color='red')
#plt.show()
#plt.title("Гистограмма и подгонка распределением Пуассона")
#plt.xlabel("число частиц за tau=10с")
plt.ylabel("частота")

plt.savefig("no_text.png", dpi=300, bbox_inches="tight")