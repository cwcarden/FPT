import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)   

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prodplan.db'
SECRET_KEY = '3562f179b152abb7ec44dc4362a87d53bfb62da503675c9b'
db = SQLAlchemy(app)

class Budget(db.Model):
    __tablename__ = 'budget'
    id = db.Column(db.Integer, primary_key=True)
    hybrid = db.Column(db.String(10), nullable=False)
    area = db.Column(db.Integer, nullable=False)
    units_ga = db.Column(db.Integer, nullable=False)
    female_acres = db.Column(db.Integer, nullable=False)
    fifty_lb_units = db.Column(db.Integer, nullable=False)
    female_parent = db.Column(db.String(10), nullable=False)
    male_parent = db.Column(db.String(10), nullable=False)
    gross_acres = db.Column(db.Integer, nullable=False)
    female_seed_kg = db.Column(db.Integer, nullable= False)
    male_seed_kg = db.Column(db.Integer, nullable= False)
    female_unit_50lb = db.Column(db.Integer, nullable= False)
    certified = db.Column(db.String(10), nullable=False)
    percent_female = db.Column(db.Integer, nullable=False)

    def __init__(self, hybrid, area, units_ga, female_acres, fifty_lb_units, female_parent, male_parent, gross_acres, female_seed_kg, male_seed_kg, female_unit_50lb, certified, percent_female):
        self.hybrid = hybrid
        self.area = area
        self.units_ga = units_ga
        self.female_acres = female_acres
        self.fifty_lb_units = fifty_lb_units
        self.female_parent = female_parent
        self.male_parent = male_parent
        self.gross_acres = gross_acres
        self.female_seed_kg = female_seed_kg
        self.male_seed_kg = male_seed_kg
        self.female_unit_50lb = female_unit_50lb
        self.certified = certified
        self.percent_female = percent_female


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

###############################################################################
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

@app.route('/delete', methods=['POST'])
def delete_data():
    row_id = request.form['row_id']
    print(row_id)
    Seedfield.query.filter(Seedfield.id == row_id).delete()
    db.session.commit()
    return redirect(url_for('field_plan'))

###############################################################################
###############################################################################

#Start Sorghum Acreage Plan
@app.route('/prod_budget', methods=['GET', 'POST'])
def prod_budget():
    acrePlan = Budget.query.all()
    return render_template('prod_budget.html', acrePlan=acrePlan, title='Budget Plan')

@app.route('/post_budget_data', methods=['POST'])
def post_budget_data():
    plan = Budget(request.form['hybrid'], request.form['area'], request.form['units_ga'], request.form['female_acres'],request.form['fifty_lb_units'], request.form['female_parent'], request.form['male_parent'], request.form['gross_acres'], request.form['female_seed_kg'], request.form['male_seed_kg'], request.form['female_unit_50lb'], request.form['certified'], request.form['percent_female']) 
    db.session.add(plan)
    db.session.commit()
    return redirect(url_for('prod_budget'))

@app.route('/delete', methods=['POST'])
def delete_budget_data():
    row_id = request.form['row_id']
    print(row_id)
    Budget.query.filter(Budget.id == row_id).delete()
    db.session.commit()
    return redirect(url_for('prod_budget'))
###############################################################################

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)