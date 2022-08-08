# Como apagar um elemento de uma lista

### A partir da posição do elemento na lista
```python
myList.pop(2)
```

- `myList` - List to remove element from
- `pop(` - Removes specified element by index (starts from zero) 
- `(2)` - Remove element with index `2` (third element)

group: delete_element

## Example: 
```python
myList = ["Python", "Java", "Rust", "Javascript", "Ruby"]
myList.pop(2)
print(myList)
```
```
['Python', 'Java', 'Javascript', 'Ruby']

```

# Delete element from list by value

```python
myList.remove("Java")
```

- `myList` - List to remove element from
- `remove(` - Removes specified element by value
- `"Java"` - Value of an element to remove from list

group: delete_element

## Example:
```python
myList = ["Python", "Java", "Rust", "Javascript", "Ruby"]
myList.remove("Java")
print(myList)
```
```
['Python', 'Rust', 'Javascript', 'Ruby']

```

