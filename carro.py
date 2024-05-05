from enum import Enum
import unittest


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


class Asiento:
    def __init__(self, material, con_funda):
        self.material = material
        self.con_funda = con_funda

    def to_string(self):
        return f"Asiento - Material: {self.material}, {'Con funda' if self.con_funda else 'Sin funda'}"


class Carro:
    def __init__(
        self,
        motor,
        chasis,
        carroceria,
        llantas,
        asientos,
        airbags,
        frenos_abs,
        vidrios_electricos,
        espejos_electricos,
        sunroof,
    ):
        self.motor = motor
        self.chasis = chasis
        self.carroceria = carroceria
        self.llantas = llantas
        self.asientos = asientos
        self.airbags = airbags
        self.frenos_abs = frenos_abs
        self.vidrios_electricos = vidrios_electricos
        self.espejos_electricos = espejos_electricos
        self.sunroof = sunroof

    def to_string(self):
        result = [
            self.motor.to_string(),
            self.chasis.to_string(),
            self.carroceria.to_string(),
            *[llanta.to_string() for llanta in self.llantas],
            *[asiento.to_string() for asiento in self.asientos],
            f"Airbags: {'Sí' if self.airbags else 'No'}",
            f"Frenos ABS: {'Sí' if self.frenos_abs else 'No'}",
            f"Vidrios eléctricos: {'Sí' if self.vidrios_electricos else 'No'}",
            f"Espejos eléctricos: {'Sí' if self.espejos_electricos else 'No'}",
            f"Sunroof: {'Sí' if self.sunroof else 'No'}",
        ]
        return "\n".join(result)



def main():
    motor = Motor(2)
    chasis = Chasis(ChasisTipo.Monocasco)
    carroceria = Carroceria("rojo", CarroceriaTipo.Tubular)
    llantas = [Llanta("Goodyear", 25, 20, 15) for _ in range(4)]
    asientos = [Asiento("Cuero", True), Asiento("Cuero", True), Asiento("Cuero", False)]
    carro = Carro(
        motor, chasis, carroceria, llantas, asientos, True, True, True, True, True
    )
    print(carro.to_string())


class TestCarro(unittest.TestCase):
    def test_motor(self):
        motor = Motor(2)
        self.assertEqual(motor.to_string(), "Motor - Volumen: 2 litros")


if __name__ == "__main__":
    main()
    unittest.main()
