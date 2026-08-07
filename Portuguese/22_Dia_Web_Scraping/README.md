<div align="center">
  <h1> 30 Dias de Python: Dia 22 - Web Scraping </h1>
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

[<< Dia 21](../21_Dia_Classes_e_Objetos/README.md) | [Dia 23 >>](../23_Dia_Ambiente_Virtual/README.md)

![30DiasDePython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 22](#-dia-22)
  - [Web Scraping com Python](#web-scraping-com-python)
    - [O que é Web Scraping](#o-que-é-web-scraping)
  - [💻 Exercícios: Dia 22](#-exercícios-dia-22)

# 📘 Dia 22

## Web Scraping com Python

### O que é Web Scraping

A internet está cheia de uma enorme quantidade de dados que podem ser usados para diferentes propósitos. Para coletar esses dados, precisamos saber como extrair dados de um site.

Web scraping é o processo de extrair e coletar dados de sites e armazená-los em uma máquina local ou em um banco de dados.

Nesta seção, vamos usar os pacotes beautifulsoup e requests para fazer scraping de dados. A versão do pacote que estamos usando é beautifulsoup 4.

Para começar a fazer scraping de sites, você precisa de _requests_, _beautifoulSoup4_ e um _site_.

```sh
pip install requests
pip install beautifulsoup4
```

Para extrair dados de sites, é necessário um entendimento básico de tags HTML e seletores CSS. Miramos o conteúdo de um site usando tags HTML, classes e/ou ids.
Vamos importar os módulos requests e BeautifulSoup

```py
import requests
from bs4 import BeautifulSoup
```

Vamos declarar a variável url do site do qual vamos extrair dados.

```py

import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Vamos usar o método get do requests para buscar os dados da url

response = requests.get(url)
# vamos verificar o status
status = response.status_code
print(status) # 200 significa que a busca foi bem-sucedida
```

```sh
200
```

Usando o BeautifulSoup para fazer o parse do conteúdo da página

```py
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # obtemos todo o conteúdo do site
soup = BeautifulSoup(content, 'html.parser') # o beautiful soup nos permite fazer o parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # devolve a página inteira do site
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# Estamos mirando a tabela com o atributo cellpadding de valor 3
# Podemos selecionar usando id, class ou tag HTML; para mais informações, consulte a documentação do beautifulsoup
table = tables[0] # o resultado é uma lista; estamos pegando os dados dela
for td in table.find('tr').find_all('td'):
    print(td.text)
```

Se você executar este código, verá que a extração está pela metade. Você pode continuar, pois isso faz parte do exercício 1.
Para referência, consulte a [documentação do beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)

🌕 Você é especial e está progredindo todos os dias. Restam apenas oito dias no seu caminho para a grandeza. Agora faça alguns exercícios para o cérebro e para os músculos.

## 💻 Exercícios: Dia 22

1. Faça o scrape do seguinte site e armazene os dados como arquivo json (url = 'http://www.bu.edu/president/boston-university-facts-stats/').
1. Extraia a tabela desta url (https://archive.ics.uci.edu/ml/datasets.php) e converta-a em um arquivo json
2. Faça o scrape da tabela de presidentes e armazene os dados como json (https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). A tabela não é muito estruturada e o scraping pode demorar bastante.

🎉 PARABÉNS! 🎉

[<< Dia 21](../21_Dia_Classes_e_Objetos/README.md) | [Dia 23 >>](../23_Dia_Ambiente_Virtual/README.md)
