import numpy as np
import scipy as sp
import pandas as pd
import statistics

import seaborn as sns
import matplotlib.pyplot as plt


load_file = pd.read_csv('load.txt', sep=',',header=None).values

print "Media : " + str(np.average(load_file))
print "Mediana : " + str(np.median(load_file))
print "Variancia : "+str(np.var(load_file))
print "Desvio Padrao : "+str(np.std(load_file))
print "coeficiente de variabilidade : "+str(sp.stats.variation(load_file))
print "primeiro quartil : "+str(np.percentile(load_file,25))
print "segundo quartil : "+str(np.percentile(load_file,50))
print "terceiro quartil : "+str(np.percentile(load_file,75))
print "percentis 1% : "+str(np.percentile(load_file,1))
print "percentis 10% : "+str(np.percentile(load_file,10))
print "percentis 90% : "+str(np.percentile(load_file,90))
print "percentis 99% : "+str(np.percentile(load_file,99))

#PDF
sns.distplot(load_file)
plt.show()

#CDF
sns.distplot(load_file,hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
plt.show()

