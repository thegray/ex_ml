# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 20:16:37 2018

@author: Bangun
"""

from sklearn import datasets, neighbors

iris = datasets.load_iris()

knn = neighbors.KNeighborsClassifier()

knn.fit(iris.data, iris.target)

result = knn.predict([[5.0, 5.0, 5.0, 2.0]])

##############

from sklearn import cluster, datasets

kmeans = cluster.KMeans(n_clusters = 3).fit(iris.data)

pred = kmeans.predict(iris.data)

print("pred: ")
for label in pred:
    print(label, end = ' ')
print('')
print("target: ")
for label in iris.target:
    print(label, end = ' ')

############
    
from sklearn import svm

svc = svm.LinearSVC()
svc.fit(iris.data, iris.target)
res2 = svc.predict([[5.0, 5.0, 5.0, 2.0]])
