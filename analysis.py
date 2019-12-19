# 전현진, 이예진, 오민재 시작

from flask import Flask, escape, request, render_template
import random
from bs4 import BeautifulSoup
import requests
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
import pandas as pd
import numpy as np


app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/result')
def result():
    POPULARITY = int(request.args.get('POPULARITY'))
    BUCKET = int(request.args.get('BUCKET'))
    TOTAL_SELL = int(request.args.get('TOTAL_SELL'))
    LIKE_ = int(request.args.get('LIKE_'))
    REVIEW = int(request.args.get('REVIEW'))
    PRICE = int(request.args.get('PRICE'))
    df_train = pd.read_csv("df_train.csv")

    y_label = df_train['FIRST_PAGE']
    df_train = df_train.drop(['Unnamed: 0','FIRST_PAGE'] , axis = 1)
    df_train.to_csv("test")

    X_train , X_test , y_train , y_test =train_test_split(df_train , y_label, random_state = 156) 

    dt_clf = DecisionTreeClassifier()

    dt_clf = dt_clf.fit(X_train,y_train)
    dt_prediction = dt_clf.predict(X_test)

    confusion_matrix(y_test , dt_prediction, labels=[1,0])

    accuracy = accuracy_score(y_test , dt_prediction)
    print("정확도",accuracy)

    new_data01 = np.array([[POPULARITY , BUCKET, TOTAL_SELL, LIKE_,REVIEW,PRICE]])
    plus_ = dt_clf.predict(new_data01)
    if plus_[0] == 1:
        plus = "상위 페이지에 등록되기에 충분합니다!!"
    else:
        plus = "상위 페이지에 등록되기엔 부족합니다."
    return render_template('result.html', POPULARITY=POPULARITY, BUCKET=BUCKET, TOTAL_SELL=TOTAL_SELL, LIKE_=LIKE_, REVIEW=REVIEW, PRICE=PRICE, plus=plus)

if __name__ == '__main__':
    app.run(debug=True)

    # 전현진, 이예진, 오민재 끝