# Código inicial para a criação de uma arvore de decisão 
# Realizado na aula introdutória ao conteúdo de arvore de decisão
# Foi utilizado um dataset simples e sintético apenas para demonstração
# O dataset foi criado manualmente e está disponível no arquivo data.xlsx

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import matplotlib.pyplot as plt

dados = pd.read_excel("./data.xlsx")

print(dados) # print da tabela

lb_encoder = LabelEncoder()


dados['Tempo'] = lb_encoder.fit_transform(dados['Tempo'])
dados['Vento'] = lb_encoder.fit_transform(dados['Vento'])
dados['Joga (sim/nao)'] = lb_encoder.fit_transform(dados['Joga (sim/nao)'])


print("\n\n\n\n\n")

print(dados) # vendo a mudança que o encoder fez

arvore_decisao = tree.DecisionTreeClassifier()

x = dados.iloc[:,0:4]

print("\n\n\n\n\n")
print(x) # ignorando o Y e mantendo só o X

y = dados.iloc[:,-1]

print("\n\n\n\n\n")
print(y) # mantendo só o Y

arvore_decisao = arvore_decisao.fit(x,y)

print("\n\n\n\n\n")
tree.plot_tree(arvore_decisao, feature_names=x.columns, class_names=['Sim', 'Não'], filled=True) # plotando a arvore de decisão
plt.show()
