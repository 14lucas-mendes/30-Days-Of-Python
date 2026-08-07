<div align="center">
  <h1> 30 Dias de Python: Dia 29 - Construindo uma API </h1>
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

[<< Dia 28](../28_Dia_API/README.md) | [Dia 30 >>](../30_Dia_Conclusao/README.md)

![30DiasDePython](../../images/30DaysOfPython_banner3@2x.png)

- [Dia 29](#dia-29)
- [Construindo API](#construindo-api)
  - [Estrutura de uma API](#estrutura-de-uma-api)
  - [Recuperando dados usando get](#recuperando-dados-usando-get)
  - [Obtendo um documento por id](#obtendo-um-documento-por-id)
  - [Criando dados usando POST](#criando-dados-usando-post)
  - [Atualizando usando PUT](#atualizando-usando-put)
  - [Deletando um documento usando Delete](#deletando-um-documento-usando-delete)
- [💻 Exercícios: Dia 29](#-exercícios-dia-29)

## Dia 29

## Construindo API


Nesta seção, vamos cobrir uma RESTful API que usa métodos de requisição HTTP para GET, PUT, POST e DELETE de dados.

RESTful API é uma application program interface (API) que usa requisições HTTP para GET, PUT, POST e DELETE de dados. Nas seções anteriores, aprendemos sobre Python, Flask e MongoDB. Vamos usar o conhecimento que adquirimos para desenvolver uma RESTful API usando Python Flask e MongoDB. Toda aplicação que tem operação CRUD (Create, Read, Update, Delete) tem uma API para criar dados, obter dados, atualizar dados ou deletar dados do banco de dados.

O navegador pode lidar apenas com requisição get. Portanto, precisamos ter uma ferramenta que possa nos ajudar a lidar com todos os métodos de requisição (GET, POST, PUT, DELETE).

Exemplos de API

- Countries API: https://restcountries.eu/rest/v2/all
- Cats breed API: https://api.thecatapi.com/v1/breeds

[Postman](https://www.getpostman.com/) é uma ferramenta muito popular quando se trata de desenvolvimento de API. Então, se você quiser fazer esta seção, precisa [baixar o postman](https://www.getpostman.com/). Uma alternativa ao Postman é o [Insomnia](https://insomnia.rest/download).

![Postman](../../images/postman.png)

### Estrutura de uma API

Um endpoint de API é uma URL que pode ajudar a recuperar, criar, atualizar ou deletar um recurso. A estrutura fica assim:
Exemplo:
https://api.twitter.com/1.1/lists/members.json
Retorna os membros da lista especificada. Membros de lista privada só serão mostrados se o usuário autenticado for dono da lista especificada.
O nome da empresa seguido da versão seguido do propósito da API.
Os métodos:
Métodos HTTP e URLs

A API usa os seguintes métodos HTTP para manipulação de objetos:

```sh
GET        Used for object retrieval
POST       Used for object creation and object actions
PUT        Used for object update
DELETE     Used for object deletion
```

Vamos construir uma API que coleta informações sobre estudantes do 30DaysOfPython. Vamos coletar o nome, país, cidade, data de nascimento, skills e bio.

Para implementar esta API, vamos usar:

- Postman
- Python
- Flask
- MongoDB

### Recuperando dados usando get

Neste passo, vamos usar dados dummy e retorná-los como json. Para retornar como json, vamos usar o módulo json e o módulo Response.

```py
# vamos importar o flask

from flask import Flask,  Response
import json
import os

app = Flask(__name__)

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():
    student_list = [
        {
            'name':'Asabeneh',
            'country':'Finland',
            'city':'Helsinki',
            'skills':['HTML', 'CSS','JavaScript','Python']
        },
        {
            'name':'David',
            'country':'UK',
            'city':'London',
            'skills':['Python','MongoDB']
        },
        {
            'name':'John',
            'country':'Sweden',
            'city':'Stockholm',
            'skills':['Java','C#']
        }
    ]
    return Response(json.dumps(student_list), mimetype='application/json')


if __name__ == '__main__':
    # para deploy
    # para funcionar tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Quando você requisitar a url http://localhost:5000/api/v1.0/students no navegador, você vai obter isto:

![Get no navegador](../../images/get_on_browser.png)

Quando você requisitar a url http://localhost:5000/api/v1.0/students no navegador, você vai obter isto:

![Get no postman](../../images/get_on_postman.png)

Em vez de exibir dados dummy, vamos conectar a aplicação flask com o MongoDB e obter dados do banco de dados mongoDB.

```py
# vamos importar o flask

from flask import Flask,  Response
import json
import pymongo
import os

app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acessando o banco de dados

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')


if __name__ == '__main__':
    # para deploy
    # para funcionar tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Conectando o flask, podemos buscar os dados da collection students do banco de dados thirty_days_of_python.

```sh
[
    {
        "_id": {
            "$oid": "5df68a21f106fe2d315bbc8b"
        },
        "name": "Asabeneh",
        "country": "Finland",
        "city": "Helsinki",
        "age": 38
    },
    {
        "_id": {
            "$oid": "5df68a23f106fe2d315bbc8c"
        },
        "name": "David",
        "country": "UK",
        "city": "London",
        "age": 34
    },
    {
        "_id": {
            "$oid": "5df68a23f106fe2d315bbc8e"
        },
        "name": "Sami",
        "country": "Finland",
        "city": "Helsinki",
        "age": 25
    }
]
```

### Obtendo um documento por id

Podemos acessar um único documento usando um id; vamos acessar Asabeneh usando o id dele.
http://localhost:5000/api/v1.0/students/5df68a21f106fe2d315bbc8b

```py
# vamos importar o flask

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
import os

app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acessando o banco de dados

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')

if __name__ == '__main__':
    # para deploy
    # para funcionar tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
[
    {
        "_id": {
            "$oid": "5df68a21f106fe2d315bbc8b"
        },
        "name": "Asabeneh",
        "country": "Finland",
        "city": "Helsinki",
        "age": 38
    }
]
```

### Criando dados usando POST

Usamos o método de requisição POST para criar dados

```py
# vamos importar o flask

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
from datetime import datetime
import os

app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acessando o banco de dados

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students', methods = ['POST'])
def create_student ():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.insert_one(student)
    return ;
def update_student (id):
if __name__ == '__main__':
    # para deploy
    # para funcionar tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### Atualizando usando PUT

```py
# vamos importar o flask

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
from datetime import datetime
import os

app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acessando o banco de dados

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students', methods = ['POST'])
def create_student ():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.insert_one(student)
    return
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # este decorator cria a rota home
def update_student (id):
    query = {"_id":ObjectId(id)}
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.update_one(query, student)
    # return Response(dumps({"result":"a new student has been created"}), mimetype='application/json')
    return
def update_student (id):
if __name__ == '__main__':
    # para deploy
    # para funcionar tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### Deletando um documento usando Delete

```py
# vamos importar o flask

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
from datetime import datetime
import os

app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acessando o banco de dados

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students', methods = ['POST'])
def create_student ():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.insert_one(student)
    return
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # este decorator cria a rota home
def update_student (id):
    query = {"_id":ObjectId(id)}
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.update_one(query, student)
    # return Response(dumps({"result":"a new student has been created"}), mimetype='application/json')
    return
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # este decorator cria a rota home
def update_student (id):
    query = {"_id":ObjectId(id)}
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.update_one(query, student)
    # return Response(dumps({"result":"a new student has been created"}), mimetype='application/json')
    return ;
@app.route('/api/v1.0/students/<id>', methods = ['DELETE'])
def delete_student (id):
    db.students.delete_one({"_id":ObjectId(id)})
    return
if __name__ == '__main__':
    # para deploy
    # para funcionar tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

## 💻 Exercícios: Dia 29

1. Implemente o exemplo acima e desenvolva [isto](https://thirtydayofpython-api.herokuapp.com/)

🎉 PARABÉNS ! 🎉

[<< Dia 28](../28_Dia_API/README.md) | [Dia 30 >>](../30_Dia_Conclusao/README.md)
