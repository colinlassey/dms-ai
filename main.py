import random
import sqlite3
import time

cars = ["chevy", "ford", "lexus", "toyota", "honda"]
database = {
    "chevy": {"model": "camaro", "year": 2020},
    "ford": {"model": "mustang", "year": 2021},
    "lexus": {"model": "rx", "year": 2019},
    "toyota": {"model": "corolla", "year": 2018},
    "honda": {"model": "civic", "year": 2022}
}

# Connect to SQLite database
conn = sqlite3.connect('cars.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS cars
             (id INTEGER PRIMARY KEY, make TEXT, model TEXT, year INTEGER, count INTEGER)''')

for i in range(5):
    c.execute(f'''SELECT * FROM cars WHERE id = {i}''')
    if c.fetchone() is None:
        c.execute(f'''INSERT INTO cars (id, make, model, year, count) VALUES
                     ({i}, '{cars[i]}', '{database[cars[i]]['model']}', {database[cars[i]]['year']}, 0)''')
        conn.commit()
    else: 
        pass

while True:
    time.sleep(3)
    random_number = random.randint(1, 5)
    random_car = cars[random_number - 1]
    print(f"Randomly selected car: {random_car}")
    c.execute('''SELECT * FROM cars WHERE make = ?''', (random_car,))
    car_data = c.fetchone()
    print(f"Car data: {car_data}")
    c.execute('''UPDATE cars SET count = count + 1 WHERE make = ?''', (random_car,))
    conn.commit()
    print(f"Updated count for {random_car}: {car_data[4] + 1}")