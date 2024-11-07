import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import  neighbors
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


data = pd.read_csv("./ObesityDataSet_raw_and_data_sinthetic.csv")

# print(data.head(10))
# print('\n\n\n\n\n\n\n\n')


# Transformando as variáveis categóricas em numéricas
lb_encoder = LabelEncoder() 

data['Gender'] = lb_encoder.fit_transform(data['Gender'])
data['CALC'] = lb_encoder.fit_transform(data['CALC'])
data['FAVC'] = lb_encoder.fit_transform(data['FAVC'])
data['SCC'] = lb_encoder.fit_transform(data['SCC'])
data['SMOKE'] = lb_encoder.fit_transform(data['SMOKE'])
data['family_history_with_overweight'] = lb_encoder.fit_transform(data['family_history_with_overweight'])
data['CAEC'] = lb_encoder.fit_transform(data['CAEC'])
data['MTRANS'] = lb_encoder.fit_transform(data['MTRANS'])
data['NObeyesdad'] = lb_encoder.fit_transform(data['NObeyesdad'])




# Separando as variáveis independentes e dependentes e transformando em array

x = data.iloc[:,0:17]
y = data.iloc[:,-1]

# print (x.head(10))
# print('\n\n\n\n\n\n\n\n')
# print (y.head(10))
# print('\n\n\n\n\n\n\n\n')

# Separando os dados em treino e teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)


# Criando o modelo de KNN
knn = neighbors.KNeighborsClassifier(n_neighbors=5)

# Treinando o modelo
knn = knn.fit(x_train,y_train)

# Fazendo a predição
score = knn.score(x_test, y_test)


print(f'this is the precison of the model:{score}')

