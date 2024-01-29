import math

class GraniastoslupTrojkatny():
    def __init__(self, _a: int, _h: int) -> None:
        self.a = _a
        self.h = _h
        self.pole_podstawy = (math.sqrt(3)/4) * self.a**2
        self.obj = (1/3) * self.pole_podstawy * self.h
    
    def info(self):
        print(f"Długość boku trójkąta - {self.a}")
        print(f"Wysokość graniastosłupa - {self.h}")
        print(f"Pole podstawy - {self.pole_podstawy}")
        print(f"Objętość graniastosłupa - {self.obj}")

    def zmien_parametry(self, a, h):
        self.a = a
        self.h = h
        self.pole_podstawy = (math.sqrt(3)/4) * self.a**2
        self.obj = (1/3) * self.pole_podstawy * self.h

graniastoslup1 = GraniastoslupTrojkatny(5, 8)
graniastoslup1.info()
graniastoslup1.zmien_parametry(10, 12)
graniastoslup1.info()

graniastoslup2 = GraniastoslupTrojkatny(3, 6)
graniastoslup2.info()
