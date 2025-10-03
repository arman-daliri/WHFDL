import pandas as pd
from sklearn.model_selection import train_test_split

import FWHFDL as fw

data_path = '../Data/data.csv'

data = pd.read_csv(data_path)
X = data.drop(['state'], axis=1)
y = data['state']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

fwhh = fw.FWHH()
fwhh.data_set(X_train, y_train, X_test, y_test)
fwhh.problem_set()
# iteration of each algorithm
fwhh.problem.MaxIt = 15
# iteration of whh
fwhh.MaxIt = 15
fwhh.algs_set()
fwhh.pop_set()
res = fwhh.run()
print("Best Cost:", res['best_cost'])
print("Selected Num:", res['selected_num'])
print("Selected:", res['selected'])
