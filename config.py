import sqlite3

conn = sqlite3.connect('prodplan.db')
print("Opened database successfully")

conn.execute('CREATE TABLE fields (hybrid TEXT, grower TEXT, field_name TEXT, certified TEXT, field_number INTEGER, area INTEGER, cont_gross_acres INTEGER, percent_target INTEGER, female_plan_acres INTEGER, hybrid_code TEXT, material_group TEXT)')
print("Table created successfully")
conn.close()
