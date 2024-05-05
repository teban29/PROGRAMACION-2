from enum import Enum


class ChasisTipo(Enum):
    Independiente = 1
    Monocasco = 2


class CarroceriaTipo(Enum):
    Independiente = 1
    Autoportante = 2
    Tubular = 3


class Motor:
    def __init__(self, volumen_litros):
        self.volumen_litros = volumen_litros

    def to_string(self):
        return f"Motor - Volumen: {self.volumen_litros} litros"


class Chasis:
    def __init__(self, tipo):
        self.tipo = tipo

    def to_string(self):
        return f"Chasis - Tipo: {self.tipo.name}"


class Carroceria:
    def __init__(self, color, tipo):
        self.color = color
        self.tipo = tipo

    def to_string(self):
        return f"Carrocería - Color: {self.color}, Tipo: {self.tipo.name}"


class Llanta:
    def __init__(self, marca, diametro_rin, altura, anchura):
        self.marca = marca
        self.diametro_rin = diametro_rin
        self.altura = altura
        self.anchura = anchura

    def to_string(self):
        return f"Llanta - Marca: {self.marca}, Rin: {self.diametro_rin}, Altura: {self.altura}, Anchura: {self.anchura}"


class Carro:
    def __init__(self, motor, chasis, carroceria, llantas):
        self.motor = motor
        self.chasis = chasis
        self.carroceria = carroceria
        self.llantas = llantas

    def to_string(self):
        result = [
            self.motor.to_string(),
            self.chasis.to_string(),
            self.carroceria.to_string(),
        ]
        result.extend([llanta.to_string() for llanta in self.llantas])
        return "\n".join(result)


# Método main
def main():
    motor = Motor(2)
    chasis = Chasis(ChasisTipo.Monocasco)
    carroceria = Carroceria("rojo", CarroceriaTipo.Tubular)
    llantas = [Llanta("Goodyear", 25, 20, 15) for _ in range(4)]
    carro = Carro(motor, chasis, carroceria, llantas)

    print(carro.to_string())


if __name__ == "__main__":
    main()
