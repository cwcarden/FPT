import sqlite3
from fpdf import FPDF

#connect to db
conn = sqlite3.connect('prodplan.db')
c = conn.cursor()
c.execute('SELECT id, hybrid, grower, field_name, certified, field_number, area, cont_gross_acres, percent_target, female_plant_population, hybrid_code, material_group FROM Seedfield')
data = c.fetchall()
conn.close()

#sort db data by growing area
def fp_all_data():
    print(data)
    for field in data:
        return field

def fp_area4_data():
    for field in data:
        if field[6] == 4:
            print(field)
        
def fp_area5_data():
    for field in data:
        if field[6] == 5:
            print(field)

def fp_area7_data():
    for field in data:
        if field[6] == 7:
            print(field)

def fp_area8_data():
    for field in data:
        if field[6] == 8:
            print(field)

#sort db data by grower
def fp_grower_data():
    for field in data:
        growers = (field[2])
        grower_list = []
        grower_list.append(growers)
