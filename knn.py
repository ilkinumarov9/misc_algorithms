#import tensorflow as tf
import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style
from sklearn import linear_model, preprocessing, neighbors
from sklearn.utils import shuffle

data = pd.read_csv("car.data")

pp = preprocessing.LabelEncoder()
#numpy arrays of df's columns
buying = pp.fit_transform(list(data["buying"]))
maint = pp.fit_transform(list(data["maint"]))
door = pp.fit_transform(list(data["door"]))
persons = pp.fit_transform(list(data["persons"]))
lug_boot = pp.fit_transform(list(data["lug_boot"]))
safety = pp.fit_transform(list(data["safety"]))
clss = pp.fit_transform(list(data["class"]))

predict = "class"
#print(buying) #printing out numeric values respective to words

X = list(zip(buying,maint,door,persons,lug_boot,safety)) #zip creates tuples objects
y = list(clss)

#Splitting training and test datasets

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y,test_size=0.1)

model = sklearn.neighbors.KNeighborsClassifier(n_neighbors=7)

model.fit(x_train,y_train)

acc = model.score(x_test,y_test)

print("Accuracy of our model is {:0.2f}".format(acc))

predicted = model.predict(x_test)
clasify = ["bad","good","very good","perfect"]

for x in range(len(predicted)):
    print("Prediction: ", clasify[predicted[x]])
    print("Attributes of data", x_test[x])
    print("Actual data: ", clasify[y_test[x]])