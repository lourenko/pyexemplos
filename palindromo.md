# Verifica se uma palavra é um palíndromo

```python
def palindromo(palavra):
    return palavra.lower() == palavra[::-1].lower()

print(palindromo("Sopapos"))
```

- `palindromo(` - nome da função que verifica se a palavra é um palíndromo
- `.lower(` - converte todas as letras da palavra para minúsculas
- `word[::-1]` - escreve a palavras na ordem inversa (trás para frente)
- `return` - retorna `True` se a palavra for um palíndromo

## Exemplo: 
```python
if palindromo("Reviver"):
    print("É palíndromo!")
```
```
É palíndromo!

```
