import math

class Torus():
    def __init__(self, _R: int, _r: int) -> None:
        self.R = _R
        self.r = _r
        self.obj = 2 * math.pi**2 * self.R * self.r**2
    
    def info(self):
        print(f"Promień większego okręgu - {self.R}")
        print(f"Promień rury torusa - {self.r}")
        print(f"Objętość torusa - {self.obj}")

    def zmien_parametry(self, R, r):
        self.R = R
        self.r = r
        self.obj = 2 * math.pi**2 * self.R * self.r**2

torus1 = Torus(5, 2)
torus1.info()
torus1.zmien_parametry(8, 3)
torus1.info()

torus2 = Torus(3, 1)
torus2.info()
