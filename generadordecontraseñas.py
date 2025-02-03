import random
import string

def generar_contraseña(longitud=12):
    # Definir los caracteres que se pueden usar en la contraseña
    letras = string.ascii_letters  # Letras mayúsculas y minúsculas
    numeros = string.digits        # Números del 0 al 9
    signos = string.punctuation    # Signos de puntuación

    # Asegurarse de que la contraseña incluya al menos un número y un signo
    contraseña = [
        random.choice(letras),  # Al menos una letra
        random.choice(numeros), # Al menos un número
        random.choice(signos)   # Al menos un signo de puntuación
    ]

    # Completar el resto de la contraseña con caracteres aleatorios
    todos_los_caracteres = letras + numeros + signos
    for _ in range(longitud - 3):  # Restamos 3 porque ya hemos añadido 3 caracteres
        contraseña.append(random.choice(todos_los_caracteres))

    # Mezclar la lista para que los caracteres no estén en un orden predecible
    random.shuffle(contraseña)

    # Convertir la lista en una cadena
    return ''.join(contraseña)

# Ejemplo de uso
longitud_contraseña = 16  # Puedes cambiar la longitud de la contraseña
contraseña_generada = generar_contraseña(longitud_contraseña)
print("Contraseña generada:", contraseña_generada)