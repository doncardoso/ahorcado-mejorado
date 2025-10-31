#para poder usar choice
import random

# parte inicial del juego
class Mijuego:
    def __init__(self, palabra, vidas=6):
        self.palabra = palabra.lower()
        self.vidas = vidas
        self.correcta = set()
        self.incorrecta = set()
        self.letras_correctas = set(self.palabra)

#como no tiene graficos solo podemos mostrar los espacios de las letras
    def tablero_juego(self):
        return ' '.join([ l if l in self.correcta else '_' for l in self.palabra ])

#buscar la letra
    def adivinar(self,letra):
        letra = letra.lower()
        if letra in self.palabra:
            self.correcta.add(letra)
            return True
        else:
            self.incorrecta.add(letra)
            self.vidas -= 1
            return False

    def ganar(self ):
        return self.letras_correctas.issubset(self.correcta)

    def perder(self):
        return self.vidas <= 0

    def estado(self):
        print("\n la palabra: ",self.tablero_juego())
        print("letras incorectas:", ', '.join(sorted(self.incorrecta)))
        print("vidas: ", self.vidas)

# Listas de palabras por nivel
palabras_facil = ["casa", "perro", "mesa", "sol", "flor", "agua", "gato", "luna", "silla", "árbol"]
palabras_medio = ["ventana", "montaña", "zapato", "naranja", "estrella", "camino", "reloj", "sombrero", "escuela", "cuchara"]
palabras_dificil = ["murciélago", "arquitectura", "psicología", "terremoto", "laberinto", "astronauta", "biblioteca", "electricidad", "fotografía", "marioneta"]


# seleccion de nivel
def seleccionar_dificultad():
    print("\n=== Juego de Ahorcado ===")
    print("Selecciona el nivel de dificultad:")
    print("1. Fácil")
    print("2. Medio")
    print("3. Difícil")
    print("4. Salir")


#permite seleccionar el nivel
    while True:
        opcion = input("Opción (1-4): ")
        if opcion == "1":
            return random.choice(palabras_facil), "Fácil"
        elif opcion == "2":
            return random.choice(palabras_medio), "Medio"
        elif opcion == "3":
            return random.choice(palabras_dificil), "Difícil"
        elif opcion == "4":
            print("¡Gracias por jugar!")
            exit()
        else:
            print("Opción inválida. Intenta de nuevo.")


# aqui comiensa el juego

def juego():
    palabra , nivel = seleccionar_dificultad()
    mijuego = Mijuego(palabra)
    print(f'nivel: {nivel} suerte')

# se repite asta que se alla ganado o perdido
    while not mijuego.ganar() and not mijuego.perder():
        mijuego.estado()
        letra = input("Ingrese la letra: ").strip().lower()

        if len(letra) != 1 or not letra.isalpha():
            print('Ingresa una letra: ')
            continue

        if letra.lower() in mijuego.correcta or letra.lower() in mijuego.incorrecta:
            print('ys ongreso esa letra: ')
            continue

        if mijuego.adivinar(letra):
            print("vas bien")
        else:
            print("fallaste")

    mijuego.estado()
    if mijuego.ganar():
        print(f"\n🎉 ¡Felicidades! Adivinaste la palabra: {mijuego.palabra}")
    else:
        print(f"\n💀 Has perdido. La palabra era: {mijuego.palabra}")
# Bucle principal
while True:
    juego()
    otra = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
    if otra != 's':
        print("¡Hasta la próxima!")
        break
