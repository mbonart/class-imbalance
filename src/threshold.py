import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics
from sklearn.linear_model import LogisticRegression
import numpy as np

# read in the dataset
dat = pd.read_csv("data/creditcardfraud.zip")

# drop unused variables and create a stratified train, validation and test set
y = dat['Class']
dat.drop(['Class', 'Time', 'Amount'], inplace=True, axis=1)


X_train, X_test, y_train, y_test = train_test_split(
    dat, y, test_size=0.2, stratify=y, random_state=10)

# fit the classifier

clf = LogisticRegression(
           solver='lbfgs',
           max_iter=10000
)

clf.fit(X_train, y_train)

# predict probabilities for class 1

est_proba = clf.predict_proba(X_test)[:,1]


# chose a threshold and print the confusion matrix

threshold = 0.5
y_pred = est_proba > 0.5

conf_mat = metrics.confusion_matrix(y_pred, y_test, labels=[1,0])
print(conf_mat)


