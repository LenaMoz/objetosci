class Szecian():
    def __init__(self, _a:int) -> None:
        self.a = _a
        self.obj = self.a**3
    
    def inf(self):
        print(f"a - {self.a}")
        print(f"obj - {self.obj}")

    def zmiena_a(self,a):
        self.a = a
        self.obj = a**3

sz = Szecian(1000000000000000)
sz.inf()
sz.zmiena_a(100)
sz.inf

sz1 = Szecian(1)
