# Apertura de un archivo en modo escritura
# Este código crea un archivo llamado "archivo.txt" y escribe algunas líneas en él.
# Si el archivo ya existe, se sobrescribirá su contenido.

""" with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, mundo!\n")
    archivo.write("Este es un archivo de texto.\n") """

# El archivo se cierra automáticamente al salir del bloque with

# Apertura de un archivo en modo lectura
# Este código lee el contenido del archivo "archivo.txt" y lo imprime en la consola.

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="UTF-8") as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
# Llamada a la función para leer el archivo
leer_archivo("archivo.txt")


