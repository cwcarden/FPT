import sqlite3
from fpdf import FPDF

#By Area 4 query
def fp_area4_data():
    conn = sqlite3.connect('prodplan.db')
    c = conn.cursor()
    c.execute('SELECT id, area, hybrid, grower, field_name, certified, field_number, cont_gross_acres, percent_target, female_plant_population, hybrid_code, material_group FROM Seedfield')
    data = c.fetchall()
    for field in data:
        if field[1] == 4:
            print(field)
    conn.close()

#By Area 5 query
def fp_area5_data():
    conn = sqlite3.connect('prodplan.db')
    c = conn.cursor()
    c.execute('SELECT id, area, hybrid, grower, field_name, certified, field_number, cont_gross_acres, percent_target, female_plant_population, hybrid_code, material_group FROM Seedfield')
    data = c.fetchall()
    for field in data:
        if field[1] == 5:
            print(field)
    conn.close()

#By Area 7 query
def fp_area7_data():
    conn = sqlite3.connect('prodplan.db')
    c = conn.cursor()
    c.execute('SELECT id, area, hybrid, grower, field_name, certified, field_number, cont_gross_acres, percent_target, female_plant_population, hybrid_code, material_group FROM Seedfield')
    data = c.fetchall()
    for field in data:
        if field[1] == 7:
            print(field)
    conn.close()

#By Area 8 query
def fp_area8_data():
    conn = sqlite3.connect('prodplan.db')
    c = conn.cursor()
    c.execute('SELECT id, area, hybrid, grower, field_name, certified, field_number, cont_gross_acres, percent_target, female_plant_population, hybrid_code, material_group FROM Seedfield')
    data = c.fetchall()
    for field in data:
        if field[1] == 8:
            print(field)
    conn.close()

#sort db data by grower
def fp_grower_data():
    conn = sqlite3.connect('prodplan.db')
    c = conn.cursor()
    c.execute('SELECT id, grower, hybrid, field_name, certified, field_number, area, cont_gross_acres, percent_target, female_plant_population, hybrid_code, material_group FROM Seedfield')
    data = c.fetchall()
    conn.close()
    for field in data:
        field_list = []
        field_list.append(field)
        print(field_list)
