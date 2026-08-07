<div align="center">
  <h1> 30 Dias de Python: Dia 11 - Funcoes</h1>
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

[<< Dia 10](../10_Dia_Loops/README.md) | [Dia 12 >>](../12_Dia_Modulos/README.md)

![30DiasDePython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 11](#-dia-11)
  - [Funções](#funções)
    - [Definindo uma função](#definindo-uma-função)
    - [Declarando e chamando uma função](#declarando-e-chamando-uma-função)
    - [Função sem parâmetros](#função-sem-parâmetros)
    - [Função que retorna um valor - Parte 1](#função-que-retorna-um-valor---parte-1)
    - [Função com parâmetros](#função-com-parâmetros)
    - [Passando argumentos com chave e valor](#passando-argumentos-com-chave-e-valor)
    - [Função que retorna um valor - Parte 2](#função-que-retorna-um-valor---parte-2)
    - [Função com parâmetros padrão](#função-com-parâmetros-padrão)
    - [Número arbitrário de argumentos](#número-arbitrário-de-argumentos)
    - [Parâmetros padrão e número arbitrário de parâmetros em funções](#parâmetros-padrão-e-número-arbitrário-de-parâmetros-em-funções)
    - [Função como parâmetro de outra função](#função-como-parâmetro-de-outra-função)
  - [Depoimento](#depoimento)
  - [💻 Exercícios: Dia 11](#-exercícios-dia-11)
    - [Exercícios: Nível 1](#exercícios-nível-1)
    - [Exercícios: Nível 2](#exercícios-nível-2)
    - [Exercícios: Nível 3](#exercícios-nível-3)

# 📘 Dia 11

## Funções

Até aqui, vimos muitas funções built-in do Python. Nesta seção, vamos focar em funções personalizadas. O que é uma função? Antes de começarmos a criá-las, vamos entender o que é uma função e por que precisamos delas.

### Definindo uma função

Uma função é um bloco reutilizável de código ou de instruções de programação feito para executar determinada tarefa. Para definir ou declarar uma função, o Python oferece a palavra-chave _def_. A seguir está a sintaxe para definir uma função. O bloco de código da função só é executado se ela for chamada ou invocada.

### Declarando e chamando uma função

Quando criamos uma função, dizemos que estamos declarando uma função. Quando passamos a usá-la, dizemos que estamos _chamando_ ou _invocando_ a função. As funções podem ser declaradas com ou sem parâmetros.

```py
# sintaxe
# Declarando uma função
def function_name():
    códigos
    códigos
# Chamando uma função
function_name()
```

### Função sem parâmetros

Uma função pode ser declarada sem parâmetros.

**Exemplo:**

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # chamando uma função

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
```

### Função que retorna um valor - Parte 1

As funções retornam valores com a instrução _return_. Se uma função não tiver return, ela retorna None. Vamos reescrever as funções acima usando return. A partir de agora, ao chamar a função e imprimir o resultado, obtemos um valor.

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
```

### Função com parâmetros

Em uma função, podemos passar diferentes tipos de dados (número, string, boolean, list, tuple, dictionary ou set) como parâmetros.

- Parâmetro único: se a função recebe um parâmetro, devemos chamá-la com um argumento

```py
  # sintaxe
  # Declarando uma função
  def function_name(parameter):
    códigos
    códigos
  # Chamando a função
  print(function_name(argument))
```

**Exemplo:**

```py
def greetings (name):
    message = name + ', bem-vindo ao Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

- Dois parâmetros: uma função pode ter ou não parâmetros. Ela também pode ter dois ou mais parâmetros. Se a função recebe parâmetros, devemos chamá-la com argumentos. Vamos ver uma função com dois parâmetros:

```py
  # sintaxe
  # Declarando uma função
  def function_name(para1, para2):
    códigos
    códigos
  # Chamando a função
  print(function_name(arg1, arg2))
```

**Exemplo:**

```py
def generate_full_name (first_name, last_name):
    space = ' '
      full_name = first_name + space + last_name
      return full_name
print('Nome completo: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Soma de dois números: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age 

print('Idade: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # o valor precisa ser convertido para string primeiro
    return weight
print('Peso de um objeto em Newtons: ', weight_of_object(100, 9.81))
```

### Passando argumentos com chave e valor

Se passarmos os argumentos com chave e valor, a ordem dos argumentos não importa.

```py
# sintaxe
# Declarando uma função
def function_name(para1, para2):
    códigos
    códigos
# Chamando a função
print(function_name(para1 = 'John', para2 = 'Doe')) # a ordem dos argumentos não importa aqui
```

**Exemplo:**

```py
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh')

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # a ordem não importa
```

### Função que retorna um valor - Parte 2

Se não retornarmos um valor em uma função, ela retorna _None_ por padrão. Para retornar um valor, usamos a palavra-chave _return_ seguida da variável que queremos devolver. Podemos retornar qualquer tipo de dado de uma função.

- Retornando uma string:
**Exemplo:**

```py
def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')
```

- Retornando um número:

**Exemplo:**

```py
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Idade: ', calculate_age(2019, 1819))
```

- Retornando um boolean:
  **Exemplo:**

```py
def is_even (n):
    if n % 2 == 0:
        return True    # return interrompe a execução da função, de forma semelhante ao break
    return False
print(is_even(10)) # True
print(is_even(7)) # False
```

- Retornando uma lista:
  **Exemplo:**

```py
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```

### Função com parâmetros padrão

Às vezes passamos valores padrão aos parâmetros. Se não passarmos argumentos ao chamar a função, esses valores padrão serão usados.

```py
# sintaxe
# Declarando uma função
def function_name(param = value):
    códigos
    códigos
# Chamando a função
function_name()
function_name(arg)
```

**Exemplo:**

```py
def greetings (name = 'Peter'):
    message = name + ', bem-vindo ao Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age 
print('Idade: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # o valor precisa ser convertido para string primeiro
    return weight
print('Peso de um objeto em Newtons: ', weight_of_object(100)) # 9.81 - gravidade média na superfície da Terra
print('Peso de um objeto em Newtons: ', weight_of_object(100, 1.62)) # gravidade na superfície da Lua
```

### Número arbitrário de argumentos

Se não soubermos quantos argumentos vamos passar para a função, podemos criar uma função que aceite um número arbitrário de argumentos adicionando \* antes do nome do parâmetro.

```py
# sintaxe
# Declarando uma função
def function_name(*args):
    códigos
    códigos
# Chamando a função
function_name(param1, param2, param3,..)
```

**Exemplo:**

```py
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # o mesmo que total = total + num
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

### Parâmetros padrão e número arbitrário de parâmetros em funções

```py
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i) 
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')
```
### Desempacotamento de dicionário

Você pode chamar uma função que tem argumentos nomeados usando um dicionário cujas chaves batem com os nomes dos parâmetros. Para isso, use ``**``.

```py
# Define uma função que recebe dois argumentos: 'name' e 'location'
def greet(name, location):
    # Imprime uma mensagem de saudação usando os argumentos fornecidos
    print("Olá", name, "como está o tempo em", location)

# Chama a função usando argumentos nomeados
greet(name="Alice", location="New York")  
# Saída: Olá Alice como está o tempo em New York

# Cria um dicionário com chaves que correspondem aos nomes dos parâmetros da função
my_dict = {"name": "Alice", "location": "New York"}

# Chama a função usando desempacotamento de dicionário
greet(**my_dict)  
# O operador ** desempacota o dicionário, passando seus pares chave-valor
# como argumentos nomeados para a função.
# Saída: Olá Alice como está o tempo em New York
```

### Número arbitrário de argumentos nomeados

Você também pode definir uma função para aceitar um número arbitrário de argumentos nomeados.

```py
def arbitrary_named_args(**args):
    print("Recebi um número arbitrário de argumentos, totalizando", len(args))
    print("Eles são fornecidos como um dicionário na minha função:", type(args))
    print("Vamos imprimi-los:")
    for k, v in args.items():
        print(" * chave:", k, "valor:", v)
```

Em geral, evite isso a menos que seja necessário, pois fica mais difícil entender o que a função aceita e o que ela faz.

### Função como parâmetro de outra função

```py
# Você pode passar funções como parâmetros
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```

🌕 Você já conquistou bastante coisa até aqui. Continue! Você acabou de concluir os desafios do dia 11 e está 11 passos à frente no caminho para a grandeza. Agora faça alguns exercícios para o cérebro e para os músculos.

## Depoimento

Agora é hora de expressar suas opiniões sobre o autor e o 30DaysOfPython. Você pode deixar seu depoimento neste [link](https://testimonial-s3sw.onrender.com/)

## 💻 Exercícios: Dia 11

### Exercícios: Nível 1

1. Declare uma função _add_two_numbers_. Ela recebe dois parâmetros e retorna a soma.
2. A área de um círculo é calculada assim: area = π x r x r. Escreva uma função que calcule _area_of_circle_.
3. Escreva uma função chamada add_all_nums que recebe um número arbitrário de argumentos e soma todos eles. Verifique se todos os itens da lista são do tipo número. Se não forem, dê um feedback razoável.
4. A temperatura em °C pode ser convertida para °F com esta fórmula: °F = (°C x 9/5) + 32. Escreva uma função que converta °C para °F, _convert_celsius_to-fahrenheit_.
5. Escreva uma função chamada check-season; ela recebe um parâmetro month e retorna a estação: Autumn, Winter, Spring ou Summer.
6. Escreva uma função chamada calculate_slope que retorne a inclinação de uma equação linear
7. A equação do segundo grau é calculada assim: ax² + bx + c = 0. Escreva uma função que calcule o conjunto solução de uma equação do segundo grau, _solve_quadratic_eqn_.
8. Declare uma função chamada print_list. Ela recebe uma lista como parâmetro e imprime cada elemento da lista.
9. Declare uma função chamada reverse_list. Ela recebe um array como parâmetro e retorna o array invertido (use loops).

```py
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"])) 
# ["C", "B", "A"]
```

10. Declare uma função chamada capitalize_list_items. Ela recebe uma lista como parâmetro e retorna uma lista com os itens capitalizados
11. Declare uma função chamada add_item. Ela recebe uma lista e um item como parâmetros. Retorna a lista com o item adicionado no final.

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

```

12. Declare uma função chamada remove_item. Ela recebe uma lista e um item como parâmetros. Retorna a lista com o item removido.

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
```

13. Declare uma função chamada sum_of_numbers. Ela recebe um número como parâmetro e soma todos os números nesse intervalo.

```py
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

14. Declare uma função chamada sum_of_odds. Ela recebe um número como parâmetro e soma todos os números ímpares nesse intervalo.
15. Declare uma função chamada sum_of_even. Ela recebe um número como parâmetro e soma todos os números pares nesse intervalo.

### Exercícios: Nível 2

1. Declare uma função chamada evens_and_odds. Ela recebe um inteiro positivo como parâmetro e conta a quantidade de pares e ímpares nesse número.

```py
    print(evens_and_odds(100))
    # A quantidade de ímpares é 50.
    # A quantidade de pares é 51.
```

1. Chame sua função factorial; ela recebe um número inteiro como parâmetro e retorna o fatorial desse número
1. Chame sua função _is_empty_; ela recebe um parâmetro e verifica se ele está vazio ou não
1. Escreva diferentes funções que recebem listas. Elas devem calcular: calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (desvio padrão).
1. Escreva uma função chamada _greet_ que recebe um argumento padrão, _name_. Se nenhum argumento for fornecido, ela deve imprimir "Hello, Guest!"; caso contrário, deve cumprimentar a pessoa pelo nome.

```py
    greet()
    # "Hello, Guest!
    greet("Alice")
    # "Hello, Alice!"
```
1. Crie uma função chamada _show_args_ para receber um número arbitrário de argumentos nomeados e imprimir seus nomes e valores.
   ```py
   show_args(name="Alice", age=30, city="New York")
   # Received: name: Alice, age: 30, city: New York
   show_args(name="Bob", pet="Fluffy, the bunny")
   # Received: name: Bob, pet: Fluffy, the bunny
   ```


### Exercícios: Nível 3

1. Escreva uma função chamada is_prime, que verifica se um número é primo.
1. Escreva uma função que verifica se todos os itens da lista são únicos.
1. Escreva uma função que verifica se todos os itens da lista são do mesmo tipo de dado.
1. Escreva uma função que verifica se a variável fornecida é um nome de variável Python válido
1. Vá até a pasta data e acesse o arquivo countries-data.py.

- Crie uma função chamada the most_spoken_languages in the world. Ela deve retornar os 10 ou 20 idiomas mais falados no mundo em ordem decrescente
- Crie uma função chamada the most_populated_countries. Ela deve retornar os 10 ou 20 países mais populosos em ordem decrescente.

🎉 PARABÉNS! 🎉

[<< Dia 10](../10_Dia_Loops/README.md) | [Dia 12 >>](../12_Dia_Modulos/README.md)
