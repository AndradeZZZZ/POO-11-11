from abc import ABC, abstractmethod

class Forma(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def area(self) -> float:
        """"Método deve ser reescrito pela classe filha"""
        pass


class Retangulo(Forma):
    def __init__(self, altura:float, largura:float) -> None:
        super().__init__()
        self.__largura = largura
        self.__altura = altura

    def area(self) -> float:
        return self.__largura * self.__altura


class Circulo(Forma):
    def __init__(self, raio:float) -> None:
        super().__init__()
        self.__raio = raio

    def area(self) -> float:
        import math
        return math.pi * self.__raio ** 2


bobEsponja = Retangulo(2, 3)
print(bobEsponja.area())

print("--------")

bola = Circulo(180)
print(bola.area())

print("--------")

naoPode = Forma()
print(naoPode.area())