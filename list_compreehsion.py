frase = 'Teste de list-comprehension'
frequencia = {}
for i in frase:
    if i in 'aeiou':
        if i in frequencia.keys():
            frequencia[i] += 1
        else:
            frequencia[i] = 1
fd = {}
fd = {i:frase.count(i) for i in frase if i in 'aeiou'}
print(frequencia)
print(fd)
