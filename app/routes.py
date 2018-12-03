import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy  

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/planning', methods=['GET', 'POST'])
def planning():
    if request.method == 'POST':
        result = request.form
        print(result)  
        return render_template('planning.html')
    elif request.method == 'GET':
        return render_template('planning.html')

@app.route('/prod_budget', methods=['GET', 'POST'])
def prod_budget():
    if request.method == 'POST':
        result = request.form 
        print(result) 
        return render_template('prod_budget.html')
    elif request.method == 'GET':
        return render_template('prod_budget.html')

@app.route('/prod_reports')
def prod_report():
    return render_template('prod_reports.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
