from PIL import Image
import numpy as np
import os
import math

# Función para cifrar una frase usando el algoritmo de escítala
def cifrar_escitala(frase, num_lineas):
    # Calcular el tamaño de cada fila en la matriz de escítala
    tamano_fila = math.ceil(len(frase) / num_lineas)
    # Crear una matriz vacía con el número de líneas especificado
    matriz = [''] * num_lineas
    
    # Rellenar la matriz con los caracteres de la frase
    for i in range(len(frase)):
        fila = i % num_lineas
        matriz[fila] += frase[i]
        
    # Alinear cada fila de la matriz a la derecha con caracteres de relleno (*)
    for i in range(num_lineas):
        matriz[i] = matriz[i].ljust(tamano_fila, '*')
        
    # Concatenar las filas de la matriz para obtener el mensaje cifrado
    mensaje_cifrado = ''
    for fila in matriz:
        mensaje_cifrado += fila
    
    return mensaje_cifrado

# Función para descifrar un mensaje cifrado usando el algoritmo de escítala
def descifrar_escitala(mensaje_cifrado, num_lineas):
    # Calcular el tamaño de cada fila en la matriz de escítala
    tamano_fila = (len(mensaje_cifrado) + num_lineas - 1) // num_lineas
    # Crear una matriz vacía con el número de líneas especificado
    matriz = [''] * num_lineas
    
    # Rellenar la matriz con los caracteres del mensaje cifrado
    for i in range(num_lineas):
        inicio = i * tamano_fila
        fin = min(inicio + tamano_fila, len(mensaje_cifrado))
        matriz[i] = mensaje_cifrado[inicio:fin]
    
    # Recorrer la matriz en orden de escítala para obtener el mensaje descifrado
    mensaje_descifrado = ''
    
    for i in range(tamano_fila):
        for j in range(num_lineas):
            if i < len(matriz[j]):
                mensaje_descifrado += matriz[j][i]
    
    return mensaje_descifrado

# Solicitar al usuario la frase y el número de líneas para el cifrado
print('A) TEXTO ESCRITO DESDE TECLADO')
frase = input('Ingrese la frase que desea cifrar: ')
num_lineas = int(input('Ingrese el número de líneas: '))

# Cifrar y mostrar el mensaje cifrado
mensaje_cifrado = cifrar_escitala(frase, num_lineas)
print('MENSAJE CIFRADO:', mensaje_cifrado)

# Descifrar y mostrar el mensaje descifrado
mensaje_descifrado = descifrar_escitala(mensaje_cifrado, num_lineas)
print('MENSAJE DESCIFRADO:', mensaje_descifrado)
print('--------------------------------------------------------')

####################################################################

# Imprime la opción de leer texto desde un archivo
print('B) TEXTO CONTENIDO DESDE UN ARCHIVO(archivo debe llamarse "archivo_ascii.txt")')

# Ruta del archivo de entrada
ruta_archivo = os.path.join(os.path.dirname(__file__), 'archivo_ascii.txt')

# Lectura del archivo de entrada
with open(ruta_archivo, 'r') as archivo_entrada:
    texto_original = archivo_entrada.read()

# Solicita al usuario que ingrese el número de líneas
num_lineas = int(input('Ingrese el número de líneas: '))

# Cifra el texto original utilizando la función cifrar_escitala
mensaje_cifrado = cifrar_escitala(texto_original, num_lineas)

# Guarda el mensaje cifrado en un archivo de texto
with open('texto_cifrado.txt', 'w') as archivo_salida_cifrado:
    archivo_salida_cifrado.write(mensaje_cifrado)

# Descifra el mensaje cifrado utilizando la función descifrar_escitala
mensaje_descifrado = descifrar_escitala(mensaje_cifrado, num_lineas)

# Guarda el mensaje descifrado en un archivo de texto
with open('archivo_descifrado.txt', 'w') as archivo_salida_descifrado:
    archivo_salida_descifrado.write(mensaje_descifrado)

# Imprime que el proceso se ha completado correctamente
print('El mensaje cifrado ha sido guardado en el archivo "texto_cifrado.txt" y el mensaje descifrado en el archivo "archivo_descifrado.txt".')


####################################################################

from math import ceil
print('--------------------------------------------------------')
print('C) ARCHIVO DE IMAGEN')

def cifrar(msg, n, file=False):
    # convertir ascii string a bytes
    if type(msg)==str:
        msg = bytes(msg, encoding='ascii')
    n = int(n)
    # longitud para cada fila
    l = int(ceil(len(msg) / float(n)))
    # relleno con  ' ' para hcaerlo multiplo de n
    msg = msg.ljust(l * n, b' ')
    # toma pedazos de l caracteres
    trozos = [msg[i:i+l] for i in range(0,len(msg),l)]
    transposed_codes = _transpose(trozos)
    # toma cada caracter para unirlo
    transposed_msg = list(map(lambda row: bytes(row), transposed_codes))
    msg =  b''.join(transposed_msg)
    # retorna bytes o ascii string
    if file:
        return msg
    return msg.decode(encoding='ascii')

def _transpose(matrix):
    return [bytes([row[i] for row in matrix]) for i in range(len(matrix[0]))]

def descifrar(msg, n, file=False):
    # convertir ascii string a bytes
    n = int(n)
    if type(msg)==str:
        msg = bytes(msg, encoding='ascii')
    # tomar pedazos de n caracteres
    trozos = [msg[i:i+n] for i in range(0, len(msg), n)]
    transposed_codes = _transpose(trozos)
    # tomar cada caracter para unirlo
    transposed_msg = list(map(lambda row: bytes(row), transposed_codes))
    msg = b''.join(transposed_msg)
    # retorna bytes o ascii string
    if file:
        return msg
    return msg.decode(encoding='ascii')

# Reemplaza "imagen.png" con el nombre de tu archivo de imagen
image_name = "imagen.png"

# Construye la ruta del archivo de imagen en la misma carpeta que el script de Python
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, image_name)
# Carga la imagen
image = Image.open(image_path)
image_data = image.tobytes()


# Solicita la clave al usuario
key = int(input("Por favor, ingresa la clave para el cifrado/descifrado de la imagen de nombre 'imagen.png': "))


img = open(image_name,"rb").read()
num_bytes = cifrar(img, key, file=True)

open("imagen_cifrada.png","wb").write(num_bytes)



# Imprime mensajes de éxito para las imágenes cifrada y descifrada
print('Imagen cifrada EXITOSAMENTE en archivo de nombre imagen_cifrada.png')




img = open("imagen_cifrada.png","rb").read()
num_bytes = descifrar(img, key, file=True)

open("imagen_descifrada.png","wb").write(num_bytes)
print('Imagen descifrada EXITOSAMENTE en archivo de nombre imagen_descifrada.png')
print('--------------------------------------------------------')

