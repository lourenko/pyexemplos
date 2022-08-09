# Como apagar um elemento de uma lista

### A partir da posição do elemento na lista
```python
uma_lista.pop(2)
```

- `uma_lista` - Lista da qual será retirado o elemento
- `pop(` - Remove o elemento a partir do seu endereço (a partir de zero)
- `(2)` - Remover o elemento indexado em `2` (ou terceiro elemento)

## Exemplo:
```python
uma_lista = [1, "Jaca", 3.14, "Vaca amarela", 7.8]
uma_lista.pop(2)
print(uma_lista)
```
```
[1, 'Jaca', 'Vaca amarela', 7.8]

```

# ou diretamente a partir do valor

```python
uma_lista.remove("Jaca")
```

- `remove(` - Remove um dado valor diretamente da lista
- `"Java"` - Valor a ser removido

## Exemplo:
```python
uma_lista = [1, "Jaca", 3.14, "Vaca amarela", 7.8]
uma_lista.remove("Jaca")
print(uma_lista)
```
```
[1, 3.14, 'Vaca amarela', 7.8]

```

