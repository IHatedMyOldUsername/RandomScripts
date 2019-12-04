from sklearn import datasets
from sklearn import svm

cancer = datasets.load_breast_cancer()

iris = datasets.load_iris()
digits = datasets.load_digits()

clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])
print(clf.predict(digits.data[-1:]))

# X_train, X_test, y_train, t_test = train_test_split(X,y)

