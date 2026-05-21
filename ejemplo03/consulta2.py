from clases import Curso, Instructor
from config import cadena_base_datos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

cursos = (
    session.query(Curso).join(Instructor).filter(Instructor.nombre.like("%Zam%")).all()
)

print("Cursos con profesores que tienen 'Zam' en su nombre")
for c in cursos:
    print("Curso: %s | Profesor: %s" % (c.titulo, c.instructor.nombre))
