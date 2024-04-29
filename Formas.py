# Interfaz común para todas las formas
from abc import ABC, abstractmethod


class Forma(ABC):
    @abstractmethod
    def dibujar(self):
        pass


# Implementación concreta para un círculo
class Circulo(Forma):
    def dibujar(self):
        print("Círculo dibujado")


# Implementación concreta para un cuadrado
class Cuadrado(Forma):
    def dibujar(self):
        print("Cuadrado dibujado")


# Clase para dibujar formas
class DibujadorDeFormas:
    def __init__(self, forma):
        self.forma = forma

    def dibujar(self):
        self.forma.dibujar()


# Ejemplo de uso
circulo = Circulo()
cuadrado = Cuadrado()

dibujador_circulo = DibujadorDeFormas(circulo)
dibujador_circulo.dibujar()

dibujador_cuadrado = DibujadorDeFormas(cuadrado)
dibujador_cuadrado.dibujar()
