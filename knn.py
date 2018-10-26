

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5, metric='minkowski')
knn.fit(X_train,Y_train)

y_pred = knn.predict(X_test)
cm = confusion_matrix(y_test,y_pred)
print(cm)
