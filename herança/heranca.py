class Veiculos: 
    def __init__(self, color, plaque, wheels ):
        self.color = color
        self.plaque = plaque
        self.wheels = wheels


        def start_motor(self):
            print("motor ligado")

        def __str__(self):
            return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"
        

class Motorcycle(Veiculos):
            pass

class Car(Veiculos):
            pass
class Truck(Veiculos):
    def __init__(self, color, plaque, wheels, charger):
        super().__init__(color, plaque, wheels)
        self.charger = charger


    def Is_loaded(self):
        print(f"{'Sim' if self.charger else 'Não'} estou carregado")




moto = Motorcycle("preta", "abc-1234", 2)
carro = Car("branco", "xde-0098", 4)
caminhao = Truck("roxo", "gfd-8712", 8, True)

print(moto)
print(carro)
print(caminhao)