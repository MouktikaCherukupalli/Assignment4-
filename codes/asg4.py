import numpy as np
import pandas as pd

# Preparing the data
df = pd.read_excel(r'../Table/Table2.xlsx')
data = np.array(df)
probs = dict(zip(data[:,0], data[:,1]))

# Computing the probability
pr = (probs['Pr(X = 1|Y = 0)'] * probs['Pr(Y = 0)']) / (probs['Pr(X = 1|Y = 0)'] * probs['Pr(Y = 0)'] + probs['Pr(X = 1|Y = 1)'] * probs['Pr(Y = 1)'])
print(format(pr, '.3f'))
