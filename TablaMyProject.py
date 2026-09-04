import sqlite3
import os

ruta = os.path.join(os.path.dirname(__file__),'MedidasSemanales.db')
conexion=sqlite3.connect(ruta)
consulta=conexion.cursor()

medidas = '''CREATE TABLE medidas(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                date TEXT NOT NULL,
                weight REAL NOT NULL,
                waist REAL NOT NULL,
                biceps REAL NOT NULL,
                leg REAL NOT NULL,
                gluteus REAL NOT NULL
                ); '''

print(medidas)
try:
    consulta.execute(medidas)
    print('successful creation')
except sqlite3.Error as e:
    print('Error: ',e)

consulta.close()
conexion.commit()
conexion.close()