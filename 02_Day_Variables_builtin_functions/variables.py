
# Dia 2/30 dias de programação em Python

import datetime

first_name = "Lucas"
last_name = "Mendes"
complete_name = first_name  + " " + last_name
pais = "Brasil"
cidade = "Suzano"
idade = 34
is_married = True
is_true = True
is_light_on = False
year = datetime.datetime.now().year

nome, pais, cidade, idade, is_married, is_true, is_light_on, year = "Lucas", "Brasil", "Suzano", 34, True, True, False, datetime.datetime.now().year
print(complete_name, pais, cidade, idade, is_married, is_true, is_light_on)

print(type(complete_name))
print(type(pais))
print(type(cidade))
print(type(idade))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(year))

print(len(complete_name))
print(pais)
print(cidade)
print(idade)
print(is_married)
print(is_true)
print(is_light_on)

print(type(complete_name))
print(type(pais))
print(type(cidade))
print(type(idade))

print(len(first_name), len(last_name), len(complete_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exponent = num_one ** num_two
division_floor = num_one // num_two
print(total, diff, product, division, remainder)


raio = int(input("Digite o raio do círculo: "))

area_circle = 3.14 * raio ** 2
print(area_circle)

_circum_circle = 2 * 3.14 * raio
print(_circum_circle)


first_name = input("Digite seu primeiro nome: ")
last_name = input("Digite seu sobrenome: ")
age = input("Digite sua idade: ")
city = input("Digite sua cidade: ")
country = input("Digite seu país: ")

full_name = first_name + " " + last_name
print(full_name)
print(age)
print(city)
print(country)



