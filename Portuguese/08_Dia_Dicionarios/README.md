<div align="center">
  <h1> 30 Dias de Python: Dia 8 - Dicionarios</h1>
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

[<< Dia 7](../07_Dia_Conjuntos/README.md) | [Dia 9 >>](../09_Dia_Condicionais/README.md)

![30DiasDePython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 8](#-dia-8)
  - [Dicionários](#dicionários)
    - [Criando um dicionário](#criando-um-dicionário)
    - [Tamanho do dicionário](#tamanho-do-dicionário)
    - [Acessando itens do dicionário](#acessando-itens-do-dicionário)
    - [Adicionando itens a um dicionário](#adicionando-itens-a-um-dicionário)
    - [Modificando itens em um dicionário](#modificando-itens-em-um-dicionário)
    - [Verificando chaves em um dicionário](#verificando-chaves-em-um-dicionário)
    - [Removendo pares chave-valor de um dicionário](#removendo-pares-chave-valor-de-um-dicionário)
    - [Convertendo um dicionário em uma lista de itens](#convertendo-um-dicionário-em-uma-lista-de-itens)
    - [Limpando um dicionário](#limpando-um-dicionário)
    - [Excluindo um dicionário](#excluindo-um-dicionário)
    - [Copiando um dicionário](#copiando-um-dicionário)
    - [Obtendo as chaves do dicionário como lista](#obtendo-as-chaves-do-dicionário-como-lista)
    - [Obtendo os valores do dicionário como lista](#obtendo-os-valores-do-dicionário-como-lista)
  - [💻 Exercícios: Dia 8](#-exercícios-dia-8)

# 📘 Dia 8

## Dicionários

Um dicionário é uma coleção não ordenada, modificável (mutável) e formada por pares (chave: valor).

### Criando um dicionário

Para criar um dicionário, usamos chaves `{}` ou a função built-in *dict()*.

```py
# sintaxe
empty_dict = {}
# Dicionário com valores
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
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
```

O dicionário acima mostra que um valor pode ser de qualquer tipo de dado: string, boolean, list, tuple, set ou até outro dicionário.

### Tamanho do dicionário

O tamanho indica quantos pares `chave: valor` o dicionário possui.

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
```

**Exemplo:**

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(len(person)) # 7

```

### Acessando itens do dicionário

Você acessa os itens de um dicionário pelo nome da chave.

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
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
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
print(person['city'])       # Erro
```

Acessar um item pelo nome da chave gera um erro se a chave não existir. Para evitar isso, primeiro verifique se a chave existe ou use o método _get_. O método get retorna None (um objeto do tipo NoneType) quando a chave não existe.
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
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None
```

### Adicionando itens a um dicionário

Você pode adicionar novos pares chave-valor a um dicionário.

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
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
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)
```

### Modificando itens em um dicionário

Você pode modificar itens em um dicionário.

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
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
person['first_name'] = 'Eyob'
person['age'] = 252
```

### Verificando chaves em um dicionário

Usamos o operador _in_ para verificar se uma chave existe em um dicionário.

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
```

### Removendo pares chave-valor de um dicionário

- _pop(key)_: remove o item com o nome da chave informado
- _popitem()_: remove o último item
- _del_: remove um item com o nome da chave informado

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # remove o item key1
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # remove o último item
del dct['key2'] # remove o item key2
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
person.pop('first_name')        # Remove o item first_name
person.popitem()                # Remove o item address
del person['is_married']        # Remove o item is_married
```

### Convertendo um dicionário em uma lista de itens

O método _items()_ transforma o dicionário em uma lista de tuplas.

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```

### Limpando um dicionário

Se você não quiser mais os itens de um dicionário, pode limpá-los com o método _clear()_.

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None
```

### Excluindo um dicionário

Se você não for mais usar o dicionário, pode excluí-lo por completo.

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
```

### Copiando um dicionário

Você pode copiar um dicionário com o método _copy()_. Assim, evita alterar o dicionário original por engano.

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

### Obtendo as chaves do dicionário como lista

O método _keys()_ devolve todas as chaves do dicionário como uma lista.

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
```

### Obtendo os valores do dicionário como lista

O método _values()_ devolve todos os valores do dicionário como uma lista.

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
```

🌕 Você está incrível. Agora você está turbinado com o poder dos dicionários. Você acabou de concluir os desafios do dia 8 e está 8 passos à frente no caminho para a grandeza. Agora faça alguns exercícios para o cérebro e para os músculos.

## 💻 Exercícios: Dia 8

1. Crie um dicionário vazio chamado dog
2. Adicione name, color, breed, legs e age ao dicionário dog
3. Crie um dicionário student e adicione first_name, last_name, gender, age, marital status, skills, country, city e address como chaves
4. Obtenha o tamanho do dicionário student
5. Obtenha o valor de skills e verifique o tipo de dado — deve ser uma lista
6. Modifique os valores de skills adicionando uma ou duas habilidades
7. Obtenha as chaves do dicionário como uma lista
8. Obtenha os valores do dicionário como uma lista
9. Transforme o dicionário em uma lista de tuplas usando o método _items()_
10. Delete um dos itens do dicionário
11. Delete um dos dicionários

🎉 PARABÉNS! 🎉

[<< Dia 7](../07_Dia_Conjuntos/README.md) | [Dia 9 >>](../09_Dia_Condicionais/README.md)
