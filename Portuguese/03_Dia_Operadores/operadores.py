idade = 34
altura = 1.85
num_cxomplexo = 5 + 3j


#area de um triangulo
base = int(input("Informe o valor da base do triangulo: "))
altura = int(input("Informe o valor da altura do traingulo: "))

def calcula_area(b, h):
    if b <= 0 or h <= 0:
        return "Valores inválidos, digite um valor válido!"
    
    area_triangulo = 0.5 * b * h
    
    return f"A area do triangulo é: {area_triangulo}"
    

print(calcula_area(base, altura))


#Perimetro de um triangulo
lado_a = int(input("Informe o valor de um dos 3 lados do triangulo: "))
lado_b = int(input("Informe o valor de um dos 3 lados do triangulo: "))
lado_c = int(input("Informe o valor de um dos 3 lados do triangulo: "))

def calcula_perimetro(a, b, c):
    if a <= 0 or b< 0 or c <= 0:
        return "Valores inválidos! Digite um número maior que zero."
    
    perimetro_trinagulo = a + b + c

    return f"O perimetro do triangulo é de: {perimetro_trinagulo}"

print(calcula_perimetro(lado_a, lado_b, lado_c))


#Area e perimetro de um retangulo
largura = int(input("Informe a largura do retangulo: "))
comprimento = int(input("Informe a comprimento do retangulo: "))

area_retangulo = comprimento * largura
perimetro = 2 * (comprimento + largura)
print(f"Area {area_retangulo} e perimetro {perimetro}")