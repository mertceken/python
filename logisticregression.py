from sklearn.linear_model import LogisticRegression
logr = LogisticRegression(random_state=0)
logr.fit(X_train,Y_train)

y_pred = logr.predict(X_test)
print(y_pred)
print(y_test)