from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit = (X_train, Y_train)

y_pred = gnb.predict(X_test)
cm = confusion_matrix(y_test,y_pred)
print('GNB')
print('cm')