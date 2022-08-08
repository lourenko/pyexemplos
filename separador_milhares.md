# Separador de milhares

```python
sep = "{:,}".format(963852741)
sep.replace(',','.')
```

- `,` - charactere de separação
- `963852741` - número a ser separado
- `sep` - contém o número separado com vírgula
- `replace(',','.')` - substitui as vírgulas por pontos

## Example: 
```python
print(("{:,}".format(123456789)).replace(',','.'))
```
```
963.852.741

```
