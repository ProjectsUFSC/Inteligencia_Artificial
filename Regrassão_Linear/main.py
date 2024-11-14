import pandas as pd

dados_casas = pd.read_csv('./house_prices.csv')


import matplotlib.pyplot as plt
import seaborn as sns

dados_casas.describe()

figura = plt.figure(figsize=(20, 20))
sns.heatmap(dados_casas.drop(columns='date').corr(), annot=True)
plt.show()

"""# Preparação dos dados"""

from sklearn.model_selection import train_test_split

X = dados_casas.iloc[:, 5].values
y = dados_casas.iloc[:, 2].values


X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=0)


"""# Configuração do regressor linear"""

from sklearn.linear_model import LinearRegression

regressor_casas = LinearRegression()

regressor_casas.fit(X_treino.reshape(-1, 1), y_treino.reshape(-1, 1))

print(regressor_casas.coef_)

print(regressor_casas.intercept_)

print(X_teste[0])

print(y_teste[0])

1430 * 278.32860644 - 37893.59850107

print(regressor_casas.predict([[1430]]))

regressor_casas.score(X_teste.reshape(-1, 1), y_teste.reshape(-1, 1))

"""# Regressão com Árvore de Decisão (regressão)"""

from sklearn.tree import DecisionTreeRegressor

casas_arvore = DecisionTreeRegressor(criterion='friedman_mse')

casas_arvore.fit(X_treino.reshape(-1, 1), y_treino.reshape(-1,1))

print(casas_arvore.score(X_teste.reshape(-1, 1), y_teste.reshape(-1, 1)))

"""# Regressão com KNN"""

from sklearn.neighbors import KNeighborsRegressor

casas_knn = KNeighborsRegressor(n_neighbors=3)

casas_knn.fit(X_treino.reshape(-1, 1), y_treino.reshape(-1, 1))

print(casas_knn.score(X_teste.reshape(-1, 1), y_teste.reshape(-1, 1)))

