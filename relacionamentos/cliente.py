class Cliente:
    def __init__(self, nome, cpf, end=None):
        self._nome = nome
        self._cpf = cpf
        self._endereco = end

    def __str__(self):
        return f'{self._nome} | {self._cpf} | {self._endereco}'
