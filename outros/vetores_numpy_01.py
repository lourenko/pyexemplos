#===============================
# Alguns testes utilizando a biblioteca
# Numpy.
# 02/09/2022
# Métodos numéricos para ciências térmicas
#===============================

import numpy as np

## Criação de vetores
#
# * Utilizando o método 'array'
# Esse método suporta qualquer seq. na entrada
v1 = np.array([1, 2, 3., 5, 9])#, dtype=np.int16)
print(v1, " é do tipo, ", v1.dtype)

b = 1
texto = "Existem no vetor {} termos maiores que {}"
print(texto.format(len(v1[v1 > b]), b))

# * Utilizando linspace(start, stop, num)
v2 = np.linspace(2, 100, 49)
# Note que sempre respeita os limites
print(v2)

# * Utilizando arange(start, stop, step)
# Assim como range, sempre vai de i até i+n-1
v3 = np.arange(2, 10, 1.5)
# Cuidado com os limites da sequência
print('v3 = ', v3)

print(sum(v3), v3.sum())

# * Utilizando um valor aleatório
v4 = np.random.randint(3, 21, 7)
print("v4 = ", v4)
# print(min(v4), max(v4))
# print(v4.argmin(), v4.argmax())
# mascara1 = 5 < v4
# mascara2 = v4 < 17
# mascara = mascara1 & mascara2
mascara = (5 < v4) & (v4 < 17) # O mesmo das 3 linhas acima
print(np.where(mascara))

# * Utilizando valores (uniformes) predefinidos pelo usuário
v5 = np.zeros(9) #+ 2.34 # Teste com esses valores
v6 = np.ones(9) #* 2.34  # comentados
print(v5, '\n', v6)

n = 4
a1 = np.zeros((n, n))
for i in range(n):
    a1[i,i]=2
print(a1)

