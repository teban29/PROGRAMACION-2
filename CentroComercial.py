# Interfaz para el principio de abierto/cerrado
from abc import ABC, abstractmethod


class EstrategiaDescuento(ABC):
    @abstractmethod
    def aplicar_descuento(self, precio):
        pass


# Implementaciones concretas de la estrategia de descuento
class DescuentoRopaNino(EstrategiaDescuento):
    def aplicar_descuento(self, precio):
        # Aplica un descuento específico para ropa de niño
        return precio * 0.8


class DescuentoElectronico(EstrategiaDescuento):
    def aplicar_descuento(self, precio):
        # Aplica un descuento específico para electrónicos
        return precio * 0.4


# Clase CentroComercial que utiliza una estrategia de descuento
class CentroComercial:
    def __init__(self, nombre_tienda, tipo_de_comercio, precio, estrategia_descuento):
        self.nombre_tienda = nombre_tienda
        self.tipo_de_comercio = tipo_de_comercio
        self.precio = precio
        self.estrategia_descuento = estrategia_descuento

    def calcular_precio_final(self):
        return self.estrategia_descuento.aplicar_descuento(self.precio)

    def __str__(self):
        return f"Nombre de la tienda: {self.nombre_tienda}\nTipo de comercio: {self.tipo_de_comercio}\nPrecio final con descuento: {self.calcular_precio_final()}"


if __name__ == "__main__":
    descuento_ropa_nino = DescuentoRopaNino()
    tienda_ropa_nino = CentroComercial(
        "Niños Felices", "Ropa para niños", 100, descuento_ropa_nino
    )
    print(tienda_ropa_nino)
    descuento_electronico = DescuentoElectronico()
    tienda_electronica = CentroComercial(
        "Tecnología Avanzada", "Electrónicos", 500, descuento_electronico
    )
    print(tienda_electronica)
