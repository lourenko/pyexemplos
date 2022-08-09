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


