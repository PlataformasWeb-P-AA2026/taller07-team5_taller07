import csv
from datetime import datetime

from clases import (
    Curso,
    Departamento,
    Entrega,
    Estudiante,
    Inscripcion,
    Instructor,
    Tarea,
)
from config import cadena_base_datos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

with open("01_departamento.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        departamento = Departamento(id=int(fila["id"]), nombre=fila["nombre"])
        session.add(departamento)
    session.commit()

with open("02_instructor.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        instructor = Instructor(id=int(fila["id"]), nombre=fila["nombre"])
        session.add(instructor)
    session.commit()

with open("03_curso.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        departamento = (
            session.query(Departamento).filter_by(id=int(fila["departamento_id"])).one()
        )
        instructor = (
            session.query(Instructor).filter_by(id=int(fila["instructor_id"])).one()
        )

        curso = Curso(
            id=int(fila["id"]),
            titulo=fila["titulo"],
            departamento=departamento,
            instructor=instructor,
        )
        session.add(curso)
    session.commit()

with open("04_estudiante.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        estudiante = Estudiante(id=int(fila["id"]), nombre=fila["nombre"])
        session.add(estudiante)
    session.commit()

with open("05_inscripcion.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        estudiante = (
            session.query(Estudiante).filter_by(id=int(fila["estudiante_id"])).one()
        )
        curso = session.query(Curso).filter_by(id=int(fila["curso_id"])).one()

        inscripcion = Inscripcion(
            estudiante=estudiante,
            curso=curso,
            fecha_inscripcion=datetime.strptime(
                fila["fecha_inscripcion"], "%Y-%m-%d %H:%M:%S"
            ),
        )
        session.add(inscripcion)
    session.commit()

with open("06_tarea.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        curso = session.query(Curso).filter_by(id=int(fila["curso_id"])).one()

        tarea = Tarea(
            id=int(fila["id"]),
            curso=curso,
            titulo=fila["titulo"],
            fecha_entrega=datetime.strptime(fila["fecha_entrega"], "%Y-%m-%d %H:%M:%S"),
        )
        session.add(tarea)
    session.commit()

with open("07_entrega.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        tarea = session.query(Tarea).filter_by(id=int(fila["tarea_id"])).one()
        estudiante = (
            session.query(Estudiante).filter_by(id=int(fila["estudiante_id"])).one()
        )

        entrega = Entrega(
            id=int(fila["id"]),
            tarea=tarea,
            estudiante=estudiante,
            fecha_envio=datetime.strptime(fila["fecha_envio"], "%Y-%m-%d %H:%M:%S"),
            calificacion=float(fila["calificacion"]),
        )
        session.add(entrega)
    session.commit()
