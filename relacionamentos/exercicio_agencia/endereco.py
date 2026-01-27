class Endereco:
    def __init__(self, cep, rua, cidade):
        self._cep = cep
        self._rua = rua
        self._cidade = cidade

    def __str__(self):
        return f'{self._cep}, {self._rua}, {self._cidade} '
