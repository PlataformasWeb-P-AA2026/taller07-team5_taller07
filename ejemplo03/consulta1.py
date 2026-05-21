from clases import Entrega
from config import cadena_base_datos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

entregas = session.query(Entrega).all()

print("Listado de entregas")
for e in entregas:
    print(
        "Estudiante: %s | Título: %s | Profesor: %s"
        % (e.estudiante.nombre, e.tarea.titulo, e.tarea.curso.instructor.nombre)
    )
