# Workshop Fábrica 2024.2 - Cidades e Estados
### Autor: Wilton Nicolas de Lima Lopes

![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white)

Essa aplicação foi desenvolvida com Django REST e possui duas entidades principais: Estado e Cidade. A entidade Estado é capaz de consumir uma API externa para obter o UTC do país informado, o que permite que a aplicação sincronize informações de fuso horário de maneira eficiente. Além disso, ela inclui uma feature opcional de autenticação via JWT (JSON Web Token), que pode ser ativada para aumentar a segurança das interações na aplicação. O banco de dados utilizado é o MySQL, garantindo um armazenamento robusto e confiável para as informações gerenciadas.

## Features ✨

- CRUD Completo: Implementação de operações de Create, Read, Update e Delete para as entidades Estado e Cidade.
- Consumo de API Externa: A aplicação consome uma API para verificar e obter informações de fuso horário (UTC) com base no país informado na entidade Estado.
- Autenticação JWT (opcional): Integração opcional de autenticação via JWT (JSON Web Token) para proteger e assegurar as operações realizadas na API.
- Integração com Banco de Dados MySQL: Persistência de dados utilizando o banco MySQL, garantindo armazenamento confiável das informações das entidades.

## Dependências 🔧

- Python
- MySQL (MariaDB 10.5+)
- Django
- Django Rest
- Xampp

## Como começar 🚀

1. Instale o <a href="https://www.python.org/downloads/">Python</a> em sua máquina
2. De preferência utilize o <a href="https://code.visualstudio.com/">Visual Studio Code</a> para simplificar os próximos passos
3. Crie uma pasta para armazenar os arquivos da aplicação
4. Abra a pasta através do Visual Studio Code
5. Clone todos os arquivos deste repositório para a pasta (<a href="https://desktop.github.com/download/">Github Desktop</a> simplica essa parte)
6. Abra um terminal no Visual Studio Code (CTRL + Shift + ')
7. Inicie uma venv e a ative (python -m venv venv -> \venv\scripts\activate)
8. No console do Visual Studio Code utilize o seguinte comando: pip install -r requirements.txt
9. Abra o <a href="https://www.apachefriends.org/pt_br/index.html">xampp</a> e inicialize o Apache e o MySQL
10. Então va até a página de administração do MySQL e crie um BD chamado "sistemacidadesestados"
11. Em seguida caso tudo ocorrido de forma correta utilize: python manage.py runserver
12. Após isso a aplicação já está pronta para uso

### Caso você deseje utilizar o sistema de token JWT, será necessário fazer os seguintes passos:

1. Localize a pasta Estado e Cidade, e em seguida abra os arquivos viewsets.py de âmbos
2. Localize a linha que contem o seguinte código: "# permission_classes = (IsAuthenticated, )"
3. Remova a "#" do começo dessa linha e salve o arquivo
4. Após isso o sistema de token JWT, estara ativo

### Caso você deseje alterar o nome do banco utilizado:

1. Localize a pasta chamada project, e em seguida abra o arquivo settings.py
2. Localize a linha 82, onde estara escrito 'NAME': 'sistemacidadesestados'
3. Então altere o 'sistemacidadesestados' para o nome desejado

## Como utilizar 📝

Após todos os passos de configurações serem realizados, você ira receber um link para acessar a API, similar ou igual a este: http://127.0.0.1:8000/<br><br>
Para consumir as suas funcionalidades, será necessário adicionar ao final deste link uma das duas terminações a seguir:  /api/estado/estados | /api/cidade/cidades/<br><br>
Ambas possuem o CRUD e uma interface para realizar as operações, sendo necessário pelo menos um estado cadastrado, para utilização da /api/cidade/cidades/<br><br>

##

Caso você tenha ativado a autenticação JWT, será necessário uma aplicação como <a href="https://www.postman.com/">Postman</a> para simplificar a utilização da API<br><br>
Para conseguir um token de acesso, você precisara criar primeiramente um superuser com o seguinte comando no console do VSCode: python manage.py createsuperuser (Desligue a API, caso esteja em execução)<br><br>
Após utilizar o comando, basta preencher as informações pedidas e você terá um login e senha válidos para utilizar<br><br>
Então abra o link para API, porém com a terminação /token/, e basta utilizar o login e senha nos campos correspodentes<br><br>
Após isso você recebera um token de acesso e um token de atualização, utilize o token de acesso para ter a premissão necessária<br><br>
Utilizando do software Postman ou similar, você conseguirá fazer o acesso a API de forma muito mais simples<br><br>

##

Uma observação importante, é de que o BD MySQL precisa estar ativo para a API poder ser acionada e consumida, então certifique-se de que ela está ativa antes de executar a API
