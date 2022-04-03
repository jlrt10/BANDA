from logica.instrumento import Instrumento

class Bajo(Instrumento):
    def tocar(self):
        print("Tocando el bajo")

    def afinar(self):
        print("Afinando el bajo")