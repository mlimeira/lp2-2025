class Quarto:
    def __init__(self, n, h, c):
        self._numero = n
        self._hospedes = h
        self._camas = c
        self._reservado = False
    #Garantir que os quartos sejam reservados se disponíveis
    def reservar_quarto(self):
        if self._reservado:
            print('Quarto indisponível')
        else:
            print('Quarto reservado com sucesso!')
            self._reservado = True

    def liberar_quarto(self):
        self._reservado = False