<div align="center">
  <h1> 30 Dias de Python: Dia 9 - Condicionais</h1>
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

[<< Dia 8](../08_Dia_Dicionarios/README.md) | [Dia 10 >>](../10_Dia_Loops/README.md)

![30DiasDePython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 9](#-dia-9)
  - [Condicionais](#condicionais)
    - [Condição If](#condição-if)
    - [If Else](#if-else)
    - [If Elif Else](#if-elif-else)
    - [Forma curta](#forma-curta)
    - [Condições aninhadas](#condições-aninhadas)
    - [If com operadores lógicos and](#if-com-operadores-lógicos-and)
    - [If com operadores lógicos or](#if-com-operadores-lógicos-or)
  - [💻 Exercícios: Dia 9](#-exercícios-dia-9)
    - [Exercícios: Nível 1](#exercícios-nível-1)
    - [Exercícios: Nível 2](#exercícios-nível-2)
    - [Exercícios: Nível 3](#exercícios-nível-3)

# 📘 Dia 9

## Condicionais

Por padrão, as instruções em um script Python são executadas sequencialmente, de cima para baixo. Se a lógica do programa exigir, esse fluxo pode ser alterado de duas formas:

- Execução condicional: um bloco de uma ou mais instruções é executado se determinada expressão for verdadeira
- Execução repetitiva: um bloco de uma ou mais instruções é executado repetidamente enquanto determinada expressão for verdadeira. Nesta seção, vamos cobrir as instruções _if_, _else_ e _elif_. Os operadores de comparação e lógicos que você aprendeu nas seções anteriores serão úteis aqui.

### Condição If

Em Python e em outras linguagens de programação, a palavra-chave _if_ é usada para verificar se uma condição é verdadeira e executar o bloco de código. Lembre-se da indentação depois dos dois-pontos.

```py
# sintaxe
if condition:
    esta parte do código roda para condições verdadeiras
```

**Exemplo: 1**

```py
a = 3
if a > 0:
    print('A é um número positivo')
# A é um número positivo
```

Como você viu no exemplo acima, 3 é maior que 0. A condição era verdadeira e o bloco de código foi executado. Porém, se a condição for falsa, você não vê nenhum resultado. Para tratar o caso falso, precisamos de outro bloco: o _else_.

### If Else

Se a condição for verdadeira, o primeiro bloco é executado; caso contrário, o bloco else roda.

```py
# sintaxe
if condition:
    esta parte do código roda para condições verdadeiras
else:
     esta parte do código roda para condições falsas
```

**Exemplo:**

```py
a = 3
if a < 0:
    print('A é um número negativo')
else:
    print('A é um número positivo')
```

A condição acima resulta em falso; por isso, o bloco else foi executado. E se tivermos mais de duas possibilidades? Aí usamos _elif_.

### If Elif Else

No dia a dia, tomamos decisões o tempo todo. Não checamos só uma ou duas condições, e sim várias. Assim como na vida, a programação também é cheia de condições. Usamos _elif_ quando temos múltiplas condições.

```py
# sintaxe
if condition:
    código
elif condition:
    código
else:
    código

```

**Exemplo:**

```py
a = 0
if a > 0:
    print('A é um número positivo')
elif a < 0:
    print('A é um número negativo')
else:
    print('A é zero')
```

### Forma curta

```py
# sintaxe
código if condition else código
```

**Exemplo:**

```py
a = 3
print('A é positivo') if a > 0 else print('A é negativo') # primeira condição atendida, 'A é positivo' será impresso
```

### Condições aninhadas

As condições podem ser aninhadas.

```py
# sintaxe
if condition:
    código
    if condition:
    código
```

**Exemplo:**

```py
a = 0
if a > 0:
    if a % 2 == 0:
        print('A é um inteiro positivo e par')
    else:
        print('A é um número positivo')
elif a == 0:
    print('A é zero')
else:
    print('A é um número negativo')

```

Você pode evitar escrever condições aninhadas usando o operador lógico _and_.

### If com operadores lógicos and

```py
# sintaxe
if condition and condition:
    código
```

**Exemplo:**

```py
a = 0
if a > 0 and a % 2 == 0:
        print('A é um inteiro positivo e par')
elif a > 0 and a % 2 !=  0:
     print('A é um inteiro positivo')
elif a == 0:
    print('A é zero')
else:
    print('A é negativo')
```

### If com operadores lógicos or

```py
# sintaxe
if condition or condition:
    código
```

**Exemplo:**

```py
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Acesso concedido!')
else:
    print('Acesso negado!')
```

🌕 Você está indo muito bem. Nunca desista, porque coisas grandes levam tempo. Você acabou de concluir os desafios do dia 9 e está 9 passos à frente no caminho para a grandeza. Agora faça alguns exercícios para o cérebro e para os músculos.

## 💻 Exercícios: Dia 9

### Exercícios: Nível 1

1. Obtenha a entrada do usuário com input("Digite sua idade: "). Se o usuário tiver 18 anos ou mais, dê o feedback: Você tem idade suficiente para dirigir. Se tiver menos de 18, diga para esperar a quantidade de anos que faltam. Saída:

    ```sh
    Digite sua idade: 30
    Você tem idade suficiente para aprender a dirigir.
    Saída:
    Digite sua idade: 15
    Você precisa de mais 3 anos para aprender a dirigir.
    ```

2. Compare os valores de my_age e your_age usando if … else. Quem é mais velho (eu ou você)? Use input("Digite sua idade: ") para obter a idade. Você pode usar uma condição aninhada para imprimir 'ano' quando a diferença for de 1 ano, 'anos' para diferenças maiores, e um texto personalizado se my_age = your_age. Saída:

    ```sh
    Digite sua idade: 30
    Você é 5 anos mais velho do que eu.
    ```

3. Obtenha dois números do usuário com input. Se a for maior que b, retorne a é maior que b; se a for menor que b, retorne a é menor que b; caso contrário, a é igual a b. Saída:

```sh
Digite o primeiro número: 4
Digite o segundo número: 3
4 é maior que 3
```

### Exercícios: Nível 2

   1. Escreva um código que atribua notas aos estudantes de acordo com as pontuações:

    ```sh
    90-100, A
    80-89, B
    70-79, C
    60-69, D
    0-59, F
    ```

   2. Obtenha o mês pela entrada do usuário e verifique se a estação é Outono, Inverno, Primavera ou Verão. Se a entrada for:
    September, October ou November, a estação é Outono.
    December, January ou February, a estação é Inverno.
    March, April ou May, a estação é Primavera.
    June, July ou August, a estação é Verão.
   3. A lista a seguir contém algumas frutas:

    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```

    Se a fruta não existir na lista, adicione-a e imprima a lista modificada. Se a fruta já existir, imprima print('Essa fruta já existe na lista')

### Exercícios: Nível 3

   1. Aqui temos um dicionário person. Sinta-se à vontade para modificá-lo!

```py
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
```

     * Verifique se o dicionário person tem a chave skills; se tiver, imprima a habilidade do meio da lista skills.
     * Verifique se o dicionário person tem a chave skills; se tiver, confira se a pessoa tem a habilidade 'Python' e imprima o resultado.
     * Se as skills da pessoa forem apenas JavaScript e React, imprima print('Ele é um desenvolvedor front end'); se tiver Node, Python e MongoDB, imprima print('Ele é um desenvolvedor backend'); se tiver React, Node e MongoDB, imprima print('Ele é um desenvolvedor fullstack'); caso contrário, imprima print('título desconhecido') — para resultados mais precisos, você pode aninhar mais condições!
     * Se a pessoa for casada e mora na Finlândia, imprima as informações no seguinte formato:

```py
    Asabeneh Yetayeh lives in Finland. He is married.
```

🎉 PARABÉNS! 🎉

[<< Dia 8](../08_Dia_Dicionarios/README.md) | [Dia 10 >>](../10_Dia_Loops/README.md)
