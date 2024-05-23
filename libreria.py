import json


class Libreria:
    """Clase que representa una librería que maneja una colección de libros."""

    def __init__(self):
        """Inicializa una nueva instancia de la clase Libreria."""
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        """
        Añade un libro a la colección.

        Devuelve un mensaje indicando que el libro fue añadido.
        """
        self.libros.append({
            'titulo': titulo,
            'autor': autor,
            'genero': genero,
            'anio': anio
        })
        return "Libro añadido"

    def buscar_libro(self, titulo):
        """
        Busca un libro por su título.

        Se pasa por parametro el título del libro a buscar.

        Devuelve una lista de libros que coinciden con el título.
        """
        return [
            libro for libro in self.libros 
            if libro['titulo'].lower() == titulo.lower()
        ]

    def buscar_por_autor(self, autor):
        """
        Busca libros por el autor.

        Se pasa por parametro el autor de los libros a buscar.

        Devuelve una lista de libros que coinciden con el autor.
        """
        return [
            libro for libro in self.libros 
            if autor.lower() in libro['autor'].lower()
        ]

    def eliminar_libro(self, titulo):
        """
        Elimina un libro por su título.

        Se pasa por parametro el título del libro a eliminar.

        Devuelve un mensaje indicando si el libro fue eliminado o no encontrado.
        """
        original_count = len(self.libros)
        self.libros = [
            libro for libro in self.libros 
            if libro['titulo'].lower() != titulo.lower()
        ]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"

    def guardar_libros(self, archivo):
        """
        Guarda la colección de libros en un archivo JSON.

        Se pasa por parametro el nombre del archivo donde se guardarán los libros.

        Devuelve un mensaje indicando que los libros fueron guardados.
        """
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
        """
        Carga la colección de libros desde un archivo JSON.

        Se pasa por parametro el nombre del archivo desde el cual se cargarán los libros.

        Devuelve un mensaje indicando que los libros fueron cargados o que el archivo no fue encontrado.
        """
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"


# Ejemplo de uso
mi_libreria = Libreria()
mi_libreria.anadir_libro(
    "Cien años de soledad", 
    "Gabriel García Márquez", 
    "Novela", 
    1967
)
mi_libreria.guardar_libros('libreria.json')
print(mi_libreria.cargar_libros('libreria.json'))
print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))