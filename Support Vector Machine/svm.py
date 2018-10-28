from sklearn.svm import SVC
svc = SVC(kernel ='linear')
svc.fit(X_train,y_train)

y_pred = svc.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
print('SVC')
print(cm)