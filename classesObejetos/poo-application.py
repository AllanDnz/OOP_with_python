class Bike:
    def __init__(self, color, model, year, value):
        self.color = color
        self.model = model
        self.year = year
        self.value = value

    def horn(self):
        print("birubilu")

    def stopping(self):
        print("*som onomatopeico de freio*")
    
    def running(self):
        print("raaaaam tchum")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"
    


b1 = Bike("vermelha", "caloi", 2022, 600)
b1.horn()
b1.running()
b1.stopping()
print(b1.color, b1.model, b1.year, b1.value)

b2 = Bike("verde", "monark", 2000, 189)
print(b2)
b2.running()