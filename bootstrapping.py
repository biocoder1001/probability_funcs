#!/Users/ishitajain/anaconda3/bin/python

import numpy as np
import math
import random
import tqdm 
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    random.seed(19)
    population = np.random.normal(100, 20, 100000)
    means = []
    variances = []
    for i in tqdm.tqdm(range(1000)):
        sample = np.random.choice(population, 200, replace=True)
        mean = np.mean(sample)
        variance = np.std(sample, ddof=1)
        variances.append(variance)
        means.append(mean)
    
    ax = sns.histplot(variances, kde=True)
    plt.show()

main()