<div align="center">
  <h1> 30 Dias de Python: Dia 16 - Datetime </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Author:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small>Segunda edição: July, 2021</small>
  </sub>
</div>

[<< Dia 15](../15_Dia_Tipos_de_Erros/README.md) | [Dia 17 >>](../17_Dia_Tratamento_de_Excecoes/README.md)

![30DiasDePython](../../images/30DaysOfPython_banner3@2x.png)
- [📘 Dia 16](#-dia-16)
  - [Python *datetime*](#python-datetime)
    - [Obtendo Informacoes de *datetime*](#obtendo-informacoes-de-datetime)
    - [Formatando a Saida de Data com *strftime*](#formatando-a-saida-de-data-com-strftime)
    - [String para Tempo com *strptime*](#string-para-tempo-com-strptime)
    - [Usando *date* de *datetime*](#usando-date-de-datetime)
    - [Objetos Time para Representar Tempo](#objetos-time-para-representar-tempo)
    - [Diferenca Entre Dois Pontos no Tempo Usando](#diferenca-entre-dois-pontos-no-tempo-usando)
    - [Diferenca Entre Dois Pontos no Tempo Usando *timedelta*](#diferenca-entre-dois-pontos-no-tempo-usando-timedelta)
  - [💻 Exercicios: Dia 16](#-exercicios-dia-16)
# 📘 Dia 16

## Python *datetime*

O Python tem o módulo _datetime_ para lidar com data e hora.

```py
import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```

Com os comandos built-in dir ou help, é possível conhecer as funções disponíveis em um determinado módulo. Como você pode ver, no módulo datetime há muitas funções, mas vamos focar em _date_, _datetime_, _time_ e _timedelta_. Vamos vê-las uma a uma.

### Obtendo Informacoes de *datetime*

```py
from datetime import datetime
now = datetime.now()
print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38
```

Timestamp ou Unix timestamp é o número de segundos decorridos desde 1º de janeiro de 1970 UTC.

### Formatando a Saida de Data com *strftime*

```py
from datetime import datetime
new_year = datetime(2020, 1, 1)
print(new_year)      # 2020-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) #1 1 2020 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0

```

Formatando data e hora com o método *strftime*; a documentação pode ser encontrada [aqui](https://strftime.org/).

```py
from datetime import datetime
# data e hora atuais
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("hora:", t)           # hora: 18:21:40
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# formato mm/dd/YY H:M:S
print("hora um:", time_one)        # hora um: 06/28/2022, 18:21:40
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# formato dd/mm/YY H:M:S
print("hora dois:", time_two)        # hora dois: 28/06/2022, 18:21:40
```

```sh
hora: 01:05:01
hora um: 12/05/2019, 01:05:01
hora dois: 05/12/2019, 01:05:01
```

Aqui estão todos os símbolos _strftime_ que usamos para formatar o tempo. Um exemplo de todos os formatos deste módulo.

![strftime](../../images/strftime.png)

### String para Tempo com *strptime*
Aqui está uma [documentação](https://www.programiz.com/python-programming/datetime/strptime) que ajuda a entender o formato. 

```py
from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)     # date_string = 5 December, 2019
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)     # date_object = 2019-12-05 00:00:00
```

```sh
date_string = 5 December, 2019
date_object = 2019-12-05 00:00:00
```

### Usando *date* de *datetime*

```py
from datetime import date
d = date(2020, 1, 1)
print(d)        # 2020-01-01
print('Data atual:', d.today())    # 2019-12-05
# objeto date da data de hoje
today = date.today()
print("Ano atual:", today.year)   # 2019
print("Mês atual:", today.month) # 12
print("Dia atual:", today.day)     # 5
```

### Objetos Time para Representar Tempo

```py
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)     # a = 00:00:00
# time(hora, minuto e segundo)
b = time(10, 30, 50)
print("b =", b)     # b = 10:30:50
# time(hora, minuto e segundo)
c = time(hour=10, minute=30, second=50)
print("c =", c)     # c = 10:30:50
# time(hora, minuto, segundo, microssegundo)
d = time(10, 30, 50, 200555)
print("d =", d)     # d = 10:30:50.200555
```

saída  
a = 00:00:00  
b = 10:30:50  
c = 10:30:50  
d = 10:30:50.200555

### Diferenca Entre Dois Pontos no Tempo Usando

```py
from datetime import date, datetime
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Tempo restante para o ano novo:  27 days, 0:00:00
print('Tempo restante para o ano novo: ', time_left_for_newyear)  # Tempo restante para o ano novo:  27 days, 0:00:00

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Tempo restante para o ano novo:', diff) # Tempo restante para o ano novo: 26 days, 23: 01: 00
```

### Diferenca Entre Dois Pontos no Tempo Usando *timedelta*

```py
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
```

```sh
    date_string = 5 December, 2019
    date_object = 2019-12-05 00:00:00
    t3 = 86 days, 22:56:50
```

🌕 Você é extraordinário. Está 16 passos à frente no caminho para a grandeza. Agora faça alguns exercícios para o cérebro e para os músculos.

## 💻 Exercicios: Dia 16

1. Obtenha o dia, mês, ano, hora, minuto e timestamp atuais do módulo datetime
2. Formate a data atual usando este formato: "%m/%d/%Y, %H:%M:%S")
3. Hoje é 5 December, 2019. Transforme esta string de tempo em time.
4. Calcule a diferença de tempo entre agora e o ano novo.
5. Calcule a diferença de tempo entre 1 January 1970 e agora.
6. Pense: para que você pode usar o módulo datetime? Exemplos:
   - Análise de séries temporais
   - Obter um timestamp de quaisquer atividades em uma aplicação
   - Adicionar posts em um blog 

🎉 PARABÉNS ! 🎉

[<< Dia 15](../15_Dia_Tipos_de_Erros/README.md) | [Dia 17 >>](../17_Dia_Tratamento_de_Excecoes/README.md)
