import math
class Forma:
    def __init__(self, tipo=None):
        self._tipo = tipo
        
    def area(self):
        return 0

    def perimetro(self):
        return 0

    def __str__(self):
        return f'{self._tipo} Área:{self.area()} Perímetro:{self.perimetro()}'
    
##    def __init__(self, *args):
##        if len(args) == 1:
##            self._tipo = 'Circulo'
##        elif len(args) == 2:
##            self._tipo = 'Quadrilatero'
##        elif len(args) == 3:
##            self._tipo = 'Triangulo'
##        else:
##            self._tipo = 'Forma Genérica'
        
##Subclasses
class Circulo(Forma):
    def __init__(self, raio):
        super().__init__('Circulo')
        self._raio = raio

    ##Métodos substituídos
    def area(self):
        return math.pi * self._raio ** 2

    def perimetro(self):
        return 2 * math.pi * self._raio
        
class Quadrilatero(Forma):
    def __init__(self, base, altura=None):
        if altura == base or altura==None:
            super().__init__('Quadrado')
            self._base = base
            self._altura = base
        else:
            super().__init__('Retângulo')
            self._base = base
            self._altura = altura
    def area(self):
        return self._base * self._altura

    def perimetro(self):
        return 2 * self._base + 2 * self._altura
    
class Triangulo(Forma):
    def __init__(self, a, b, c):
        if a < b+c and b < a+c and c < b+a:
            super().__init__('Triangulo')
            self._a, self._b, self._c = a, b, c
        else:
            raise Exception('Os valores não formam um triângulo')

    def perimetro(self):
        return self._a + self._b + self._c
    
    def area(self):
        s = self.perimetro() / 2
        return math.sqrt(s*(s-self._a)*(s-self._b)*(s-self._c))
        
c1 = Circulo(2)
q1 = Quadrilatero(4)
r1 = Quadrilatero(4,5)
t1 = Triangulo(1,2,3)

formas = [c1, q1, r1, t1]
for f in formas:
    print(f)
