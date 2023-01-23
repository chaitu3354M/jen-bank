# -*- coding: utf-8 -*-
"""model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12mb6eVjYtCUsWN1mycHLYBkTJJ1EAliG

## problem statement

"" for given data building one classification model by using ML algorithm and exatract the pickle file ""
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
import pickle

data = pd.read_csv("BankNote_Authentication.csv")

data.head()

data.isnull().sum()

data.tail()

X = data.drop('class', axis=1)
y = data['class']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

classifier=DecisionTreeClassifier()
classifier.fit(X_train,y_train)

"""## ""by using the pipeline""
"""

from sklearn.pipeline import Pipeline

pipe = Pipeline([
    ('classifier', DecisionTreeClassifier())
])

pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_test)

y_pred

accuracy = accuracy_score(y_test, y_pred)

print('Accuracy', accuracy)

print(acc)

pickle_out = open("classifier.pkl","wb")
pickle.dump(, pickle_out)
pickle_out.close()



"""### ""without pipeline""
"""

y_pred=classifier.predict(X_test)

from sklearn.metrics import accuracy_score
acc=accuracy_score(y_test,y_pred)

print(acc)

pickle_out = open("classifier.pkl","wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()

classifier.predict([[2,3,4,1]])





