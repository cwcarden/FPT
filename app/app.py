import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)   

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prodplan.db'
SECRET_KEY = '3562f179b152abb7ec44dc4362a87d53bfb62da503675c9b'
db = SQLAlchemy(app)

class Seedfield(db.Model):
    __tablename__ = 'seedfield'
    id = db.Column(db.Integer, primary_key=True)
    hybrid = db.Column(db.String(80), nullable=False)
    grower = db.Column(db.String(80), nullable=False)
    field_name = db.Column(db.String(80), unique=True, nullable=False)
    certified = db.Column(db.String(80), nullable=False)
    field_number = db.Column(db.Integer, unique=True, nullable=False)
    area = db.Column(db.Integer,  nullable=False)
    cont_gross_acres = db.Column(db.Integer,  nullable=False)
    percent_target = db.Column(db.Integer,  nullable=False)
    female_plant_population = db.Column(db.Integer,  nullable=False)
    hybrid_code = db.Column(db.String(80),  nullable=False)
    material_group = db.Column(db.String(80),  nullable=False)

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
        return '<Field Number %r>' % self.field_number

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/field_plan')
def field_plan():
    dataPlan = Seedfield.query.all()
    return render_template('field_plan.html', dataPlan=dataPlan, title="Field Planning")

@app.route('/post_data', methods=['POST'])
def post_data():
    fields = Seedfield(request.form['hybrid'], request.form['grower'], request.form['field_name'], request.form['certified'], request.form['field_number'], request.form['area'], request.form['cont_gross_acres'], request.form['percent_target'], request.form['female_plant_population'], request.form['hybrid_code'], request.form['material_group']) 
    db.session.add(fields)
    db.session.commit()
    return redirect(url_for('field_plan'))
####################################################################################
@app.route('/delete', methods=['POST'])
def delete_data():
    row_id = request.form['row_id']
    print(row_id)
    Seedfield.query.filter(Seedfield.id == row_id).delete()
    db.session.commit()
    return redirect(url_for('field_plan'))
####################################################################################
@app.route('/update', methods=['POST'])
def update_data():
    db.session.commit()
    return redirect(url_for('field_plan'))

@app.route('/prod_budget', methods=['GET', 'POST'])
def prod_budget():
    return render_template('prod_budget.html', title='Budget Acres')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)