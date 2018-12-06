import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)   

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/prodplan'
db = SQLAlchemy(app)

class Fields(db.Model):
    hybrid = db.Column(db.String(80), primary_key=True)
    grower = db.Column(db.String(80), primary_key=True)
    field_name = db.Column(db.String(80), unique=True)
    certified = db.Column(db.String(80), primary_key=True)
    field_number = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.Integer, primary_key=True)
    cont_gross_acres = db.Column(db.Integer, primary_key=True)
    percent_target = db.Column(db.Integer, primary_key=True)
    female_plant_population = db.Column(db.Integer, primary_key=True)
    hybrid_code = db.Column(db.String(80), primary_key=True)
    material_group = db.Column(db.String(80), primary_key=True)

    def __init__(self, hybrid, grower, field_name, certified, field_number, area, cont_gross_acres, percent_target, female_plant_population, hybrid_code, material_group):
        self.hybrid = hybrid
        self.grower = grower
        self.field_name = field_name 
        self.certified = certified 
        self.field_number = field_number
        self.area = area
        self.cont_gross_acres = cont_gross_acres
        self.percent_target = percent_target
        self.female_plant_population = female_plant_population
        self.hybrid_code = hybrid_code
        self.material_group = material_group
    
    def __repr__(self):
        return '<Fields %r>' % self.field_name

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/field_plan')
def field_plan():
    return render_template('field_plan.html')

@app.route('/post_data', methods=['POST'])
def post_data():
    fields = Fields(request.form['hybrid'], request.form['grower'], request.form['field_name'], request.form['certified'],request.form['field_number'], request.form['area'],request.form['cont_gross_acres'], request.form['percent_target'], request.form['female_plant_population'], request.form['hybrid_code'], request.form['material_group']) 
    db.session.add(fields)
    db.session.commit()
    return redirect(url_for('field_plan'))

@app.route('/prod_budget', methods=['GET', 'POST'])
def prod_budget():
    if request.method == 'POST':
        result = request.form 
        print(result) 
        return render_template('prod_budget.html')
    elif request.method == 'GET':
        return render_template('prod_budget.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
