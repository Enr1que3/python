import sqlite3

miConexcion=sqlite3.connect('EjercicioDB')

cursor=miConexcion.cursor()

cursor.execute("""
    CREATE TABLE Alumnos(
        id INTEGER primary key,
        nombre TEXT,
        apellidoPaterno TEXT,
        apellidoMaterno TEXT
    )
""")

agegarAlumnos=[
    ('1','Mario','Lopez','Flores'),
    ('2','Eduardo','Martinez','Corona'),
    ('3','Luis','Galicia','Melendez'),
    ('4','Raul','Lopez','Ramirez'),
    ('5','Francisco','Juarez','Diaz'),
    ('6','Luis Alberto','Galicia','Flores'),
    ('7','Juan','Torres','Cervantes'),
    ('8','Enrique','Peña','Nieto'),
]

cursor.executemany('INSERT INTO Alumnos VALUES(?,?,?,?)',agegarAlumnos)

miConexcion.commit()

miConexcion.close()