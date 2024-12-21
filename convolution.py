from decimal import *
import math
import random
import numpy as np
from scipy import stats
import tqdm
import seaborn as sns
import matplotlib.pyplot as plt


totals = []
for i in tqdm.tqdm(range(10000)):
    total = 0
    for j in tqdm.tqdm(range(100)):
        total += stats.poisson.rvs(100)
        
    
ax = sns.histplot(totals)
plt.show()