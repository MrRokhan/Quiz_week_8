import sqlite3
condb = sqlite3.connect('climate.db')
cs = condb.cursor()

cs.execute("SELECT * FROM ClimateData")

dataset = cs.fetchall()
print("Table: ClimateData")

for row in dataset:
    year, co2, temperature = row
    print(f"Year CO2 Temperature")
    print(f"{year} {co2} {temperature}")
condb.close()

