import sys
import traceback

class ValorNegativoError(Exception):
    pass

while True:
    try:
        y = input('Entre com um valor numérico:')
        d = int(y)
        if d < 0:
            raise ValorNegativoError('Não entrar com valores negativos')
        x = 5 / d
        print(x)
        # break
    except ZeroDivisionError as zde:
        print('Impossível dividir por zero, tente novamente...')
    except ValorNegativoError as vne:
        print(str(vne))
    except ValueError as ve:
        #Imprimindo a mensagem interna da exceção
        print(str(ve))
        #Imprimir a tupla da excecão
        print(sys.exc_info())
        print('Valor inadequado. Tente novamente...')
        #Impressão da mensagem completa da exceção
        traceback.print_exc()
        if y == 'a':
            print(f'Teste da letra {y}')
    except EOFError as eo:
        print('Programa interrompido pelo teclado')
        break
    else:
        print('Deu certo')
        break
    finally:
        try:
            print(f'O valor inserido foi {y}')
        except NameError as ne:
            print('Variável não inicializada')
