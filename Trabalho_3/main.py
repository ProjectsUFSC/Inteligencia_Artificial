import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Importando bibliotecas do Sklearn para pré-processamento, modelagem e avaliação
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# Importando bibliotecas do Keras para construção e treinamento da rede neural
from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping

# Leitura do dataset a partir de um arquivo CSV localizado no diretório atual
ds = pd.read_csv("./Salary Data.csv")

# Exibição das estatísticas descritivas do dataset para entender a distribuição dos dados
print("Estatísticas descritivas do dataset:")
print(ds.describe())

# Verificação de valores ausentes em cada coluna para identificar a necessidade de limpeza de dados
print("\nDados ausentes por coluna:")
print(ds.isnull().sum())

# Codificação das variáveis categóricas utilizando LabelEncoder para transformar texto em números
label_encoder = LabelEncoder()
ds['Gender'] = label_encoder.fit_transform(ds['Gender'])
ds['Education Level'] = label_encoder.fit_transform(ds['Education Level'])
ds['Job Title'] = label_encoder.fit_transform(ds['Job Title'])

# Separação das variáveis independentes (X) e da variável dependente (y)
X = ds.iloc[:, :-1].values  # Todas as colunas exceto a última (Salário)
y = ds.iloc[:, -1].values   # A última coluna (Salário)

# Aplicação da normalização nas variáveis independentes para padronizar os dados
scaler_X = StandardScaler()
X = scaler_X.fit_transform(X)

# Redimensionamento e normalização da variável dependente
scaler_y = StandardScaler()
y = y.reshape(-1, 1)
y = scaler_y.fit_transform(y)

# Divisão dos dados em conjuntos de treinamento e teste (90% treino, 10% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

# ----- Modelo de Rede Neural (ANN) -----

# Definição da arquitetura da rede neural sequencial
ann = Sequential()
ann.add(Dense(units=128, activation='relu', input_dim=X_train.shape[1]))  # Camada de entrada com 128 neurônios e ativação ReLU
ann.add(Dropout(0.2))  # Camada de Dropout para prevenir overfitting
ann.add(Dense(units=64, activation='relu'))  # Camada oculta com 64 neurônios e ativação ReLU
ann.add(Dropout(0.2))  # Outra camada de Dropout
ann.add(Dense(units=1, activation='linear'))  # Camada de saída com ativação linear para regressão

# Compilação do modelo com o otimizador Adam e a função de perda MSE
optimizer = Adam(learning_rate=0.001)
ann.compile(optimizer=optimizer, loss='mean_squared_error')

# Definição do callback para parada antecipada caso a validação não melhore após 10 épocas
early_stopping = EarlyStopping(monitor='val_loss', patience=10)

# Treinamento do modelo de rede neural com validação e callback de parada antecipada
ann.fit(X_train, y_train, validation_split=0.1, epochs=500, batch_size=32, callbacks=[early_stopping])

# ----- Modelo de Random Forest -----

# Definição da grade de parâmetros para otimização via Grid Search
param_grid = {
    'n_estimators': [100, 200, 300],          # Número de árvores na floresta
    'max_depth': [None, 10, 20],             # Profundidade máxima das árvores
    'min_samples_split': [2, 5, 10]          # Número mínimo de amostras para dividir um nó
}

# Inicialização do regressor Random Forest
rf = RandomForestRegressor(random_state=50)

# Configuração do Grid Search com validação cruzada de 5 folds
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, scoring='r2', n_jobs=-1)
grid_search.fit(X_train, y_train.ravel())

# Seleção do melhor modelo obtido pelo Grid Search
best_rf = grid_search.best_estimator_

# Treinamento do modelo Random Forest com os melhores parâmetros encontrados
best_rf.fit(X_train, y_train.ravel())

# ----- Previsões e Avaliação dos Modelos -----

# Previsão dos salários no conjunto de teste utilizando a rede neural
y_pred_ann = ann.predict(X_test)
# Reversão da normalização para obter os valores reais de salário
y_pred_ann = scaler_y.inverse_transform(y_pred_ann)
y_test_actual = scaler_y.inverse_transform(y_test)

# Cálculo do R² para o modelo de rede neural
r2_ann = r2_score(y_test_actual, y_pred_ann)
print(f"R2 Score para a Rede Neural: {r2_ann}")

# Previsão dos salários no conjunto de teste utilizando o Random Forest
y_pred_rf = best_rf.predict(X_test)
# Redimensionamento e reversão da normalização
y_pred_rf = y_pred_rf.reshape(-1, 1)
y_pred_rf = scaler_y.inverse_transform(y_pred_rf)

# Cálculo do R² para o modelo de Random Forest
r2_rf = r2_score(y_test_actual, y_pred_rf)
print(f"R2 Score para o Random Forest: {r2_rf}")

# ----- Critérios de Avaliação dos Modelos -----

# Cálculo do Erro Quadrático Médio (MSE) para a Rede Neural
mse_ann = mean_squared_error(y_test_actual, y_pred_ann)
print(f"Mean Squared Error para a Rede Neural: {mse_ann}")

# Cálculo do Erro Absoluto Médio (MAE) para a Rede Neural
mae_ann = np.mean(np.abs(y_test_actual - y_pred_ann))
print(f"Mean Absolute Error para a Rede Neural: {mae_ann}")

# Cálculo do Erro Quadrático Médio (MSE) para o Random Forest
mse_rf = mean_squared_error(y_test_actual, y_pred_rf)
print(f"Mean Squared Error para o Random Forest: {mse_rf}")

# Cálculo do Erro Absoluto Médio (MAE) para o Random Forest
mae_rf = np.mean(np.abs(y_test_actual - y_pred_rf))
print(f"Mean Absolute Error para o Random Forest: {mae_rf}")

# ----- Visualizações para Comparação dos Modelos -----

# Configuração do estilo dos gráficos
sns.set(style="whitegrid")

# Gráfico de Comparação dos R² Scores
metrics = ['R²']
ann_scores = [r2_ann]
rf_scores = [r2_rf]

x = np.arange(len(metrics))  # Posições no eixo x
width = 0.35  # Largura das barras

fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, ann_scores, width, label='Rede Neural')
bars2 = ax.bar(x + width/2, rf_scores, width, label='Random Forest')

# Adicionando rótulos e título
ax.set_ylabel('Valores de R²')
ax.set_title('Comparação dos R² Scores dos Modelos')
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend()

# Adição de rótulos de valor nas barras
for bar in bars1 + bars2:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Deslocamento de 3 pontos acima da barra
                textcoords="offset points",
                ha='center', va='bottom')

plt.show()

# Gráfico de Erros Absolutos Médios
metrics_mae = ['MAE']
ann_mae = [mae_ann]
rf_mae = [mae_rf]

x = np.arange(len(metrics_mae))

fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, ann_mae, width, label='Rede Neural')
bars2 = ax.bar(x + width/2, rf_mae, width, label='Random Forest')

ax.set_ylabel('Valores de MAE')
ax.set_title('Comparação dos Erros Médios Absolutos dos Modelos')
ax.set_xticks(x)
ax.set_xticklabels(metrics_mae)
ax.legend()

for bar in bars1 + bars2:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

plt.show()

# Gráfico de Dispersão das Previsões vs. Valores Reais para a Rede Neural
plt.figure(figsize=(8,6))
sns.scatterplot(x=y_test_actual.flatten(), y=y_pred_ann.flatten(), color='blue', label='Rede Neural')
plt.plot([y_test_actual.min(), y_test_actual.max()], [y_test_actual.min(), y_test_actual.max()], 'k--', lw=2)
plt.xlabel('Valores Reais')
plt.ylabel('Previsões')
plt.title('Rede Neural: Previsões vs. Valores Reais')
plt.legend()
plt.show()

# Gráfico de Dispersão das Previsões vs. Valores Reais para o Random Forest
plt.figure(figsize=(8,6))
sns.scatterplot(x=y_test_actual.flatten(), y=y_pred_rf.flatten(), color='green', label='Random Forest')
plt.plot([y_test_actual.min(), y_test_actual.max()], [y_test_actual.min(), y_test_actual.max()], 'k--', lw=2)
plt.xlabel('Valores Reais')
plt.ylabel('Previsões')
plt.title('Random Forest: Previsões vs. Valores Reais')
plt.legend()
plt.show() 