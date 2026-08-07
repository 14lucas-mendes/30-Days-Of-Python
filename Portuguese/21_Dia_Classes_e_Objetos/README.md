<div align="center">
  <h1> 30 Dias de Python: Dia 21 - Classes e Objetos</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Autor:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>Segunda edição: July, 2021</small>
</sub>

</div>

[<< Dia 20](../20_Dia_Gerenciador_de_Pacotes/README.md) | [Dia 22 >>](../22_Dia_Web_Scraping/README.md)

![30DiasDePython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 21](#-dia-21)
  - [Classes e Objetos](#classes-e-objetos)
    - [Criando uma Classe](#criando-uma-classe)
    - [Criando um Objeto](#criando-um-objeto)
    - [Construtor da Classe](#construtor-da-classe)
    - [Métodos do Objeto](#métodos-do-objeto)
    - [Métodos Padrão do Objeto](#métodos-padrão-do-objeto)
    - [Método para Modificar Valores Padrão da Classe](#método-para-modificar-valores-padrão-da-classe)
    - [Herança](#herança)
    - [Sobrescrevendo o método da classe pai](#sobrescrevendo-o-método-da-classe-pai)
  - [💻 Exercícios: Dia 21](#-exercícios-dia-21)
    - [Exercícios: Nível 1](#exercícios-nível-1)
    - [Exercícios: Nível 2](#exercícios-nível-2)
    - [Exercícios: Nível 3](#exercícios-nível-3)

# 📘 Dia 21

## Classes e Objetos

Python é uma linguagem de programação orientada a objetos. Tudo em Python é um objeto, com suas propriedades e métodos. Um número, string, lista, dicionário, tupla, conjunto etc. usados em um programa são objetos de uma classe built-in correspondente. Criamos uma classe para criar um objeto. Uma classe é como um construtor de objetos, ou um "modelo" para criar objetos. Instanciamos uma classe para criar um objeto. A classe define atributos e o comportamento do objeto, enquanto o objeto, por outro lado, representa a classe.

Temos trabalhado com classes e objetos desde o início deste desafio sem perceber. Todo elemento em um programa Python é um objeto de uma classe.
Vamos verificar se tudo em Python é uma classe:

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> num = 10
>>> type(num)
<class 'int'>
>>> string = 'string'
>>> type(string)
<class 'str'>
>>> boolean = True
>>> type(boolean)
<class 'bool'>
>>> lst = []
>>> type(lst)
<class 'list'>
>>> tpl = ()
>>> type(tpl)
<class 'tuple'>
>>> set1 = set()
>>> type(set1)
<class 'set'>
>>> dct = {}
>>> type(dct)
<class 'dict'>
```

### Criando uma Classe

Para criar uma classe precisamos da palavra-chave **class** seguida do nome e de dois-pontos. O nome da classe deve estar em **CamelCase**.

```sh
# sintaxe
class ClassName:
  o código vai aqui
```

**Exemplo:**

```py
class Person:
  pass
print(Person)
```

```sh
<__main__.Person object at 0x10804e510>
```

### Criando um Objeto

Podemos criar um objeto chamando a classe.

```py
p = Person()
print(p)
```

### Construtor da Classe

Nos exemplos acima, criamos um objeto a partir da classe Person. No entanto, uma classe sem construtor não é muito útil em aplicações reais. Vamos usar a função construtora para tornar nossa classe mais útil. Como a função construtora em Java ou JavaScript, o Python também tem uma função construtora built-in **__init__()**. O construtor **__init__** tem o parâmetro self, que é uma referência à instância atual da classe.
**Exemplos:**

```py
class Person:
      def __init__ (self, name):
        # self permite anexar o parâmetro à classe
          self.name =name

p = Person('Asabeneh')
print(p.name)
print(p)
```

```sh
# saída
Asabeneh
<__main__.Person object at 0x2abf46907e80>
```

Vamos adicionar mais parâmetros à função construtora.

```py
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)
```

```sh
# saída
Asabeneh
Yetayeh
250
Finland
Helsinki
```

### Métodos do Objeto

Objetos podem ter métodos. Os métodos são funções que pertencem ao objeto.

**Exemplo:**

```py
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())
```

```sh
# saída
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland
```

### Métodos Padrão do Objeto

Às vezes, você pode querer ter valores padrão para os métodos do seu objeto. Se dermos valores padrão aos parâmetros no construtor, podemos evitar erros quando chamamos ou instanciamos nossa classe sem parâmetros. Veja como fica:

**Exemplo:**

```py
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
```

```sh
# saída
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
John Doe is 30 years old. He lives in Noman city, Nomanland.
```

### Método para Modificar Valores Padrão da Classe

No exemplo abaixo, na classe person, todos os parâmetros do construtor têm valores padrão. Além disso, temos o parâmetro skills, ao qual podemos acessar usando um método. Vamos criar o método add_skill para adicionar habilidades à lista skills.

```py
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)
```

```sh
# saída
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
John Doe is 30 years old. He lives in Noman city, Nomanland.
['HTML', 'CSS', 'JavaScript']
[]
```

### Herança

Usando herança, podemos reutilizar o código da classe pai. A herança nos permite definir uma classe que herda todos os métodos e propriedades da classe pai. A classe pai, super ou base é a classe que fornece todos os métodos e propriedades. A classe filha é a classe que herda de outra classe ou da classe pai.
Vamos criar uma classe student herdando da classe person.

```py
class Student(Person):
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

```

```sh
saída
Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 years old. He lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

Não chamamos o construtor **__init__()** na classe filha. Se não o chamarmos, ainda podemos acessar todas as propriedades da classe pai. Mas se chamarmos o construtor, podemos acessar as propriedades do pai chamando _super_.
Podemos adicionar um novo método à filha ou sobrescrever os métodos da classe pai criando o mesmo nome de método na classe filha. Quando adicionamos a função **__init__()**, a classe filha deixa de herdar a função **__init__()** do pai.

### Sobrescrevendo o método da classe pai

```py
class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
```

```sh
Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 years old. She lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

Podemos usar a função built-in super() ou o nome do pai Person para herdar automaticamente os métodos e propriedades do pai. No exemplo acima, sobrescrevemos o método do pai. O método da filha tem um recurso diferente: ele identifica se o gênero é male ou female e atribui o pronome adequado (He/She).

🌕 Agora você está totalmente carregado com um superpoder de programação. Agora faça alguns exercícios para o cérebro e para os músculos.

## 💻 Exercícios: Dia 21

### Exercícios: Nível 1

1. O Python tem o módulo chamado _statistics_ e podemos usá-lo para fazer todos os cálculos estatísticos. No entanto, para aprender a criar funções e reutilizá-las, vamos tentar desenvolver um programa que calcule as medidas de tendência central de uma amostra (média, mediana, moda) e as medidas de variabilidade (amplitude, variância, desvio padrão). Além dessas medidas, encontre o mínimo, máximo, contagem, percentil e a distribuição de frequência da amostra. Você pode criar uma classe chamada Statistics e criar todas as funções que fazem os cálculos estatísticos como métodos da classe Statistics. Confira a saída abaixo.

```py
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```

```sh
# sua saída deve se parecer com isto
print(data.describe())
Count: 25
Sum:  744
Min:  24
Max:  38
Range:  14
Mean:  30
Median:  29
Mode:  (26, 5)
Variance:  17.5
Standard Deviation:  4.2
Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```

### Exercícios: Nível 2

1. Crie uma classe chamada PersonAccount. Ela tem as propriedades firstname, lastname, incomes e expenses e os métodos total_income, total_expense, account_info, add_income, add_expense e account_balance. Incomes é um conjunto de rendas e suas descrições. O mesmo vale para expenses.

### Exercícios: Nível 3

🎉 PARABÉNS! 🎉

[<< Dia 20](../20_Dia_Gerenciador_de_Pacotes/README.md) | [Dia 22 >>](../22_Dia_Web_Scraping/README.md)
