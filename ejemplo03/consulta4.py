from clases import Curso
from config import cadena_base_datos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

cursos = session.query(Curso).all()

print("Cursos y sus tareas asociadas")
for c in cursos:
    print("Curso: %s" % c.titulo)
    for t in c.tareas:
        print("- %s" % t.titulo)
    print("---------")
