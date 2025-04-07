import csv
import unicodedata

def normalizar_texto(texto):
    texto = ''.join(
        c for c in unicodedata.normalize('NFKD', texto.lower()) if not unicodedata.combining(c)
    )
    if texto.endswith("s"):  # Eliminar plurales básicos
        texto = texto[:-1]
    return texto

def convertir_puntuacion(puntuacion):
    return float(puntuacion.replace(",", "."))  # Reemplazar coma por punto

class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = normalizar_texto(genero)
        self.puntuacion = convertir_puntuacion(puntuacion)

lista_libros = [
    Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", "4.5"),
    Libro("1984", "George Orwell", "Ciencia Ficción", "4.3"),
    Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", "4.7"),
    Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", "4.2"),
    Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", "4.4"),
    Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", "4.1"),
    Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", "4.6"),
    Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", "4.8"),
    Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", "4.4"),
    Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", "4.0")
]

def agregar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = normalizar_texto(input("Ingrese el género del libro: "))
    puntuacion = input("Ingrese la puntuación del libro: ")
    lista_libros.append(Libro(titulo, autor, genero, puntuacion))
    print("Libro agregado exitosamente.\n")

def buscar_por_genero():
    genero = normalizar_texto(input("Ingrese el género que desea buscar: "))
    encontrados = [libro.titulo for libro in lista_libros if libro.genero == genero]
    if encontrados:
        print("Libros encontrados:")
        for titulo in encontrados:
            print(f"- {titulo}")
    else:
        print("No se encontraron libros en ese género, intente con otro genero si es que lo desea.")
    print()

def recomendar_libro():
    genero = normalizar_texto(input("Ingrese su género de interés: "))
    libros_genero = [libro for libro in lista_libros if libro.genero == genero]
    if libros_genero:
        mejor_libro = max(libros_genero, key=lambda libro: libro.puntuacion)
        print(f"Te recomendamos: {mejor_libro.titulo} de {mejor_libro.autor} con una puntuación de {mejor_libro.puntuacion}\n")
    else:
        print("No se encontraron libros en ese género.\n")

def cargar_desde_csv(nombre_archivo):
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            next(lector)  # Omitir encabezado
            for fila in lector:
                if len(fila) == 4:
                    lista_libros.append(Libro(fila[0], fila[1], fila[2], fila[3]))
        print("Libros cargados exitosamente desde el archivo.\n")
    except FileNotFoundError:
        print("No se encontró el archivo CSV.\n")

def menu():
    while True:
        print("Sistema de Recomendación de Libros")
        print("1. Agregar libro")
        print("2. Buscar libros por género")
        print("3. Recomendar libro")
        print("4. Cargar libros desde CSV")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            buscar_por_genero()
        elif opcion == "3":
            recomendar_libro()
        elif opcion == "4":
            nombre_archivo = input("Ingrese el nombre del archivo CSV: ")
            cargar_desde_csv(nombre_archivo)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.\n")

if __name__ == "__main__":
    menu()