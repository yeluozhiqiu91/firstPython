class Complex:
    def __init__(self, realpart, imagepart):
        self.r = realpart
        self.i = imagepart


x = Complex(2, 3)
print(x.r, x.i)
