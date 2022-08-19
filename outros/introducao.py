#!/usr/bin/env python
# coding: utf-8

# ## Primeira aula de Python
#
# Esta é uma célula tipo Markdown
#
# Elementos básicos:
# * Containers:
#  - Listas;
#  - Dicionários;
#  - Tuplas;
#  - Conjuntos;
# * Tipos;
#  - Strings;
#  - Int;
#  - Float;
# * Funções;
# * Classes;

# Tipos de dados
palavra = "Aleatório " + ' "ou" ' + """não
!""" # Uma string pode ser definida entre "", '', """"""
print(palavra + " ==> é uma string.\n")
print(end='')

a = 10 # Inteiros são definidos por um número sem .
print(a + 12, type(a + 12), " é um inteiro", end="T \n\n")

b = 3.14159268
print(f"pi = {b:e}" + ' ou ' + "pi = {:4.2f} é um float".format(b))

# Containers
l = ["a", 2, ['a', 3]] # Lista
l[2] = (8, 9, 14)
print(l[2][1])

# Dicionários
d = {2:"pi", 3.14:2, "a":1252}
print(d[d[3.14]])

# Set
s = {3.14, "a", 8, (6,5), 8}
print(s)

# Tuplas
t = ('a', 1, 3.14)
print(t[0])

# Funções
def soma(a, b=9):
    """
    Retorna a soma dos parâmetros
    a: Inteirno (entrada)
    b: Float
    """
    resultado = a + b
    return resultado

print(soma(3, 2))

class Carro:
    ""
    def __init__(self, cor, n_port=3, comb="Diesel"):
        "Método construtor"
        self.cor = cor
        self.portas = n_port
        self.combustivel = comb

    def test(self):
        ""
        return self.cor * self.portas

blue_car = Carro("azul")
red_car = Carro("vermelho")
red_car.portas = 5
print(red_car.test())

help(c1)

print(c1.__dict__)

