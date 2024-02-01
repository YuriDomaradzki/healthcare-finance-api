[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![SO](https://img.shields.io/badge/Platform-Linux-bringhtgreen)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04-brightgreen.svg)
![Python](https://img.shields.io/badge/Python-3.10-blue)
[![Versão do Docker](https://img.shields.io/badge/Docker-%3E%3D17.06-blue.svg)](https://www.docker.com/)
![API Badge](https://img.shields.io/badge/API-healthcare_finance_api-brightgreen)


<h1> healthcare-finance-api </h1>
<br>

Este repositório contém a implementação de uma API REST privada para o setor financeiro de uma empresa de saúde. A API fornece acesso seguro a informações sobre compras feitas pelos pacientes/clientes da empresa, abrangendo dados sobre pacientes, farmácias e transações.


## Sumário

1. [Instalação](#instalation)
   - [Instalação em modo de desenvolvedor](#instalation_dev_mode)
   - [Instalação em modo de produção](#instalation_prod_mode)
2. [Utilização](#usage)
   - [Endpoint Register](#endpoint_register)
   - [Endpoint Login](#endpoint_login)
   - [Endpoint Refresh](#endpoint_refresh)
   - [Endpoint Logout](#endpoint_logout)
   - [Endpoint User](#endpoint_user)
        - [Consulta de usuário](#endpoint_user_get)
        - [Atualização de usuário](#endpoint_user_put)
        - [Exclusão de usuário](#endpoint_user_delete)

<a id="installation"></a>
## Instalação

A implementação do healthcare-finance-api depende essencialmente de:

- [Flask](https://flask.palletsprojects.com/en/latest/)
- [Flask-smorest](https://flask-smorest.readthedocs.io/en/latest/)
- [Flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)
- [Flask-jwt-extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Passlib](https://passlib.readthedocs.io/en/stable/)
- [isort](https://pycqa.github.io/isort/)
- [flake8](https://flake8.pycqa.org/en/latest/)
- [black](https://black.readthedocs.io/en/stable/)

Para começar a utilizar a API e ter acesso ao código-fonte do software, siga os passos abaixo para clonar o repositório:

### **1.** Clone o repositório de software:

Utilize o seguinte comando para clonar o repositório para o seu ambiente local:

    git clone https://github.com/YuriDomaradzki/healthcare-finance-api.git

### **2.** Acesse a Pasta do Código-Fonte:

Navegue até a pasta do código-fonte do projeto utilizando o comando `cd`. Certifique-se de estar no diretório correto antes de prosseguir.

    cd healthcare-finance-api

<a id="instalation_dev_mode"></a>
## Instalação em modo desenvolvedor - GitHub 

Para realizar a instalação em modo de desenvolvedor do projeto a partir do GitHub, siga os passos abaixo:

### **1.** Instalação no Modo de Desenvolvimento:

Utilize o comando `make install` para realizar a instalação em modo de desenvolvimento. Este comando irá configurar o ambiente, instalar dependências e preparar o projeto para ser executado localmente.

    make install

### **2.** Execução em Modo de Desenvolvimento:

Utilize o comando `make run` no diretório raiz do projeto para executá-lo em modo de desenvolvimento, resultando na criação de um servidor em modo de desenvolvimento:

    make run

<br>

<a id="instalation_prod_mode"></a>
## Instalação em modo de produção - GitHub 

Para realizar a instalação em modo de desenvolvedor utiizando docker containers siga os passos abaixo:

### **1.** Instale o Docker caso ainda não esteja instalado (tutorial de [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)):

    make install_docker

### **2.** Instalação e Execução no Modo de Desenvolvimento:
Utilize o comando `make build` para realizar a instalação e execução da aplicação em modo de produção. Este comando irá criar uma imagem docker do projeto e subir um container a partir dela:

    make build

<a id="usage"></a>
## Utilização

A seção de utilização disponibiliza definições e exemplos para cada ponto de extremidade da API healthcare-finance-api. Para facilitar o uso da API, pode-se utilizar o <a href="https://insomnia.rest/download">Insomnia</a>.

<a id="endpoint_register"></a>
### **1.** Endpoint: Register

O endpoint `Register` é projetado para facilitar a autenticação de usuários, fornecendo um mecanismo seguro e eficiente para acessar o sistema. Ao utilizar este endpoint, os desenvolvedores podem implementar um processo de login robusto, garantindo acesso seguro às funcionalidades protegidas do sistema. Este endpoint é essencial para estabelecer a identidade dos usuários e garantir a segurança das informações sensíveis.Este endpoint é crucial para expandir a base de usuários e manter a integridade das informações.

**Recursos Principais:**
- Criação segura de contas de usuário.

**Endpoint:**

    POST {url}/register

**Headers:**

    {
        "username": "Yuri",
        "password": "teste1234"
    }

**Retorno:**

    {
        "Success": "User Yuri added!"
    }

<a id="endpoint_login"></a>
### **2.** Endpoint: Login

O endpoint `Login` é projetado para facilitar a autenticação de usuários, fornecendo um mecanismo seguro e eficiente para acessar o sistema. Ao utilizar este endpoint, os desenvolvedores podem implementar um processo de login robusto, garantindo acesso seguro às funcionalidades protegidas do sistema. Este endpoint é essencial para estabelecer a identidade dos usuários e garantir a segurança das informações sensíveis.

**Recursos Principais:**
- Autenticação segura de usuários.
- Controle de acesso a funcionalidades restritas.
- Geração de tokens de sessão para usuários autenticados.

**Endpoint:**

    POST {url}/login

**Headers:**

    {
		"username": "Yuri",
        "password": "teste1234"
    }

**Retorno:**

    {
        "access_token": "<access_token>",
        "refresh_token": "<refresh_token>"
    }

<a id="endpoint_refresh"></a>
### **3.** Endpoint: Refresh

O endpoint `Refresh` é uma extensão do sistema de autenticação proporcionado pelo endpoint `Login`. Projetado para garantir uma autenticação contínua e segura, o endpoint `Refresh` permite a geração de novos tokens de sessão para usuários previamente autenticados.

**Recursos Principais:**
- Geração de novos tokens de sessão para usuários autenticados.

**Endpoint:**

    POST {url}/refresh

**Retorno:**

    {
        "access_token": "<new_access_token>"
    }

<a id="endpoint_logout"></a>
### **4.** Endpoint: Logout

O endpoint `Logout` representa uma extensão vital do sistema de autenticação fornecido pelo endpoint `Login`. Enquanto o endpoint `Login` permite a entrada segura dos usuários no sistema, o `Logout` desempenha um papel crucial ao garantir o encerramento seguro de sessões. Ao utilizar este endpoint, os desenvolvedores podem implementar um processo robusto para encerrar sessões ativas, promovendo a segurança e o controle de acesso.

**Recursos Principais:**
- Encerramento seguro de sessões de usuário.

**Endpoint:**

    POST {url}/logout

**Retorno:**

    {
        "message": "Successfully logged out."
    }

<a id="endpoint_user"></a>
### **5.** Endpoint: User

O endpoint `User` desempenha um papel central na gestão de informações do usuário dentro do sistema. Projetado para oferecer funcionalidades robustas relacionadas aos usuários, este endpoint possibilita operações como recuperação de informações, atualizações e exclusões de usuários.

**Recursos Principais:**
- Recuperação, atualização e exclusão de informações do usuário.

<a id="endpoint_user_get"></a>
#### **5.1.** Consulta de usuário [GET]

**Endpoint:**

    GET {url}/user/{username}

**Exemplo:**

    GET {url}/user/Yuri

**Retorno:**

    {
        "User": [
            {
                "ID": "USER0006",
                "USERNAME": "Yuri"
            }
        ]
    }

<a id="endpoint_user_put"></a>
#### **5.2.** Atualização de usuário [PUT]

**Endpoint:**

    PUT {url}/user/{username}

**Exemplo:**

    GET {url}/user/Yuri

**Headers:**

    {
        "new_password": "teste1234"
    }

**Retorno:**

    {
        "Sucess": "The user was updated with successfully"
    }

<a id="endpoint_user_delete"></a>
#### **5.3.** Exclusão de usuário [DELETE]

**Endpoint:**

    DELETE {url}/user/{username}

**Exemplo:**

    DELETE {url}/user/Yuri

**Retorno:**

    {
        "Success": "The user was deleted successfully"
    }

<a id="endpoint_patients"></a>
### **6.** Endpoint: Patients
O endpoint `Patients` destina-se a fornecer informações detalhadas sobre os pacientes, proporcionando uma maneira eficiente e segura de acessar dados relevantes sobre os indivíduos registrados no sistema de saúde. Ao utilizar este endpoint, os desenvolvedores têm a capacidade de obter informações cruciais, como ID do paciente, nome, sobrenome e data de nascimento.

#### Consulta de Pacientes [GET]

**Endpoint:**

    GET {url}/patients




