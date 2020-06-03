import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
canc = datasets.load_breast_cancer()

#print(canc.feature_names)
#print(canc.target_names)

#Feature and label lists
X = canc.data
y = canc.target

#Split test and train sets
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y,test_size = 0.2)

classes = ['malignant','benign']

clsf = svm.SVC(kernel="linear", C=2)
clsf.fit(x_train,y_train)
y_pred = clsf.predict(x_test)

acc = metrics.accuracy_score(y_test,y_pred)

print("Accuracy of this model is {:0.2f}".format(acc))

for i in range(len(y_pred)):
    print(i,"Prediction: ", classes[y_pred[i]])
    print ("Actual data: ", classes[y_test[i]],"\n")