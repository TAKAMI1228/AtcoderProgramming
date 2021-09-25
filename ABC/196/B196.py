X = input()
Y = X.find(".")
if Y != -1:
    print(X[:Y])
else:
    print(X)
