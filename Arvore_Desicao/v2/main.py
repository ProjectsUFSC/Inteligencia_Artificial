import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


data = pd.read_csv("./Credit Score Classification Dataset.csv")

# print(data.head(10))
# print('\n\n\n\n\n\n\n\n')


# Transformando as variáveis categóricas em numéricas
lb_encoder = LabelEncoder() 

data['Gender'] = lb_encoder.fit_transform(data['Gender'])
data['Education'] = lb_encoder.fit_transform(data['Education'])
data['Marital Status'] = lb_encoder.fit_transform(data['Marital Status'])
data['Home Ownership'] = lb_encoder.fit_transform(data['Home Ownership'])
data['Credit Score'] = lb_encoder.fit_transform(data['Credit Score'])


# Separando as variáveis independentes e dependentes e transformando em array

x = data.iloc[:,0:7].values 
y = data.iloc[:,-1].values

# print (x)
# print('\n\n\n\n\n\n\n\n')
# print (y)
# print('\n\n\n\n\n\n\n\n')

# Separando os dados em treino e teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)


# Criando o modelo de árvore de decisão
desision_tree = tree.DecisionTreeClassifier()

# Treinando o modelo
desision_tree = desision_tree.fit(x_train,y_train)

# Plotando a árvore de decisão
tree.plot_tree(desision_tree, feature_names=data.columns, class_names=['Average', 'High', 'Low'], filled=True) # plotando a arvore de decisão
plt.show()

# Fazendo a predição
score = desision_tree.score(x_test, y_test)


print(f'this is the precison of the model:{score}')

