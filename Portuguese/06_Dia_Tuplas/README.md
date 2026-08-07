<div align="center">
  <h1> 30 Dias de Python: Dia 6 - Tuplas</h1>
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

[<< Dia 5](../05_Dia_Listas/README.md) | [Dia 7 >>](../07_Dia_Conjuntos/README.md)

![30DiasDePython](../../images/30DaysOfPython_banner3@2x.png)

- [Dia 6:](#dia-6)
  - [Tuplas](#tuplas)
    - [Criando uma tupla](#criando-uma-tupla)
    - [Comprimento da tupla](#comprimento-da-tupla)
    - [Acessando itens da tupla](#acessando-itens-da-tupla)
    - [Fatiando tuplas](#fatiando-tuplas)
    - [Convertendo tuplas em listas](#convertendo-tuplas-em-listas)
    - [Verificando um item em uma tupla](#verificando-um-item-em-uma-tupla)
    - [Unindo tuplas](#unindo-tuplas)
    - [Excluindo tuplas](#excluindo-tuplas)
  - [💻 Exercícios: Dia 6](#-exercícios-dia-6)
    - [Exercícios: Nível 1](#exercícios-nível-1)
    - [Exercícios: Nível 2](#exercícios-nível-2)

# Dia 6:

## Tuplas

Uma tupla é uma coleção de diferentes tipos de dados que é ordenada e inalterável (imutável). Tuplas são escritas com parênteses, (). Depois que uma tupla é criada, não podemos alterar seus valores. Não podemos usar métodos add, insert ou remove em uma tupla porque ela não é modificável (mutável). Diferente da lista, a tupla tem poucos métodos. Métodos relacionados a tuplas:

- tuple(): para criar uma tupla vazia
- count(): para contar o número de um item especificado em uma tupla
- index(): para encontrar o índice de um item especificado em uma tupla
- operador `+`: para unir duas ou mais tuplas e criar uma nova tupla

### Criando uma tupla

- Tupla vazia: Criando uma tupla vazia
  
  ```py
  # sintaxe
  empty_tuple = ()
  # ou usando o construtor tuple
  empty_tuple = tuple()
  ```

- Tupla com valores iniciais
  
  ```py
  # sintaxe
  tpl = ('item1', 'item2','item3')
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  ```

### Comprimento da tupla

Usamos o método _len()_ para obter o comprimento de uma tupla.

```py
# sintaxe
tpl = ('item1', 'item2', 'item3')
len(tpl)
```

### Acessando itens da tupla

- Indexação positiva
  Assim como no tipo de dado lista, usamos indexação positiva ou negativa para acessar itens da tupla.
  ![Acessando itens da tupla](../../images/tuples_index.png)

  ```py
  # Sintaxe
  tpl = ('item1', 'item2', 'item3')
  first_item = tpl[0]
  second_item = tpl[1]
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  first_fruit = fruits[0]
  second_fruit = fruits[1]
  last_index =len(fruits) - 1
  last_fruit = fruits[last_index]
  ```

- Indexação negativa
  Indexação negativa significa começar do fim: -1 refere-se ao último item, -2 refere-se ao penúltimo e o negativo do comprimento da lista/tupla refere-se ao primeiro item.
  ![Indexação negativa da tupla](../../images/tuple_negative_indexing.png)

  ```py
  # Sintaxe
  tpl = ('item1', 'item2', 'item3','item4')
  first_item = tpl[-4]
  second_item = tpl[-3]
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  first_fruit = fruits[-4]
  second_fruit = fruits[-3]
  last_fruit = fruits[-1]
  ```

### Fatiando tuplas

Podemos fatiar uma subtupla especificando um intervalo de índices onde começar e onde terminar na tupla; o valor de retorno será uma nova tupla com os itens especificados.

- Intervalo de índices positivos

  ```py
  # Sintaxe
  tpl = ('item1', 'item2', 'item3','item4')
  all_items = tpl[0:4]         # todos os itens
  all_items = tpl[0:]         # todos os itens
  middle_two_items = tpl[1:3]  # não inclui o item no índice 3
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  all_fruits = fruits[0:4]    # todos os itens
  all_fruits= fruits[0:]      # todos os itens
  orange_mango = fruits[1:3]  # não inclui o item no índice 3
  orange_to_the_rest = fruits[1:]
  ```

- Intervalo de índices negativos

  ```py
  # Sintaxe
  tpl = ('item1', 'item2', 'item3','item4')
  all_items = tpl[-4:]         # todos os itens
  middle_two_items = tpl[-3:-1]  # não inclui o item no índice 3 (-1)
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  all_fruits = fruits[-4:]    # todos os itens
  orange_mango = fruits[-3:-1]  # não inclui o item no índice 3
  orange_to_the_rest = fruits[-3:]
  ```

### Convertendo tuplas em listas

Podemos converter tuplas em listas e listas em tuplas. A tupla é imutável; se quisermos modificar uma tupla, devemos convertê-la em uma lista.

```py
# Sintaxe
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
```

### Verificando um item em uma tupla

Podemos verificar se um item existe ou não em uma tupla usando _in_; isso retorna um booleano.

```py
# Sintaxe
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
```

### Unindo tuplas

Podemos unir duas ou mais tuplas usando o operador +

```py
# sintaxe
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
```

### Excluindo tuplas

Não é possível remover um único item de uma tupla, mas é possível excluir a própria tupla usando _del_.

```py
# sintaxe
tpl1 = ('item1', 'item2', 'item3')
del tpl1

```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
```

🌕 Você é tão corajoso(a) — chegou até aqui. Você acabou de concluir os desafios do dia 6 e está 6 passos à frente no caminho para a grandeza. Agora faça alguns exercícios para o cérebro e para os músculos.

## 💻 Exercícios: Dia 6

### Exercícios: Nível 1

1. Crie uma tupla vazia
2. Crie uma tupla contendo os nomes das suas irmãs e dos seus irmãos (irmãos imaginários também valem)
3. Una as tuplas de irmãos e irmãs e atribua a siblings
4. Quantos irmãos você tem?
5. Modifique a tupla siblings, adicione o nome do seu pai e da sua mãe e atribua a family_members

### Exercícios: Nível 2

1. Desempacote irmãos e pais de family_members
1. Crie tuplas de frutas, vegetais e produtos de origem animal. Una as três tuplas e atribua a uma variável chamada food_stuff_tp.
1. Converta a tupla food_stuff_tp acima em uma lista food_stuff_lt
1. Fatie o item ou os itens do meio da tupla food_stuff_tp ou da lista food_stuff_lt.
1. Fatie os três primeiros itens e os três últimos itens da lista food_stuff_lt
1. Exclua a tupla food_stuff_tp completamente
1. Verifique se um item existe na tupla:

- Verifique se 'Estonia' é um país nórdico
- Verifique se 'Iceland' é um país nórdico

  ```py
  nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
  ```


[<< Dia 5](../05_Dia_Listas/README.md) | [Dia 7 >>](../07_Dia_Conjuntos/README.md)
