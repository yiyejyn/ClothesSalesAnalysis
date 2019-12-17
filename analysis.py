from flask import Flask, escape, request, render_template
import random
from bs4 import BeautifulSoup
import requests
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
    col1 = request.args.get('col1')
    col2 = request.args.get('col2')
    col3 = request.args.get('col3')
    col4 = request.args.get('col4')
    col5 = request.args.get('col5')
    return render_template('result.html', col1=col1, col2=col2, col3=col3, col4=col4, col5=col5)

if __name__ == '__main__':
    app.run(debug=True)