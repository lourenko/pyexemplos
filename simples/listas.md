# Como adicionar um elemento à lista

```python
lista = [1, 2]
lista.append(5)
```

- `lista` - Uma lista qualquer
- `append` - adiciona um objeto ao final da lista
- `5` - objeto adicionado como exemplo

## Exemplo: 
```python
inteiros = [1, 2]
inteiros.append(5)
print(inteiros)
```
```
[1, 2, 5]

```

# Como testar se uma lista está vazia (sem objetos)

```python
if lista:
  print("A lista contém elementos!")
else:
  print("A lista está vazia!")
```

- `lista` - nome da lista que desejamos fazer a checagem
- `print("A lista contém elementos!")` - Imprime esse aviso se não estiver vazia

## Exemplo:
```python
lista1 = [1, 2, 3]
lista2 = []

if lista1:
  print("lista1 contém objetos")
else:
  print("lista1 está vazia")

if lista2:
  print("lista2 contém objetos")
else:
  print("lista2 está vazia")
```
```
lista1 contém objetos
lista2 está vazia

```

# Como acessar o endereço de um elemento da lista a partir de seu valor

```python
uma_lista.index('agulha')
```

- `uma_lista` - a lista na qual se procura pelo endereço
- `index(` - returna o endereço do elemento ou o valor -1
- `'agulha'` - valor procurado na lista


## Exemplo:
```python
uma_lista = ['uma', 'agulha', 'no', 'palheiro']
print(uma_lista.index('agulha'))
```
```
1

```

# Como inverter a sequência de uma lista

```python
lista = ['a', 'b', 'c', 'd']
invertida = lista[::-1]
```

- `lista` - A lista a ser retirada a sequência invertida
- `invertida` - uma nova lista com a sequência invertida
- `[::-1]` - inverte a lista com o passo negativo `-1`

## Exemplo:
```python
lista = ['a', 'b', 'c']
invertida = lista[::-1]
print(invertida)
```
```
['c', 'b', 'a']

```

## Palavras-chave adicionais
- espelhamento ou _"de trás para frente"_

# Como ordenar os itens de uma lista

```python
ordenada = sorted(lista)
```

- `lista` - Uma lista de itens
- `ordenada` - A lista com os itens ordenados
- `sorted(` - Função embutida para [ordenar os elementos](https://docs.python.org/3/howto/sorting.html) que retorna a nova lista


## Exemplo:
```python
exemp = [10, 2, 7]
ord = sorted(exemp)
print(ord)
```
```
[2, 7, 10]

```


# Reverter a ordem dos itens em uma lista
## Utilizando a função `reverse()`

```python
lista_a = ["pi", 3.14, 1000]
lista_a.reverse()
```

- .reverse() - Função (ou método) que inverte a ordem dos itens

# Exemplo

```python
lista_a = ["pi", 3.14, 1000]
lista_a.reverse()
```
```bash
[1000, 3.14, "pi"]
```


## Utilizando o recurso de slicing

```python
lista_b = ["pi", 3.14, 1000]
|{|lista_revertida = lista_b[::-1]|}|

print(lista_revertida)
```

- \[::-1\] - Operador de _slicing_, no qual os itens da lista são acessados na forma `[início:término:passo]`. Se o passo for definido como `-1`, o programa vai considerar a seguinte indexação lista_b(do final até o início)


# Exemplo
```python
lista_b = ["pi", 3.14, 1000]
reversa = lista_b[::-1]
print(reversa)
```
```bash
[1000, 3.14, "pi"]
```


# Como embaralhar os itens de uma lista

```python
import random

lista = [1, 2, 3]
random.shuffle(lista)

```

- `import random` - Biblioteca embutida no python para funções aleatórias
- `lista` - Uma lista de itens qualquer (não precisa conter apenas números)
- `random.shuffle` - Função que embaralha itens de uma sequência (a lista é sobrescrita)

## Exemplo:
```python
import random

seq = [1, 2, 3]
random.shuffle(seq)

print(seq)
```
```
[3, 1, 2]

```

# Como unir listas

```python
listas_juntas = [1, 2, 3] + [4, 5, 6]
```

- `listas_juntas` - O resultado das duas listas unidas (pode ser mais de duas)
- `[1, 2, 3]` - primeira lista no exemplo
- `[4, 5, 6]` - segunda lista no exemplo


## Exemplo:
```python
listas = [1, 2, 3] + [4, 5, 6]
print(listas)
```
```
[1, 2, 3, 4, 5, 6]

```


# Como formar uma frase a partir de strings em uma lista?

```python
palavras = ['Olá', 'pessoal', '!']
frase = ' '.join(palavras)
```


## Exemplo:
```python
palavras = ['Olá', 'pessoal', '!']
frase = ' '.join(palavras)
print(frase)
```
```
Olá pessoal !

```


# Como aplicar uma função aos elementos de uma lista de forma eficiente.

```python
resultado = list(map(função, lista_de_itens))
```

- `resultado` - lista na qual são armazenados os valores processados pela função
- `list(` - converte a sequência alterada (um `iterator`) pela função para uma lista
- `função` - função a ser aplicada aos elementos da lista (pode ser outra sequência que não uma lista)
- `lista_de_itens` - auto explicativo
- `map(` - _mapeia_ cada um dos valores a partir da função

## Exemplo:
```python
lista_strings = ["1", "2", "3"]
lista_inteiros = list(map(int, lista_strings)) # int() -> função que transforma um objeto em inteiro
print(lista_inteiros)
```
```
[1, 2, 3]

```

# Como imprimir uma lista sem os colchetes (uma das formas)

```python
lista = ["a", "b", "c"]
print(*lista, sep = ", ")
```
```
a, b, c

```
- lista - Uma lista qualquer como exemplo
- `print(*lista` - `*` é um operador que _explode_ uma sequência em valores discretos.
- sep = ", " - queremos os valores separados por `,` e espaço ` `

