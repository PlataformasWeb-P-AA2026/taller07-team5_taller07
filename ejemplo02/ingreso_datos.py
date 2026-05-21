from configuracion import cadena_base_datos
from genera_tablas import Club, Jugador
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

archivo_clubs = open("data/datos_clubs.txt", "r", encoding="utf-8")
lineas_clubs = archivo_clubs.readlines()

for lc in lineas_clubs:
    datos = lc.split(";")
    club = Club(nombre=datos[0], deporte=datos[1], fundacion=int(datos[2]))
    session.add(club)

session.commit()
archivo_clubs.close()

archivo_jugadores = open("data/datos_jugadores.txt", "r", encoding="utf-8")
lineas_jugadores = archivo_jugadores.readlines()

for lj in lineas_jugadores:
    datos = lj.strip().split(";")

    if len(datos) == 4:
        nombre_club = datos[0]
        posicion = datos[1]
        dorsal = int(datos[2])
        nombre_jugador = datos[3]

        club_busqueda = session.query(Club).filter_by(nombre=nombre_club).one()

        jugador = Jugador(
            nombre=nombre_jugador, dorsal=dorsal, posicion=posicion, club=club_busqueda
        )
        session.add(jugador)

session.commit()
archivo_jugadores.close()
