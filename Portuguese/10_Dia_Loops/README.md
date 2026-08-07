<div align="center">
  <h1> 30 Dias de Python: Dia 10 - Loops</h1>
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

[<< Dia 9](../09_Dia_Condicionais/README.md) | [Dia 11 >>](../11_Dia_Funcoes/README.md)

![30DiasDePython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 10](#-dia-10)
  - [Loops](#loops)
    - [Loop While](#loop-while)
    - [Break e Continue - Parte 1](#break-e-continue---parte-1)
    - [Loop For](#loop-for)
    - [Break e Continue - Parte 2](#break-e-continue---parte-2)
    - [A função Range](#a-função-range)
    - [Loop For aninhado](#loop-for-aninhado)
    - [For Else](#for-else)
    - [Pass](#pass)
  - [💻 Exercícios: Dia 10](#-exercícios-dia-10)
    - [Exercícios: Nível 1](#exercícios-nível-1)
    - [Exercícios: Nível 2](#exercícios-nível-2)
    - [Exercícios: Nível 3](#exercícios-nível-3)

# 📘 Dia 10

## Loops

A vida é cheia de rotinas. Na programação, também fazemos muitas tarefas repetitivas. Para lidar com isso, as linguagens usam loops. O Python oferece estes dois tipos de loop:

1. while loop
2. for loop

### Loop While

Usamos a palavra reservada _while_ para criar um while loop. Ele executa um bloco de instruções repetidamente até que determinada condição seja satisfeita. Quando a condição se torna falsa, as linhas de código depois do loop passam a ser executadas.

```py
  # sintaxe
while condition:
    o código vai aqui
```

**Exemplo:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
# imprime de 0 a 4
```

No while loop acima, a condição se torna falsa quando count é 5. É nesse momento que o loop para.
Se você quiser executar um bloco de código quando a condição deixar de ser verdadeira, pode usar _else_.

```py
  # sintaxe
while condition:
    o código vai aqui
else:
    o código vai aqui
```

**Exemplo:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
```

A condição do loop acima se torna falsa quando count é 5, o loop para e a execução entra no else. Como resultado, 5 será impresso.

### Break e Continue - Parte 1

- Break: usamos break quando queremos sair ou interromper o loop.

```py
# sintaxe
while condition:
    o código vai aqui
    if another_condition:
        break
```

**Exemplo:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
```

O while loop acima imprime apenas 0, 1 e 2; quando chega a 3, ele para.

- Continue: com a instrução continue, podemos pular a iteração atual e seguir para a próxima:

```py
  # sintaxe
while condition:
    o código vai aqui
    if another_condition:
        continue
```

**Exemplo:**

```py
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1
```

O while loop acima imprime apenas 0, 1, 2 e 4 (pula o 3).

### Loop For

A palavra-chave _for_ é usada para criar um for loop, de forma semelhante a outras linguagens, mas com algumas diferenças de sintaxe. O loop serve para iterar sobre uma sequência (lista, tupla, dicionário, set ou string).

- Usando for loop em uma lista

```py
# sintaxe
for iterator in lst:
    o código vai aqui
```

**Exemplo:**

```py
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number é um nome temporário para se referir aos itens da lista, válido só dentro deste loop
    print(number)       # os números serão impressos linha a linha, de 0 a 5
```

- Usando for loop em uma string

```py
# sintaxe
for iterator in string:
    o código vai aqui
```

**Exemplo:**

```py
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])
```

- Usando for loop em uma tupla

```py
# sintaxe
for iterator in tpl:
    o código vai aqui
```

**Exemplo:**

```py
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
```

- For loop com dicionário
  Percorrer um dicionário devolve as chaves.

```py
  # sintaxe
for iterator in dct:
    o código vai aqui
```

**Exemplo:**

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # assim imprimimos tanto as chaves quanto os valores
```

- Usando for loop em um set

```py
# sintaxe
for iterator in st:
    o código vai aqui
```

**Exemplo:**

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```

### Break e Continue - Parte 2

Lembrete rápido:
_Break_: usamos break quando queremos interromper o loop antes de ele terminar.

```py
# sintaxe
for iterator in sequence:
    o código vai aqui
    if condition:
        break
```

**Exemplo:**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
```

No exemplo acima, o loop para quando chega a 3.

Continue: usamos continue quando queremos pular alguns passos da iteração do loop.

```py
  # sintaxe
for iterator in sequence:
    o código vai aqui
    if condition:
        continue
```

**Exemplo:**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('O próximo número deve ser ', number + 1) if number != 5 else print('fim do loop') # em condições curtas, precisamos tanto do if quanto do else
print('fora do loop')
```

No exemplo acima, se o número for igual a 3, o passo _depois_ da condição (mas ainda dentro do loop) é pulado e a execução do loop continua se ainda houver iterações.

### A função Range

A função _range()_ é usada para retornar uma sequência de números. O _range(start, end, step)_ recebe três parâmetros: início, fim e incremento. Por padrão, começa em 0 e o incremento é 1. A sequência range precisa de pelo menos 1 argumento (o fim).
Criando sequências com range:

```py
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 argumentos indicam início e fim da sequência; o passo fica no padrão 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# para ir do início ao fim em ordem regressiva
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]
```

```py
# sintaxe
for iterator in range(start, end, step):
```

**Exemplo:**

```py
for number in range(11):
    print(number)   # imprime de 0 a 10, sem incluir 11
```

### Loop For aninhado

Você pode escrever loops dentro de um loop.

```py
# sintaxe
for x in y:
    for t in x:
        print(t)
```

**Exemplo:**

```py
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
```

### For Else

Se você quiser executar alguma mensagem quando o loop terminar, use else.

```py
# sintaxe
for iterator in range(start, end, step):
    faça algo
else:
    print('O loop terminou')
```

**Exemplo:**

```py
for number in range(11):
    print(number)   # imprime de 0 a 10, sem incluir 11
else:
    print('O loop para em', number)
```

### Pass

Em Python, quando uma instrução é obrigatória (depois dos dois-pontos), mas você não quer executar nenhum código ali, escreva a palavra _pass_ para evitar erros. Também podemos usá-la como placeholder para instruções futuras.

**Exemplo:**

```py
for number in range(6):
    pass
```

🌕 Você alcançou um grande marco e está imparável. Continue! Você acabou de concluir os desafios do dia 10 e está 10 passos à frente no caminho para a grandeza. Agora faça alguns exercícios para o cérebro e para os músculos.

## 💻 Exercícios: Dia 10

### Exercícios: Nível 1

1. Itere de 0 a 10 usando for loop; faça o mesmo usando while loop.
2. Itere de 10 a 0 usando for loop; faça o mesmo usando while loop.
3. Escreva um loop que faça sete chamadas a print(), para obter no resultado o seguinte triângulo:

   ```py
     #
     ##
     ###
     ####
     #####
     ######
     #######
   ```

4. Use loops aninhados para criar o seguinte:

   ```sh
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   ```

5. Imprima o seguinte padrão:

   ```sh
   0 x 0 = 0
   1 x 1 = 1
   2 x 2 = 4
   3 x 3 = 9
   4 x 4 = 16
   5 x 5 = 25
   6 x 6 = 36
   7 x 7 = 49
   8 x 8 = 64
   9 x 9 = 81
   10 x 10 = 100
   ```

6. Itere pela lista ['Python', 'Numpy','Pandas','Django', 'Flask'] usando um for loop e imprima os itens.
7. Use for loop para iterar de 0 a 100 e imprimir apenas os números pares
8. Use for loop para iterar de 0 a 100 e imprimir apenas os números ímpares

### Exercícios: Nível 2

1.  Use for loop para iterar de 0 a 100 e imprimir a soma de todos os números.

```sh
A soma de todos os números é 5050.
```

2. Use for loop para iterar de 0 a 100 e imprimir a soma de todos os pares e a soma de todos os ímpares.

   ```sh
   A soma de todos os pares é 2550. E a soma de todos os ímpares é 2500.
   ```

### Exercícios: Nível 3

1. Vá até a pasta data e use o arquivo [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py). Percorra os países e extraia todos os que contêm a palavra _land_.
1. Esta é uma lista de frutas: ['banana', 'orange', 'mango', 'lemon']. Inverta a ordem usando um loop.
1. Vá até a pasta data e use o arquivo [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py).
   1. Qual é o número total de idiomas nos dados?
   2. Encontre os dez idiomas mais falados a partir dos dados
   3. Encontre os 10 países mais populosos do mundo

🎉 PARABÉNS! 🎉

[<< Dia 9](../09_Dia_Condicionais/README.md) | [Dia 11 >>](../11_Dia_Funcoes/README.md)
