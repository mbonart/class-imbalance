import pandas as pd
import plotly.offline
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import sklearn.metrics as metrics


dat = pd.read_csv("data/creditcardfraud.zip")
y = dat['Class']
dat.drop(['Class', 'Time', 'Amount'], inplace=True, axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    dat, y, 
    test_size=0.3, 
    stratify=y,
    random_state=10
)

clfs = [
    LogisticRegression(
           solver='lbfgs',
           max_iter=10000,
           class_weight='balanced'
    ),
    LogisticRegression(
        solver='lbfgs',
        max_iter=10000
    )
]

fig = go.Figure()
names = ['balanced class weights', 'no weighting']

for idx, clf in enumerate(clfs):
    clf.fit(X_train, y_train)
    scores = clf.predict_proba(X_test)
    prec, rec, thresholds = metrics.precision_recall_curve(y_test, scores[:,1])
    fig.add_trace(go.Scatter(
        x=prec, y=rec, 
        name=names[idx],
        mode='lines',
        text=[f"Treshold: {t}" for t in thresholds]))

fig.update_layout(
    title='Precision-recall curve for LR - Credit Card Fraud',
    xaxis_title='Precision',
    yaxis_title='Recall',
    template='presentation+plotly_dark')

plotly.offline.plot(fig, filename='docs/www/precision-recall-curve.html') 
