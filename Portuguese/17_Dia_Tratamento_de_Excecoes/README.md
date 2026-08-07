<div align="center">
  <h1> 30 Dias de Python: Dia 17 - Tratamento de Excecoes </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Author:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small> Segunda edição: July, 2021</small>
  </sub>
</div>

[<< Dia 16](../16_Dia_Datetime/README.md) | [Dia 18 >>](../18_Dia_Expressoes_Regulares/README.md)

![30DiasDePython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 17](#-dia-17)
  - [Tratamento de Excecoes](#tratamento-de-excecoes)
  - [Empacotamento e Desempacotamento de Argumentos em Python](#empacotamento-e-desempacotamento-de-argumentos-em-python)
    - [Desempacotamento](#desempacotamento)
      - [Desempacotando Listas](#desempacotando-listas)
      - [Desempacotando Dicionarios](#desempacotando-dicionarios)
    - [Empacotamento](#empacotamento)
    - [Empacotando Listas](#empacotando-listas)
      - [Empacotando Dicionarios](#empacotando-dicionarios)
  - [Spreading em Python](#spreading-em-python)
  - [Enumerate](#enumerate)
  - [Zip](#zip)
  - [Exercicios: Dia 17](#exercicios-dia-17)

# 📘 Dia 17

## Tratamento de Excecoes

O Python usa _try_ e _except_ para tratar erros de forma elegante. Uma saída elegante (ou tratamento elegante) de erros é um idioma simples de programação: o programa detecta uma condição de erro grave e "sai de forma elegante", de maneira controlada. Muitas vezes, o programa imprime uma mensagem de erro descritiva no terminal ou em um log como parte dessa saída elegante; isso torna nossa aplicação mais robusta. A causa de uma exceção frequentemente é externa ao próprio programa. Exemplos de exceções podem ser uma entrada incorreta, um nome de arquivo errado, a impossibilidade de encontrar um arquivo, um dispositivo de E/S com defeito. O tratamento elegante de erros impede que nossas aplicações travem.

Cobrimos os diferentes tipos de _erro_ do Python na seção anterior. Se usarmos _try_ e _except_ no nosso programa, então ele não vai levantar erros nesses blocos.

![Try and Except](../../images/try_except.png)

```py
try:
    código neste bloco se as coisas derem certo
except:
    código neste bloco executa se as coisas derem errado
```

**Exemplo:**

```py
try:
    print(10 + '5')
except:
    print('Algo deu errado')
```

No exemplo acima, o segundo operando é uma string. Poderíamos convertê-lo para float ou int para somá-lo com o número e fazer funcionar. Mas sem nenhuma alteração, o segundo bloco, _except_, será executado.

**Exemplo:**

```py
try:
    name = input('Digite o seu nome:')
    year_born = input('Ano em que você nasceu:')
    age = 2019 - year_born
    print(f'Você é {name}. E a sua idade é {age}.')
except:
    print('Algo deu errado')
```

```sh
Algo deu errado
```

No exemplo acima, o bloco de exceção vai rodar e nós não sabemos exatamente qual é o problema. Para analisar o problema, podemos usar os diferentes tipos de erro com except.

No exemplo a seguir, o erro será tratado e também vamos saber que tipo de erro foi levantado.

```py
try:
    name = input('Digite o seu nome:')
    year_born = input('Ano em que você nasceu:')
    age = 2019 - year_born
    print(f'Você é {name}. E a sua idade é {age}.')
except TypeError:
    print('Ocorreu um erro de tipo')
except ValueError:
    print('Ocorreu um erro de valor')
except ZeroDivisionError:
    print('Ocorreu um erro de divisão por zero')
```

```sh
Digite o seu nome:Asabeneh
Ano em que você nasceu:1920
Ocorreu um erro de tipo
```

No código acima, a saída vai ser um _TypeError_.
Agora, vamos adicionar um bloco adicional:

```py
try:
    name = input('Digite o seu nome:')
    year_born = input('Ano em que você nasceu:')
    age = 2019 - int(year_born)
    print(f'Você é {name}. E a sua idade é {age}.')
except TypeError:
    print('Ocorreu um erro de tipo')
except ValueError:
    print('Ocorreu um erro de valor')
except ZeroDivisionError:
    print('Ocorreu um erro de divisão por zero')
else:
    print('Eu normalmente rodo com o bloco try')
finally:
    print('Eu sempre rodo.')
```

```sh
Digite o seu nome:Asabeneh
Ano em que você nasceu:1920
Você é Asabeneh. E a sua idade é 99.
Eu normalmente rodo com o bloco try
Eu sempre rodo.
```

Também é possível encurtar o código acima da seguinte forma:

```py
try:
    name = input('Digite o seu nome:')
    year_born = input('Ano em que você nasceu:')
    age = 2019 - int(year_born)
    print(f'Você é {name}. E a sua idade é {age}.')
except Exception as e:
    print(e)

```

## Empacotamento e Desempacotamento de Argumentos em Python

Usamos dois operadores:

- \* para tuplas
- \*\* para dicionários

Vamos pegar o exemplo abaixo. Ele só recebe argumentos, mas nós temos uma lista. Podemos desempacotar a lista e transformá-la em argumentos.

### Desempacotamento

#### Desempacotando Listas

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
```

Quando executamos este código, ele levanta um erro, porque esta função recebe números (não uma lista) como argumentos. Vamos desempacotar/desestruturar a lista.

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
```

Também podemos usar o desempacotamento na função built-in range, que espera um início e um fim.

```py
numbers = range(2, 7)  # chamada normal com argumentos separados
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # chamada com argumentos desempacotados de uma lista
print(numbers)      # [2, 3, 4, 5,6]

```

Uma lista ou uma tupla também pode ser desempacotada assim:

```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
```

#### Desempacotando Dicionarios

```py
def unpacking_person_info(name, country, city, age):
    return f'{name} mora em {country}, {city}. Ele tem {age} anos de idade.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh mora em Finland, Helsinki. Ele tem 250 anos de idade.
```

### Empacotamento

Às vezes, nunca sabemos quantos argumentos precisam ser passados para uma função Python. Podemos usar o método de empacotamento para permitir que nossa função receba um número ilimitado ou arbitrário de argumentos.

### Empacotando Listas

```py
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
```

#### Empacotando Dicionarios

```py
def packing_person_info(**kwargs):
    # verifique o tipo de kwargs e ele é do tipo dict
    # print(type(kwargs))
    # Imprimindo os itens do dicionário
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))
```

```sh
name = Asabeneh
country = Finland
city = Helsinki
age = 250
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

## Spreading em Python

Como no JavaScript, o spreading é possível em Python. Vamos conferir no exemplo abaixo:

```py
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
```

## Enumerate

Se estivermos interessados no índice de uma lista, usamos a função built-in _enumerate_ para obter o índice de cada item da lista.

```py
for index, item in enumerate([20, 30, 40]):
    print(index, item)
```

```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    if i == 'Finland':
        print(f'O país {i} foi encontrado no índice {index}')
```

```sh
O país Finland foi encontrado no índice 0.
```

## Zip

Às vezes, gostaríamos de combinar listas ao percorrê-las. Veja o exemplo abaixo:

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
```

```sh
[{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]
```

🌕 Você está determinado. Está 17 passos à frente no caminho para a grandeza. Agora faça alguns exercícios para o cérebro e para os músculos.

## Exercicios: Dia 17

1. names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Desempacote os primeiros cinco países e armazene-os em uma variável nordic_countries, armazene Estonia e Russia em es e ru, respectivamente.


🎉 PARABÉNS ! 🎉

[<< Dia 16](../16_Dia_Datetime/README.md) | [Dia 18 >>](../18_Dia_Expressoes_Regulares/README.md)
