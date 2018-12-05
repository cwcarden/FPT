import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy 
import sqlite3 

app = Flask(__name__)
db = SQLAlchemy(app)

class Fields(db.Model):
    hybrid = db.Column(db.Text(80), primary_key=True, nullable=False)
    grower = db.Column(db.Text(80), primary_key=True, nullable=False)
    field_name = db.Column(db.Text(80), primary_key=True, nullable=False)
    certified = db.Column(db.Text(80), primary_key=True, nullable=False)
    field_number = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.Integer, primary_key=True, nullable=False)
    cont_gross_acres = db.Column(db.Integer, primary_key=True, nullable=False)
    percent_target = db.Column(db.Integer, primary_key=True, nullable=False)
    female_plant_population = db.Column(db.Integer, primary_key=True, nullable=False)
    hybrid_code = db.Column(db.Text, primary_key=True, nullable=False)
    material_group = db.Column(db.Text, primary_key=True, nullable=False)

    def __repr__(self, hybrid, grower, field_name, certified, field_number, area, cont_gross_acres, percent_target, female_plant_population, hybrid_code, material_group):
        self.hybrid = hybrid
        self.grower = grower
        self.field_name = field_name 
        self.certified = certified 
        self.field_number = field_number
        self.area = area
        self.cont_gross_acres 
        self.percent_target = percent_target
        self.female_plant_population = female_plant_population
        self.hybrid_code = hybrid_code
        self.material_group = material_group

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

@app.route('/plan')
def plan():
    c = sqlite3.connect('prodplan.db')
    c.row_factory = sqlite3.Row  

    c = c.cursor()
    c.execute("SELECT * FROM fields")

    rows = c.fetchone();
    return render_template('plan.html', rows = rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
