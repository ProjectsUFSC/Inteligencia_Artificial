from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import plotly.express as ex
import pandas as pd

ds = pd.read_csv('./wine.csv')

X = ds.iloc[:,0:11].values
ss = StandardScaler()

ss.fit(X)
X_ss = ss.transform(X)

dbscan = DBSCAN(eps=0.9, min_samples=3)
kmeans = KMeans(n_clusters=2)


dbscan.fit(X_ss)
kmeans.fit(X_ss)


labels_dbscan = dbscan.labels_
labels_kmeans = kmeans.labels_

print(labels_dbscan)
print(labels_kmeans)

plt1 = ex.scatter(x=X[:, 0], y=X[:, 1], color=labels_dbscan)
plt1.show()
plt2 = ex.scatter(x=X[:, 0], y=X[:, 1], color=labels_kmeans)
plt2.show()
