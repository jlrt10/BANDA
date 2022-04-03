from logica.instrumento import Instrumento

class Guitarra(Instrumento):
    def tocar(self):
        print("Tocando la guitarra")

    def afinar(self):
        print("Afinando la guitarra")