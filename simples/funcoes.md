# Como terminar (sair) de uma função

```python
def uma_funcao(param):
  if param == 5:
    return 0
    
  # continuação da função
```

- `def uma_funcao` - definição da função
- `if param == 5` - condição para terminar a função
- `return 0` - ponto de término, retornando `0`.

# Como fazer uso de funções lambda

Muito úteis para utilizar sempre que precisar de uma definição compacta de função.

```python
funcao_lambda = lambda x: x+x
```

- lambda x - declaração da função lambda (a definição de uma função padrão seria `def sum(foo)`)
- : x+x - o valor retornado (o mesmo que `return x+x` na função padrão)

# Como retornar uma função como saída de outra função

```python
def funcao():

  def outra_funcao():
    return 'Olá!'

  return outra_funcao
```

- `def funcao()` - função que retornará a função
- `def outra_funcao` - definição da função que será retornada pela primeira
- `return 'Olá!'` - um valor qualquer retornado pela função que será retornada
- `return outra_funcao` - parte que a primeira função retorna a função interna

## Exemplo:
```python
def funcao_a():

  def funcao_b():
    return 'Olá!'

  return funcao_b
  
f = funcao_a()
print(f())
```
```
Olá!

```

# Como acessar os parâmetros de uma função

```python
def uma_funcao(x, y, z):
  args = locals()
```

- `uma_funcao` - Uma função (método) qualquer
- `locals()` - Retorna um dicionário com as variáveis locais (Deve ser chamada na primeira linha da função. Por quê?)

## Exemplo:
```python
def uma_funcao(x, y, z):
  print(locals())

uma_funcao(1, 2, 3)
```
```
{'x': 1, 'y': 2, 'z': 3}

```

