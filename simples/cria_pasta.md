# Cria uma nova pasta
Útil para salvar resultados de uma simulação

```python
import os
nome = os.getlogin()
diretorio = f'C:/Users/{nome}/Desktop/'
nova_pasta = 'Resultados'
novo_caminho = os.path.join(diretorio, nova_pasta)
if not os.path.exists(novo_caminho):
    os.mkdir(novo_caminho)
```

- os - Biblioteca para comandos do sistema operacional
- os.getlogin() - retorna o nome de usuário da máquina
- os.path.join( - junta o caminho com o nome da pasta a ser criada
- os.path.exists( - verifica se a pasta já existe
- os.mkdir( - cria a nova pasta com o nome "Resultados"

