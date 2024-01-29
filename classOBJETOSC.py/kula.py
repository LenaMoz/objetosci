import math

class Kula():
    def __init__(self, _r: int) -> None:
        self.r = _r
        self.obj = (4/3) * math.pi * self.r**3
    
    def info(self):
        print(f"Promień - {self.r}")
        print(f"Objetosc - {self.obj}")

    def zmien_r(self, r):
        self.r = r
        self.obj = (4/3) * math.pi * r**3

kula1 = Kula(10)
kula1.zmien_r(100)
kula1.info()

kula2 = Kula(1)
kula2.info()
