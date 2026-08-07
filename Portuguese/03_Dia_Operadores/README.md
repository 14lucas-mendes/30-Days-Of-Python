<div align="center">
  <h1> 30 Dias de Python: Dia 3 - Operadores</h1>
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

[<< Dia 2](../02_Dia_Variaveis_BuiltIn_Functions/README.md) | [Dia 4 >>](../04_Dia_Strings/README.md)

![30DiasDePython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 3](#-dia-3)
  - [Boolean](#boolean)
  - [Operadores](#operadores)
    - [Operadores de atribuição](#operadores-de-atribuição)
    - [Operadores aritméticos](#operadores-aritméticos)
    - [Operadores de comparação](#operadores-de-comparação)
    - [Operadores lógicos](#operadores-lógicos)
  - [💻 Exercícios - Dia 3](#-exercícios---dia-3)

# 📘 Dia 3

## Boolean

Um tipo de dado booleano representa um de dois valores: _True_ ou _False_. O uso desses tipos fica mais claro quando começamos a usar operadores de comparação. A primeira letra **T** de True e **F** de False deve ser maiúscula, ao contrário do JavaScript.
**Exemplo: valores booleanos**

```py
print(True)
print(False)
```

## Operadores

A linguagem Python oferece suporte a vários tipos de operadores. Nesta seção, vamos focar em alguns deles.

### Operadores de atribuição

Os operadores de atribuição são usados para atribuir valores a variáveis. Vamos pegar o `=` como exemplo. Em matemática, o sinal de igual indica que dois valores são iguais; em Python, porém, ele significa que estamos armazenando um valor em determinada variável — chamamos isso de atribuição, ou de atribuir um valor a uma variável. A tabela abaixo mostra os diferentes tipos de operadores de atribuição do Python, retirada do [w3school](https://www.w3schools.com/python/python_operators.asp).

![Operadores de atribuição](../../images/assignment_operators.png)

### Operadores aritméticos

- Adição(+): a + b
- Subtração(-): a - b
- Multiplicação(*): a * b
- Divisão(/): a / b
- Módulo(%): a % b
- Divisão inteira(//): a // b
- Exponenciação(**): a ** b

![Operadores aritméticos](../../images/arithmetic_operators.png)

**Exemplo: inteiros**

```py
# Operações aritméticas em Python
# Inteiros

print('Adição: ', 1 + 2)        # 3
print('Subtração: ', 2 - 1)     # 1
print('Multiplicação: ', 2 * 3)  # 6
print ('Divisão: ', 4 / 2)       # 2.0  A divisão em Python retorna número decimal (float)
print('Divisão: ', 6 / 2)        # 3.0         
print('Divisão: ', 7 / 2)        # 3.5
print('Divisão sem o resto: ', 7 // 2)   # 3, retorna sem a parte decimal ou sem o resto
print ('Divisão sem o resto: ',7 // 3)   # 2
print('Módulo: ', 3 % 2)         # 1, retorna o resto
print('Exponenciação: ', 2 ** 3) # 8, significa 2 * 2 * 2
```

**Exemplo: floats**

```py
# Números decimais (ponto flutuante)
print('Número decimal, PI', 3.14)
print('Número decimal, gravidade', 9.81)
```

**Exemplo: números complexos**

```py
# Números complexos
print('Número complexo: ', 1 + 1j)
print('Multiplicando números complexos: ',(1 + 1j) * (1 - 1j))
```

Vamos declarar uma variável e atribuir um tipo numérico. Vou usar variáveis de um único caractere, mas lembre-se: não crie o hábito de declarar variáveis desse jeito. Os nomes das variáveis devem ser, sempre que possível, mnemônicos.

**Exemplo:**

```python
# Declarando as variáveis no topo, primeiro

a = 3 # a é um nome de variável e 3 é um tipo de dado inteiro
b = 2 # b é um nome de variável e 2 é um tipo de dado inteiro

# Operações aritméticas e atribuição do resultado a uma variável
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# Eu deveria ter usado sum em vez de total, mas sum é uma função nativa — evite sobrescrever funções nativas
print(total) # se você não rotular o print com alguma string, nunca sabe de onde veio o resultado
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)
```

**Exemplo:**

```py
print('== Adição, Subtração, Multiplicação, Divisão, Módulo ==')

# Declarando valores e organizando-os juntos
num_one = 3
num_two = 4

# Operações aritméticas
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Imprimindo valores com rótulo
print('total: ', total)
print('diferença: ', diff)
print('produto: ', product)
print('divisão: ', div)
print('resto: ', remainder)
```

Vamos começar a conectar os pontos e usar o que já sabemos para calcular (área, volume, densidade, peso, perímetro, distância, força).

**Exemplo:**

```py
# Calculando a área de um círculo
radius = 10                                 # raio de um círculo
area_of_circle = 3.14 * radius ** 2         # dois sinais * significam expoente ou potência
print('Área de um círculo:', area_of_circle)

# Calculando a área de um retângulo
length = 10
width = 20
area_of_rectangle = length * width
print('Área do retângulo:', area_of_rectangle)

# Calculando o peso de um objeto
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adicionando a unidade ao peso

# Calculando a densidade de um líquido
mass = 75 # em Kg
volume = 0.075 # em metro cúbico
density = mass / volume # 1000 Kg/m^3
print(density, 'Kg/m^3') # Adicionando a unidade à densidade

```

### Operadores de comparação

Na programação, comparamos valores; usamos operadores de comparação para comparar dois valores. Verificamos se um valor é maior, menor ou igual a outro. A tabela a seguir mostra os operadores de comparação do Python, retirada do [w3shool](https://www.w3schools.com/python/python_operators.asp).

![Operadores de comparação](../../images/comparison_operators.png)
**Exemplo: operadores de comparação**

```py
print(3 > 2)     # True, porque 3 é maior que 2
print(3 >= 2)    # True, porque 3 é maior que 2
print(3 < 2)     # False, porque 3 é maior que 2
print(2 < 3)     # True, porque 2 é menor que 3
print(2 <= 3)    # True, porque 2 é menor que 3
print(3 == 2)    # False, porque 3 não é igual a 2
print(3 != 2)    # True, porque 3 não é igual a 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparar algo resulta em True ou False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
```

Além dos operadores de comparação acima, o Python usa:

- _is_: Retorna true se ambas as variáveis forem o mesmo objeto (x is y)
- _is not_: Retorna true se ambas as variáveis não forem o mesmo objeto (x is not y)
- _in_: Retorna True se a lista consultada contiver determinado item (x in y)
- _not in_: Retorna True se a lista consultada não tiver determinado item (x not in y)

```py
print('1 is 1', 1 is 1)                   # True - porque os valores dos dados são os mesmos
print('1 is not 2', 1 is not 2)           # True - porque 1 não é 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A encontrado na string
print('B not in Asabeneh', 'B' in 'Asabeneh') # False - não há B maiúsculo
print('coding' in 'coding for all') # True - porque coding for all tem a palavra coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True
```

### Operadores lógicos

Diferente de outras linguagens de programação, o Python usa as palavras-chave _and_, _or_ e _not_ para operadores lógicos. Os operadores lógicos são usados para combinar declarações condicionais:

![Operadores lógicos](../../images/logical_operators.png)

```py
print(3 > 2 and 4 > 3) # True - porque ambas as declarações são verdadeiras
print(3 > 2 and 4 < 3) # False - porque a segunda declaração é falsa
print(3 < 2 and 4 < 3) # False - porque ambas as declarações são falsas
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - porque ambas as declarações são verdadeiras
print(3 > 2 or 4 < 3)  # True - porque uma das declarações é verdadeira
print(3 < 2 or 4 < 3)  # False - porque ambas as declarações são falsas
print('True or False:', True or False)
print(not 3 > 2)     # False - porque 3 > 2 é verdadeiro, então not True resulta em False
print(not True)      # False - Negação: o operador not transforma true em false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

```

🌕 Sua energia não tem limites. Você acabou de concluir os desafios do dia 3 e está três passos à frente no caminho para a grandeza. Agora faça alguns exercícios para o cérebro e para os músculos.

## 💻 Exercícios - Dia 3

1. Declare sua idade como variável inteira
2. Declare sua altura como variável float
3. Declare uma variável que armazene um número complexo
4. Escreva um script que peça ao usuário a base e a altura do triângulo e calcule a área desse triângulo (área = 0.5 x b x h).

```py
    Digite a base: 20
    Digite a altura: 10
    A área do triângulo é 100
```

5. Escreva um script que peça ao usuário o lado a, o lado b e o lado c do triângulo. Calcule o perímetro do triângulo (perímetro = a + b + c).

```py
Digite o lado a: 5
Digite o lado b: 4
Digite o lado c: 3
O perímetro do triângulo é 12
```

6. Obtenha o comprimento e a largura de um retângulo usando prompt. Calcule sua área (área = comprimento x largura) e perímetro (perímetro = 2 x (comprimento + largura))
7. Obtenha o raio de um círculo usando prompt. Calcule a área (área = pi x r x r) e a circunferência (c = 2 x pi x r), onde pi = 3.14.
8. Calcule a inclinação (slope), a interseção com x e a interseção com y de y = 2x -2
9. A inclinação é (m = y2-y1/x2-x1). Encontre a inclinação e a [distância euclidiana](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) entre o ponto (2, 2) e o ponto (6,10)
10. Compare as inclinações das tarefas 8 e 9.
11. Calcule o valor de y (y = x^2 + 6x + 9). Experimente diferentes valores de x e descubra em qual valor de x y será 0.
12. Encontre o comprimento de 'python' e 'dragon' e faça uma comparação falsy.
13. Use o operador _and_ para verificar se 'on' está em 'python' e em 'dragon'
14. _I hope this course is not full of jargon_. Use o operador _in_ para verificar se _jargon_ está na frase.
15. Não há 'on' em dragon e em python
16. Encontre o comprimento do texto _python_, converta o valor para float e depois para string
17. Números pares são divisíveis por 2 e o resto é zero. Como você verifica se um número é par ou não usando Python?
18. Verifique se a divisão inteira de 7 por 3 é igual ao valor convertido para int de 2.7.
19. Verifique se o tipo de '10' é igual ao tipo de 10
20. Verifique se int('9.8') é igual a 10
21. Escreva um script que peça ao usuário as horas e a taxa por hora. Calcule o pagamento da pessoa.

```py
Digite as horas: 40
Digite a taxa por hora: 28
Seu ganho semanal é 1120
```

22. Escreva um script que peça ao usuário o número de anos. Calcule o número de segundos que uma pessoa pode viver. Considere que uma pessoa pode viver cem anos

```py
Digite o número de anos que você viveu: 100
Você viveu por 3153600000 segundos.
```

23. Escreva um script em Python que exiba a seguinte tabela

```py
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
```

🎉 PARABÉNS! 🎉

[<< Dia 2](../02_Dia_Variaveis_BuiltIn_Functions/README.md) | [Dia 4 >>](../04_Dia_Strings/README.md)
