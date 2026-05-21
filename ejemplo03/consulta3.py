from clases import Curso, Departamento, Inscripcion
from config import cadena_base_datos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

inscripciones = (
    session.query(Inscripcion)
    .join(Inscripcion.curso)
    .join(Curso.departamento)
    .filter(Departamento.nombre == "Ciencias de la Computación")
    .all()
)

print("Inscripciones del departamento de Ciencias de la Computación")
for i in inscripciones:
    print(
        "Estudiante: %s | Curso: %s | Profesor: %s"
        % (i.estudiante.nombre, i.curso.titulo, i.curso.instructor.nombre)
    )
