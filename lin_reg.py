#import tensorflow as tf
import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("student-mat.csv", sep=';')
data = data[['G1','G2','G3','studytime','failures','absences']]

predict = "G3"

X = np.array(data.drop([predict],1))

y = np.array(data[predict])
best_score = 0
for x in range(50):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split (X, y, test_size=0.1)

    linear = linear_model.LinearRegression ()

    linear.fit (x_train, y_train)

    accuracy = linear.score (x_test, y_test)

    print("Accuracy is: {:0.2f}".format (accuracy))
    if accuracy > best_score:
        best_score = accuracy
        with open ("linear_reg.pickle", "wb") as f:
            pickle.dump(linear, f)

pickle_in = open("linear_reg.pickle", "rb")

linear = pickle.load(pickle_in)

print("Coefficients:\n" , linear.coef_)
print("Intercept:\n", linear.intercept_)

preds = linear.predict(x_test)

for x in range(len(preds)):
    print(preds[x],x_test[x],y_test[x])

print("Final accuracy is: {:0.2f}".format(accuracy))

style.use("ggplot")
pyplot.scatter(data["G1"],data["G3"])
pyplot.xlabel("1st Midterm Grade")
pyplot.ylabel("Final Grade")
pyplot.show()

