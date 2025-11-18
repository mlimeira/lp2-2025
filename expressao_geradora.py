lista = [i for i in range(1,11)]
print(lista)
exp_ger = (i for i in range(1,11))
print(next(exp_ger))
print(next(exp_ger))
for i in exp_ger:
    print(i)
