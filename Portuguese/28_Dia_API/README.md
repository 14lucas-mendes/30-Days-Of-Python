<div align="center">
  <h1> 30 Dias de Python: Dia 28 - API </h1>
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
</div>

[<< Dia 27](../27_Dia_Python_com_MongoDB/README.md) | [Dia 29 >>](../29_Dia_Construindo_APIs/README.md)

![30DiasDePython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 28](#-dia-28)
- [Application Programming Interface(API)](#application-programming-interfaceapi)
  - [API](#api)
  - [Construindo API](#construindo-api)
  - [HTTP(Hypertext Transfer Protocol)](#httphypertext-transfer-protocol)
  - [Estrutura do HTTP](#estrutura-do-http)
  - [Linha Inicial da Requisição(Status Line)](#linha-inicial-da-requisiçãostatus-line)
    - [Linha Inicial da Resposta(Status Line)](#linha-inicial-da-respostastatus-line)
    - [Campos de Header](#campos-de-header)
    - [O corpo da mensagem](#o-corpo-da-mensagem)
    - [Métodos de Requisição](#métodos-de-requisição)
  - [💻 Exercícios: Dia 28](#-exercícios-dia-28)

# 📘 Dia 28

# Application Programming Interface(API)

## API

API significa Application Programming Interface (Interface de Programação de Aplicações). O tipo de API que vamos cobrir nesta seção serão as Web APIs.
Web APIs são as interfaces definidas por meio das quais acontecem as interações entre uma empresa e as aplicações que usam seus ativos, o que também é um Service Level Agreement (SLA) para especificar o provedor funcional e expor o caminho do serviço ou a URL para os usuários da sua API.

No contexto do desenvolvimento web, uma API é definida como um conjunto de especificações, como mensagens de requisição Hypertext Transfer Protocol (HTTP), juntamente com uma definição da estrutura das mensagens de resposta, geralmente em formato XML ou JavaScript Object Notation (JSON).

A Web API tem se afastado de web services baseados em Simple Object Access Protocol (SOAP) e de service-oriented architecture (SOA) em direção a recursos web no estilo representational state transfer (REST) de forma mais direta.

Nas redes sociais, as web APIs permitiram que comunidades web compartilhassem conteúdo e dados entre comunidades e plataformas diferentes.

Usando API, conteúdo que é criado em um lugar dinamicamente pode ser publicado e atualizado em vários locais na web.

Por exemplo, a REST API do Twitter permite que desenvolvedores acessem dados centrais do Twitter e a Search API fornece métodos para que desenvolvedores interajam com o Twitter Search e dados de trends.

Muitas aplicações fornecem endpoints de API. Alguns exemplos de API como a [API de países](https://restcountries.eu/rest/v2/all), [API de raças de gatos](https://api.thecatapi.com/v1/breeds).

Nesta seção, vamos cobrir uma RESTful API que usa métodos de requisição HTTP para GET, PUT, POST e DELETE de dados.

## Construindo API

RESTful API é uma application program interface (API) que usa requisições HTTP para GET, PUT, POST e DELETE de dados. Nas seções anteriores, aprendemos sobre Python, Flask e MongoDB. Vamos usar o conhecimento que adquirimos para desenvolver uma RESTful API usando Python Flask e banco de dados MongoDB. Toda aplicação que tem operação CRUD (Create, Read, Update, Delete) tem uma API para criar dados, obter dados, atualizar dados ou deletar dados de um banco de dados.

Para construir uma API, é bom entender o protocolo HTTP e o ciclo de requisição e resposta HTTP.

## HTTP(Hypertext Transfer Protocol)

HTTP é um protocolo de comunicação estabelecido entre um cliente e um servidor. Um cliente, neste caso, é um navegador e o servidor é o lugar onde você acessa os dados. HTTP é um protocolo de rede usado para entregar recursos que podem ser arquivos na World Wide Web, sejam eles arquivos HTML, arquivos de imagem, resultados de consulta, scripts ou outros tipos de arquivo.

Um navegador é um cliente HTTP porque envia requisições a um servidor HTTP (servidor Web), que então envia respostas de volta ao cliente.

## Estrutura do HTTP

HTTP usa o modelo cliente-servidor. Um cliente HTTP abre uma conexão e envia uma mensagem de requisição a um servidor HTTP e o servidor HTTP retorna uma mensagem de resposta que são os recursos solicitados. Quando o ciclo de requisição e resposta se completa, o servidor fecha a conexão.

![Ciclo de requisição e resposta HTTP](../../images/http_request_response_cycle.png)

O formato das mensagens de requisição e resposta é semelhante. Ambos os tipos de mensagens têm

- uma linha inicial,
- zero ou mais linhas de header,
- uma linha em branco (ou seja, um CRLF sozinho), e
- um corpo de mensagem opcional (por exemplo, um arquivo, ou dados de consulta, ou saída de consulta).

Vamos ver um exemplo de mensagens de requisição e resposta navegando neste site:https://thirtydaysofpython-v1-final.herokuapp.com/. Este site foi implantado no dyno gratuito do Heroku e em alguns meses pode não funcionar por causa de alta requisição. Apoie este trabalho para fazer o servidor rodar o tempo todo.

![Header de requisição e resposta](../../images/request_response_header.png)

## Linha Inicial da Requisição(Status Line)

A linha inicial da requisição é diferente da resposta.
Uma linha de requisição tem três partes, separadas por espaços:

- nome do método(GET, POST, HEAD)
- caminho do recurso solicitado,
- a versão do HTTP que está sendo usada. ex GET / HTTP/1.1

GET é o HTTP mais comum que ajuda a obter ou ler recurso e POST é um método de requisição comum para criar recurso.

### Linha Inicial da Resposta(Status Line)

A linha inicial da resposta, chamada status line, também tem três partes separadas por espaços:

- Versão HTTP
- Código de status da resposta que dá o resultado da requisição, e um reason que descreve o código de status. Exemplos de status lines são:
  HTTP/1.0 200 OK
  ou
  HTTP/1.0 404 Not Found
  Observações:

Os códigos de status mais comuns são:
200 OK: A requisição teve sucesso, e o recurso resultante (por exemplo, arquivo ou saída de script) é retornado no corpo da mensagem.
500 Server Error
Uma lista completa de códigos de status HTTP pode ser encontrada [aqui](https://httpstatuses.com/). Também pode ser encontrada [aqui](https://httpstatusdogs.com/).

### Campos de Header

Como você viu na captura de tela acima, as linhas de header fornecem informações sobre a requisição ou resposta, ou sobre o objeto enviado no corpo da mensagem.

```sh
GET / HTTP/1.1
Host: thirtydaysofpython-v1-final.herokuapp.com
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36
Sec-Fetch-User: ?1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Referer: https://thirtydaysofpython-v1-final.herokuapp.com/post
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en;q=0.9,fi-FI;q=0.8,fi;q=0.7,en-CA;q=0.6,en-US;q=0.5,fr;q=0.4
```

### O corpo da mensagem

Uma mensagem HTTP pode ter um corpo de dados enviado após as linhas de header. Em uma resposta, é aqui que o recurso solicitado é retornado ao cliente (o uso mais comum do corpo da mensagem), ou talvez texto explicativo se houver um erro. Em uma requisição, é aqui que dados inseridos pelo usuário ou arquivos enviados são enviados ao servidor.

Se uma mensagem HTTP inclui um corpo, geralmente há linhas de header na mensagem que descrevem o corpo. Em particular,

O header Content-Type: dá o MIME-type dos dados no corpo(text/html, application/json, text/plain, text/css, image/gif).
O header Content-Length: dá o número de bytes no corpo.

### Métodos de Requisição

GET, POST, PUT e DELETE são os métodos de requisição HTTP que vamos implementar em uma API ou em uma aplicação de operação CRUD.

1. GET: O método GET é usado para recuperar e obter informações do servidor informado usando uma URI informada. Requisições usando GET devem apenas recuperar dados e não devem ter outro efeito sobre os dados.

2. POST: A requisição POST é usada para criar dados e enviar dados ao servidor, por exemplo, criar um novo post, upload de arquivo, etc. usando formulários HTML.

3. PUT: Substitui todas as representações atuais do recurso alvo pelo conteúdo enviado e usamos para modificar ou atualizar dados.

4. DELETE: Remove dados

## 💻 Exercícios: Dia 28

1. Leia sobre API e HTTP

🎉 PARABÉNS ! 🎉

[<< Dia 27](../27_Dia_Python_com_MongoDB/README.md) | [Dia 29 >>](../29_Dia_Construindo_APIs/README.md)
