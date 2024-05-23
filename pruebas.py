import unittest
import json
import os

from libreria import Libreria  # Importar la clase Libreria del archivo correspondiente


class TestLibreria(unittest.TestCase):
    def setUp(self):
        """Configura una nueva instancia de Libreria antes de cada prueba."""
        self.libreria = Libreria()

    def test_anadir_libro(self):
        """Prueba la adición de un libro a la librería."""
        resultado = self.libreria.anadir_libro(
            "Cien años de soledad", 
            "Gabriel García Márquez", 
            "Novela", 
            1967
        )
        self.assertEqual(resultado, "Libro añadido")
        self.assertEqual(len(self.libreria.libros), 1)
        self.assertEqual(self.libreria.libros[0]['titulo'], "Cien años de soledad")


    def test_buscar_libro(self):
        """Prueba la búsqueda de un libro por título."""
        self.libreria.anadir_libro(
            "Cien años de soledad", 
            "Gabriel García Márquez", 
            "Novela", 
            1967
        )
        resultado = self.libreria.buscar_libro("Cien años de soledad")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]['titulo'], "Cien años de soledad")

    def test_buscar_libro_no_existente(self):
        """Prueba la búsqueda de un libro que no existe."""
        resultado = self.libreria.buscar_libro("Libro inexistente")
        self.assertEqual(len(resultado), 0)

    def test_buscar_por_autor(self):
        """Prueba la búsqueda de libros por autor."""
        self.libreria.anadir_libro(
            "Cien años de soledad", 
            "Gabriel García Márquez", 
            "Novela", 
            1967
        )
        self.libreria.anadir_libro(
            "El otoño del patriarca", 
            "Gabriel García Márquez", 
            "Novela", 
            1975
        )
        resultado = self.libreria.buscar_por_autor("Gabriel García Márquez")
        self.assertEqual(len(resultado), 2)

    def test_buscar_por_autor_no_existente(self):
        """Prueba la búsqueda de libros por un autor que no existe."""
        resultado = self.libreria.buscar_por_autor("Autor inexistente")
        self.assertEqual(len(resultado), 0)

    def test_eliminar_libro(self):
        """Prueba la eliminación de un libro por título."""
        self.libreria.anadir_libro(
            "Cien años de soledad", 
            "Gabriel García Márquez", 
            "Novela", 
            1967
        )
        resultado = self.libreria.eliminar_libro("Cien años de soledad")
        self.assertEqual(resultado, "Libro eliminado")
        self.assertEqual(len(self.libreria.libros), 0)

        resultado_no_encontrado = self.libreria.eliminar_libro("Libro inexistente")
        self.assertEqual(resultado_no_encontrado, "Libro no encontrado")

    def test_guardar_libros(self):
        """Prueba la funcionalidad de guardar libros en un archivo JSON."""
        self.libreria.anadir_libro(
            "Cien años de soledad", 
            "Gabriel García Márquez", 
            "Novela", 
            1967
        )
        archivo = 'test_libreria.json'
        resultado = self.libreria.guardar_libros(archivo)
        self.assertEqual(resultado, "Libros guardados")
        
        with open(archivo, 'r') as f:
            libros = json.load(f)
        self.assertEqual(len(libros), 1)
        self.assertEqual(libros[0]['titulo'], "Cien años de soledad")
        
        os.remove(archivo)  # Limpiar archivo de prueba

    def test_cargar_libros(self):
        """Prueba la funcionalidad de cargar libros desde un archivo JSON."""
        archivo = 'test_libreria.json'
        libros = [{
            'titulo': "Cien años de soledad",
            'autor': "Gabriel García Márquez",
            'genero': "Novela",
            'anio': 1967
        }]
        with open(archivo, 'w') as f:
            json.dump(libros, f)
        
        resultado = self.libreria.cargar_libros(archivo)
        self.assertEqual(resultado, "Libros cargados")
        self.assertEqual(len(self.libreria.libros), 1)
        self.assertEqual(self.libreria.libros[0]['titulo'], "Cien años de soledad")
        
        os.remove(archivo)  # Limpiar archivo de prueba

    def test_cargar_libros_archivo_no_encontrado(self):
        """Prueba la carga de libros desde un archivo inexistente."""
        resultado = self.libreria.cargar_libros('archivo_inexistente.json')
        self.assertEqual(resultado, "Archivo no encontrado")


if __name__ == '__main__':
    unittest.main()