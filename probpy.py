#!/Users/ishitajain/anaconda3/bin/python
from decimal import *
import math
import random
import numpy as np
from scipy import stats
import tqdm
import seaborn as sns
import matplotlib.pyplot as plt
getcontext().prec = 5
for i  in range(10):
    r = Decimal(random.randint(1,5)/5)
    print(r)
total = 0
totals = []
for i in tqdm.tqdm(range(10000)):
    for i in tqdm.tqdm(range(100)):
        total += stats.uniform.rvs(0,1)
    totals.append(total)
ax = sns.histplot(totals, bins=100, binrange=(0,100))
plt.show()



n = math.pow(10, 20)
print(type(n))
no_of_perms = math.factorial(52)
denominator = no_of_perms
numerator = no_of_perms-1

getcontext().prec = 5
log_numerator = Decimal(numerator).ln()
log_denominator = Decimal(denominator).ln()
log_pr = log_numerator - log_denominator

print(type(Decimal(n)*log_pr))
