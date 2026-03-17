class Sistema:
    def logar(self, autenticavel):
        try:
            return autenticavel.autenticar('1234')
        except Exception as e:
            print(e)