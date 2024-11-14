import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

dataset = pd.read_csv('./wine.csv')

print(dataset.head(5))

X = dataset.iloc[:,1:3].values

y = dataset.iloc[:,-1]


# px.scatter(x = X[:,0], y = X[:,1]).show()

k_means = KMeans(n_clusters= 2)

k_means.fit(X)

centroides = k_means.cluster_centers_
labels = k_means.labels_

fig1 = px.scatter(x = X[:,0], y = X[:,1], color = labels)
fig2 = px.scatter(x = centroides[:,0], y = centroides[:,1], size = [10,10])
fig3 = go.Figure(data = fig1.data + fig2.data)
fig3.show() 