<div align="center">
  <h1> 30 Dias de Python: Dia 12 - Modulos </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Autor:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> Segunda edição: July, 2021</small>
</sub>


</div>

[<< Dia 11](../11_Dia_Funcoes/README.md) | [Dia 13 >>](../13_Dia_Compreensao_de_Listas/README.md)

![30DiasDePython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 12](#-dia-12)
  - [Módulos](#módulos)
    - [O que é um módulo](#o-que-é-um-módulo)
    - [Criando um módulo](#criando-um-módulo)
    - [Importando um módulo](#importando-um-módulo)
    - [Importando funções de um módulo](#importando-funções-de-um-módulo)
    - [Importando funções de um módulo e renomeando](#importando-funções-de-um-módulo-e-renomeando)
  - [Importando módulos built-in](#importando-módulos-built-in)
    - [Módulo OS](#módulo-os)
    - [Módulo Sys](#módulo-sys)
    - [Módulo Statistics](#módulo-statistics)
    - [Módulo Math](#módulo-math)
    - [Módulo String](#módulo-string)
    - [Módulo Random](#módulo-random)
  - [💻 Exercícios: Dia 12](#-exercícios-dia-12)
    - [Exercícios: Nível 1](#exercícios-nível-1)
    - [Exercícios: Nível 2](#exercícios-nível-2)
    - [Exercícios: Nível 3](#exercícios-nível-3)

# 📘 Dia 12

## Módulos

### O que é um módulo

Um módulo é um arquivo que contém um conjunto de códigos ou de funções que podem ser incluídos em uma aplicação. Um módulo pode ser um arquivo com uma única variável, uma função ou uma grande base de código.

### Criando um módulo

Para criar um módulo, escrevemos nosso código em um script Python e salvamos como um arquivo .py. Crie um arquivo chamado mymodule.py dentro da pasta do seu projeto. Vamos escrever um pouco de código nesse arquivo.

```py
# arquivo mymodule.py
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
```

Crie o arquivo main.py no diretório do seu projeto e importe o arquivo mymodule.py.

### Importando um módulo

Para importar o arquivo, usamos a palavra-chave _import_ e apenas o nome do arquivo.

```py
# arquivo main.py
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh
```

### Importando funções de um módulo

Podemos ter muitas funções em um arquivo e importá-las de formas diferentes.

```py
# arquivo main.py
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])
```

### Importando funções de um módulo e renomeando

Durante a importação, podemos renomear o módulo.

```py
# arquivo main.py
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100 
weight = mass * g
print(weight)
print(p)
print(p['firstname'])
```

## Importando módulos built-in

Assim como em outras linguagens de programação, também podemos importar módulos usando a palavra-chave _import_. Vamos importar os módulos comuns que usamos com mais frequência. Alguns dos módulos built-in mais comuns: _math_, _datetime_, _os_, _sys_, _random_, _statistics_, _collections_, _json_, _re_

### Módulo OS

Com o módulo _os_ do Python, é possível automatizar muitas tarefas do sistema operacional. O módulo OS fornece funções para criar, alterar o diretório de trabalho atual, remover um diretório (pasta), obter seu conteúdo, mudar e identificar o diretório atual.

```py
# importa o módulo
import os
# Criando um diretório
os.mkdir('directory_name')
# Alterando o diretório atual
os.chdir('path')
# Obtendo o diretório de trabalho atual
os.getcwd()
# Removendo um diretório
os.rmdir()
```

### Módulo Sys

O módulo sys fornece funções e variáveis usadas para manipular diferentes partes do ambiente de execução do Python. A função sys.argv retorna uma lista dos argumentos de linha de comando passados a um script Python. O item no índice 0 dessa lista é sempre o nome do script; no índice 1 está o argumento passado pela linha de comando.

Exemplo de um arquivo script.py:

```py
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # esta linha imprimiria: filename argument1 argument2
print('Bem-vindo {}. Aproveite o desafio {}!'.format(sys.argv[1], sys.argv[2]))
```

Agora, para ver como esse script funciona, escrevi na linha de comando:

```sh
python script.py Asabeneh 30DaysOfPython
```

O resultado:

```sh
Bem-vindo Asabeneh. Aproveite o desafio 30DayOfPython! 
```

Alguns comandos úteis do sys:

```py
# para sair do sys
sys.exit()
# Para saber o maior inteiro que a variável aceita
sys.maxsize
# Para saber o path do ambiente
sys.path
# Para saber a versão do Python que você está usando
sys.version
```

### Módulo Statistics

O módulo statistics fornece funções de estatística matemática para dados numéricos. As funções estatísticas populares definidas neste módulo são: _mean_, _median_, _mode_, _stdev_ etc.

```py
from statistics import * # importando todos os módulos de statistics
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

### Módulo Math

Módulo que contém muitas operações matemáticas e constantes.

```py
import math
print(math.pi)           # 3.141592653589793, constante pi
print(math.sqrt(2))      # 1.4142135623730951, raiz quadrada
print(math.pow(2, 3))    # 8.0, função exponencial
print(math.floor(9.81))  # 9, arredondando para baixo
print(math.ceil(9.81))   # 10, arredondando para cima
print(math.log10(100))   # 2, logaritmo na base 10
```

Agora importamos o módulo *math*, que contém várias funções que nos ajudam a fazer cálculos matemáticos. Para verificar quais funções o módulo tem, podemos usar _help(math)_ ou _dir(math)_. Isso exibe as funções disponíveis no módulo. Se quisermos importar apenas uma função específica do módulo, fazemos assim:

```py
from math import pi
print(pi)
```

Também é possível importar várias funções de uma vez

```py

from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

```

Mas se quisermos importar todas as funções do módulo math, podemos usar \* .

```py
from math import *
print(pi)                  # 3.141592653589793, constante pi
print(sqrt(2))             # 1.4142135623730951, raiz quadrada
print(pow(2, 3))           # 8.0, exponencial
print(floor(9.81))         # 9, arredondando para baixo
print(ceil(9.81))          # 10, arredondando para cima
print(math.log10(100))     # 2
```

Na importação, também podemos renomear a função.

```py
from math import pi as  PI
print(PI) # 3.141592653589793
```

### Módulo String

O módulo string é útil para muitos propósitos. O exemplo abaixo mostra alguns usos do módulo string.

```py
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### Módulo Random

A esta altura, você já está familiarizado com a importação de módulos. Vamos fazer mais uma importação para fixar bem. Vamos importar o módulo _random_, que nos dá um número aleatório entre 0 e 0.9999.... O módulo _random_ tem muitas funções, mas nesta seção usaremos apenas _random_ e _randint_.

```py
from random import random, randint
print(random())   # não recebe argumentos; retorna um valor entre 0 e 0.9999
print(randint(5, 20)) # retorna um número inteiro aleatório entre [5, 20] inclusive
```

🌕 Você está indo longe. Continue! Você acabou de concluir os desafios do dia 12 e está 12 passos à frente no caminho para a grandeza. Agora faça alguns exercícios para o cérebro e para os músculos.

## 💻 Exercícios: Dia 12

### Exercícios: Nível 1

1. Escreva uma função que gere um random_user_id de seis dígitos/caracteres.
   ```py
     print(random_user_id()) 
     '1ee33d'
   ```
2. Modifique a tarefa anterior. Declare uma função chamada user_id_gen_by_user. Ela não recebe parâmetros, mas obtém duas entradas com input(). Uma das entradas é o número de caracteres e a outra é o número de IDs que devem ser gerados.
   
```py
print(user_id_gen_by_user()) # entrada do usuário: 5 5
#saída:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr
```

3. Escreva uma função chamada rgb_color_gen. Ela vai gerar cores rgb (3 valores variando de 0 a 255 cada).
   
```py
print(rgb_color_gen())
# rgb(125,244,255) - a saída deve estar neste formato
```

### Exercícios: Nível 2

1. Escreva uma função list_of_hexa_colors que retorna qualquer quantidade de cores hexadecimais em um array (seis números hexadecimais escritos depois de #. O sistema numérico hexadecimal é formado por 16 símbolos: 0-9 e as 6 primeiras letras do alfabeto, a-f. Veja a tarefa 6 para exemplos de saída).
1. Escreva uma função list_of_rgb_colors que retorna qualquer quantidade de cores RGB em um array.
1. Escreva uma função generate_colors que pode gerar qualquer quantidade de cores hexa ou rgb.

```py
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
   ```

### Exercícios: Nível 3

1. Chame sua função shuffle_list; ela recebe uma lista como parâmetro e retorna uma lista embaralhada
1. Escreva uma função que retorna um array de sete números aleatórios no intervalo de 0-9. Todos os números devem ser únicos.

🎉 PARABÉNS! 🎉

[<< Dia 11](../11_Dia_Funcoes/README.md) | [Dia 13 >>](../13_Dia_Compreensao_de_Listas/README.md)
