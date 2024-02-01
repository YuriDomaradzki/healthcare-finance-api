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
   - [Endpoint Patients](#endpoint_patients)
        - [Listar todos os pacientes](#endpoint_list_patients)
        - [Consulta de paciente pelo primeiro nome](#endpoint_patient_first_name_get)
        - [Consulta de paciente pela data de nascimento](#endpoint_patient_birthday_get)
        - [Consulta de paciente pelo nome completo](#endpoint_patient_birthday_get)
   - [Endpoint Pharmacies](#endpoint_pharmacies)
        - [Listar todas as farmácias](#endpoint_list_pharmacies)
        - [Consulta de farmácias pelo nome](#endpoint_pharmacy_name_get)
        - [Consulta de farmácias por cidade](#endpoint_pharmacy_city_get)
        - [Consulta de farmácias por nome e cidade](#endpoint_pharmacy_city_name_get)
   - [Endpoint Transactions](#endpoint_transactions)
        - [Listar todas as transações](#endpoint_list_transactions)
        - [Consulta as transações de uma farmácia pelo nome](#endpoint_transaction_pharmacy_name_get)
        - [Consulta as transações de uma farmácia pelo nome para uma determinada data](#endpoint_transaction_pharmacy_name_date_get)
        - [Consulta as transações de um paciente pelo nome completo](#endpoint_transaction_patient_get)
        - [Consulta as transações de um determinado período](#endpoint_transaction_period_get)
        - [Consulta as transações por uma faixa de valores](#endpoint_transaction_byvalues_get)
3. [Testes](#tests)
   - [Testar as funcionalidades de Patients](#test_patients)
   - [Testar as funcionalidades de Pharmacies](#test_pharmacies)
   - [Testar as funcionalidades de Transactions](#test_transactions)
   - [Testar as funcionalidades de User](#test_user)
4. [Garantir Padrões e estilo de códigos de forma automatizada](#code_patterns)


<a id="instalation"></a>
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

    POST http://127.0.0.1:5000/register

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

    POST http://127.0.0.1:5000/login

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

    POST http://127.0.0.1:5000/refresh

**Headers:**

    {
        "Authorization": f"Bearer <access_token>"
    }

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

    POST http://127.0.0.1:5000/logout

**Headers:**

    {
        "Authorization": f"Bearer <access_token>"
    }

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

    GET http://127.0.0.1:5000/user/{username}

**Headers:**

    {
        "Authorization": f"Bearer <access_token>"
    }

**Exemplo:**

    GET http://127.0.0.1:5000/user/Yuri

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

    PUT http://127.0.0.1:5000/user/{username}

**Exemplo:**

    GET http://127.0.0.1:5000/user/Yuri

**Headers:**

    {
        "new_password": "teste1234",
        "Authorization": f"Bearer <access_token>"
    }

**Retorno:**

    {
        "Sucess": "The user was updated with successfully"
    }

<a id="endpoint_user_delete"></a>
#### **5.3.** Exclusão de usuário [DELETE]

**Endpoint:**

    DELETE http://127.0.0.1:5000/user/{username}

**Headers:**

    {
        "Authorization": f"Bearer <access_token>"
    }

**Exemplo:**

    DELETE http://127.0.0.1:5000/user/Yuri

**Retorno:**

    {
        "Success": "The user was deleted successfully"
    }

<a id="endpoint_patients"></a>
### **6.** Endpoint: Patients
O endpoint `Patients` destina-se a fornecer informações detalhadas sobre os pacientes, proporcionando uma maneira eficiente e segura de acessar dados relevantes sobre os indivíduos registrados no sistema. Ao utilizar este endpoint, os desenvolvedores têm a capacidade de obter informações cruciais, como ID do paciente, nome, sobrenome e data de nascimento.

**Recursos Principais:**
- Listar todos os pacientes
- Buscar pacientes pelo primeiro nome
- Buscar pacientes pela data de nascimento
- Buscar pacientes pelo nome completo

<a id="endpoint_list_patients"></a>
#### **6.1.** Listar todos os pacientes [GET]

**Endpoint:**

    GET http://127.0.0.1:5000/patients

**Headers:**

    {
        "Authorization": f"Bearer <access_token>"
    }

**Retorno:**

    {
        "Patients": [
            {
                "DATE OF BIRTH": "1996-10-25",
                "FIRST NAME": "JOANA",
                "ID": "PATIENT0001",
                "LAST NAME": "SILVA"
            },
            {
                "DATE OF BIRTH": "1984-12-05",
                "FIRST NAME": "GUSTAVO",
                "ID": "PATIENT0002",
                "LAST NAME": "SALOMAO"
            },
            ...
        ]
    }

<a id="endpoint_patient_first_name_get"></a>
#### **6.2.** Consulta de paciente pelo primeiro nome [GET]

**Endpoint:**

    GET http://127.0.0.1:5000/patient/name/{first_name}

**Headers:**

    {
        "Authorization": f"Bearer <access_token>"
    }

**Exemplo:**

    GET http://127.0.0.1:5000/patient/name/JOANA

**Retorno:**

    {
        "Patient": [
            {
                "DATE OF BIRTH": "1996-10-25",
                "FIRST NAME": "JOANA",
                "ID": "PATIENT0001",
                "LAST NAME": "SILVA"
            },
            {
                "DATE OF BIRTH": "1980-07-23",
                "FIRST NAME": "JOANA",
                "ID": "PATIENT0035",
                "LAST NAME": "FERREIRA"
            }
        ]
    }

<a id="endpoint_patient_birthday_get"></a>
#### **6.3.** Consulta de paciente pela data de nascimento [GET]

**Endpoint:**

    GET http://127.0.0.1:5000/patient/birthday/{birthday}

**Headers:**

    {
        "Authorization": f"Bearer <access_token>"
    }

**Exemplo:**

    GET http://127.0.0.1:5000/patient/birthday/1984-12-05

**Retorno:**

    {
        "Patient": [
            {
                "DATE OF BIRTH": "1984-12-05",
                "FIRST NAME": "GUSTAVO",
                "ID": "PATIENT0002",
                "LAST NAME": "SALOMAO"
            }
        ]
    }

<a id="endpoint_patient_birthday_get"></a>
#### **6.4.** Consulta de paciente pelo nome completo [GET]

**Endpoint:**

    GET http://127.0.0.1:5000/patient/name/{first_name}/lastName/{last_name}

**Headers:**

    {
        "Authorization": f"Bearer <access_token>"
    }

**Exemplo:**

    GET http://127.0.0.1:5000/patient/name/JOANA/lastName/Silva

**Retorno:**

    {
        "Patient": [
            {
                "DATE OF BIRTH": "1996-10-25",
                "FIRST NAME": "JOANA",
                "ID": "PATIENT0001",
                "LAST NAME": "SILVA"
            }
        ]
    }


<a id="endpoint_pharmacies"></a>
### **7.** Endpoint: Pharmacies
O endpoint `Pharmacies` é dedicado a fornecer informações detalhadas sobre farmácias, oferecendo uma abordagem eficiente e segura para acessar dados relevantes relacionados aos estabelecimentos farmacêuticos registrados no sistema. Ao utilizar este endpoint, os desenvolvedores podem adquirir informações cruciais, tais como identificador da farmácia, localização, e detalhes específicos dos serviços prestados.

**Recursos Principais:**
- Listar todas as farmácias
- Buscar farmácias pelo nome
- Buscar pacientes pela data de nascimento
- Buscar pacientes pelo nome completo

<a id="endpoint_list_pharmacies"></a>
#### **7.1.** Listar todas as farmácias [GET]

**Endpoint:**

    GET http://127.0.0.1:5000/pharmacies

**Headers:**

    {
        "Authorization": f"Bearer <access_token>"
    }

**Retorno:**

    {
        "Pharmacies": [
            {
                "CITY": "RIBEIRAO PRETO",
                "ID": "PHARM0001",
                "NAME": "DROGA MAIS"
            },
            {
                "CITY": "SAO SIMAO",
                "ID": "PHARM0002",
                "NAME": "DROGAO SUPER"
            },
            ...
        ]
    }


<a id="endpoint_pharmacy_name_get"></a>
#### **7.2.** Consulta de farmácias pelo nome [GET]

**Endpoint:**

    GET http://127.0.0.1:5000/pharmacy/name/{name}

**Exemplo:**

    GET http://127.0.0.1:5000/pharmacy/name/Droga Mais

**Headers:**

    {
        "Authorization": f"Bearer <access_token>"
    }

**Retorno:**

    {
        "Pharmacy": [
            {
                "CITY": "RIBEIRAO PRETO",
                "ID": "PHARM0001",
                "NAME": "DROGA MAIS"
            },
            {
                "CITY": "SAO PAULO",
                "ID": "PHARM0006",
                "NAME": "DROGA MAIS"
            }
        ]
    }


<a id="endpoint_pharmacy_city_get"></a>
#### **7.3.** Consulta de farmácias por cidade [GET]

**Endpoint:**

    GET http://127.0.0.1:5000/pharmacy/city/{city_name}

**Exemplo:**

    GET http://127.0.0.1:5000/pharmacy/city/Sao Simao

**Headers:**

    {
        "Authorization": f"Bearer <access_token>"
    }

**Retorno:**

    {
        "Pharmacy": [
            {
                "CITY": "SAO SIMAO",
                "ID": "PHARM0002",
                "NAME": "DROGAO SUPER"
            },
            {
                "CITY": "SAO SIMAO",
                "ID": "PHARM0007",
                "NAME": "DROGASIL"
            }
        ]
    }


<a id="endpoint_pharmacy_city_name_get"></a>
#### **7.4.** Consulta de farmácias por nome e cidade [GET]

**Endpoint:**

    GET http://127.0.0.1:5000/pharmacy/city/{city_name}/name/{name}

**Exemplo:**

    GET http://127.0.0.1:5000/pharmacy/city/Sao Paulo/name/Droga Mais

**Headers:**

    {
        "Authorization": f"Bearer <access_token>"
    }

**Retorno:**

    {
        "Pharmacy": [
            {
                "CITY": "SAO PAULO",
                "ID": "PHARM0006",
                "NAME": "DROGA MAIS"
            }
        ]
    }


<a id="endpoint_transactions"></a>
### **8.** Endpoint: Transactions
O endpoint `Transactions` é projetado para fornecer informações detalhadas sobre as transações realizadas no sistema, permitindo um acesso eficiente e seguro aos dados financeiros relacionados. Ao utilizar este endpoint, os desenvolvedores podem obter informações cruciais sobre transações específicas, histórico financeiro e outras métricas relacionadas.

**Recursos Principais:**
- Listar todas as transações
- Buscar transações por data
- Buscar transações por tipo
- Detalhes específicos de cada transação

<a id="endpoint_list_transactions"></a>
#### **8.1.** Listar todas as transações [GET]

**Endpoint:**

    GET http://127.0.0.1:5000/transactions

**Headers:**

    {
        "Authorization": f"Bearer <access_token>"
    }

**Retorno:**

    {
        "Transactions": [
            {
                "AMOUNT": "R$ 40.68",
                "ID": "TRAN0111",
                "PATIENT": {
                    "DATE OF BIRTH": "1979-03-22",
                    "FIRST NAME": "ABEL",
                    "ID": "PATIENT0025",
                    "LAST NAME": "MANCINI"
                },
                "PHARMACY": {
                    "CITY": "RIBEIRAO PRETO",
                    "ID": "PHARM0005",
                    "NAME": "DROGARIA SAO SIMAO"
                },
                "TRANSACTION DATE": "2020-01-01"
            },
            ...
        ]
    }


<a id="endpoint_transaction_pharmacy_name_get"></a>
#### **8.2.** Consulta as transações de uma farmácia pelo nome  [GET]

**Endpoint:**

    GET http://127.0.0.1:5000/transactions/pharmacy/{name}

**Exemplo:**

    GET http://127.0.0.1:5000/transactions/pharmacy/Droga Mais

**Headers:**

    {
        "Authorization": f"Bearer <access_token>"
    }

**Retorno:**

    {
        "Transaction": [
            {
                "AMOUNT": "R$ 7.34",
                "ID": "TRAN0236",
                "PATIENT": {
                    "DATE OF BIRTH": "1979-03-22",
                    "FIRST NAME": "ABEL",
                    "ID": "PATIENT0025",
                    "LAST NAME": "MANCINI"
                },
                "PHARMACY": {
                    "CITY": "RIBEIRAO PRETO",
                    "ID": "PHARM0001",
                    "NAME": "DROGA MAIS"
                },
                "TRANSACTION DATE": "2020-01-07"
            },
            {
                "AMOUNT": "R$ 1.79",
                "ID": "TRAN0082",
                "PATIENT": {
                    "DATE OF BIRTH": "1975-12-01",
                    "FIRST NAME": "CRISTIANO",
                    "ID": "PATIENT0036",
                    "LAST NAME": "FERREIRA"
                },
                "PHARMACY": {
                    "CITY": "RIBEIRAO PRETO",
                    "ID": "PHARM0001",
                    "NAME": "DROGA MAIS"
                },
                "TRANSACTION DATE": "2020-02-14"
            },
            ...
        ]
    }

<a id="endpoint_transaction_pharmacy_name_date_get"></a>
#### **8.3.** Consulta as transações de uma farmácia pelo nome para uma determinada data [GET]

**Endpoint:**

    GET http://127.0.0.1:5000/transactions/pharmacy/{name}/date/{date}

**Exemplo:**

    GET http://127.0.0.1:5000/transactions/pharmacy/DROGAO SUPER/date/2020-02-05

**Headers:**

    {
        "Authorization": f"Bearer <access_token>"
    }

**Retorno:**

    {
        "Transaction": [
            {
                "AMOUNT": "R$ 3.50",
                "ID": "TRAN0001",
                "PATIENT": {
                    "DATE OF BIRTH": "1993-09-30",
                    "FIRST NAME": "CRISTIANO",
                    "ID": "PATIENT0045",
                    "LAST NAME": "SALOMAO"
                },
                "PHARMACY": {
                    "CITY": "CAMPINAS",
                    "ID": "PHARM0008",
                    "NAME": "DROGAO SUPER"
                },
                "TRANSACTION DATE": "2020-02-05"
            }
        ]
    }


<a id="endpoint_transaction_patient_get"></a>
#### **8.4.** Consulta as transações de um paciente pelo nome completo  [GET]

**Endpoint:**

    GET http://127.0.0.1:5000/transactions/patient/{first_name}/{last_name}

**Exemplo:**

    GET http://127.0.0.1:5000/transactions/patient/Joana/SILVA

**Headers:**

    {
        "Authorization": f"Bearer <access_token>"
    }

**Retorno:**

    {
        "Transaction": [
            {
                "AMOUNT": "R$ 2.69",
                "ID": "TRAN0282",
                "PATIENT": {
                    "DATE OF BIRTH": "1996-10-25",
                    "FIRST NAME": "JOANA",
                    "ID": "PATIENT0001",
                    "LAST NAME": "SILVA"
                },
                "PHARMACY": {
                    "CITY": "SAO PAULO",
                    "ID": "PHARM0010",
                    "NAME": "DROGARIA SAO SIMAO"
                },
                "TRANSACTION DATE": "2020-03-18"
            },
            ...
        ]
    }


<a id="endpoint_transaction_period_get"></a>
#### **8.5.** Consulta as transações de um determinado período [GET]

**Endpoint:**

    GET http://127.0.0.1:5000/transactions/byPeriod/{first_date}/{end_date}

**Exemplo:**

    GET http://127.0.0.1:5000/transactions/byPeriod/2020-01-01/2020-01-08

**Headers:**

    {
        "Authorization": f"Bearer <access_token>"
    }

**Retorno:** :

    {
        "Transaction": [
            {
                "AMOUNT": "R$ 40.68",
                "ID": "TRAN0111",
                "PATIENT": {
                    "DATE OF BIRTH": "1979-03-22",
                    "FIRST NAME": "ABEL",
                    "ID": "PATIENT0025",
                    "LAST NAME": "MANCINI"
                },
                "PHARMACY": {
                    "CITY": "RIBEIRAO PRETO",
                    "ID": "PHARM0005",
                    "NAME": "DROGARIA SAO SIMAO"
                },
                "TRANSACTION DATE": "2020-01-01"
            },
            {
                "AMOUNT": "R$ 33.14",
                "ID": "TRAN0033",
                "PATIENT": {
                    "DATE OF BIRTH": "1977-09-10",
                    "FIRST NAME": "STEPHANY",
                    "ID": "PATIENT0008",
                    "LAST NAME": "FERREIRA"
                },
                "PHARMACY": {
                    "CITY": "SAO PAULO",
                    "ID": "PHARM0010",
                    "NAME": "DROGARIA SAO SIMAO"
                },
                "TRANSACTION DATE": "2020-01-02"
            },
            ...
        ]
    }


<a id="endpoint_transaction_byvalues_get"></a>
#### **8.6.** Consulta as transações por uma faixa de valores [GET]

**Endpoint:**

    GET http://127.0.0.1:5000/transactions/byValues/{min_value}/{max_value}

**Exemplo:**

    GET http://127.0.0.1:5000/transactions/byValues/5/12

**Headers:**

    {
        "Authorization": f"Bearer <access_token>"
    }

**Retorno:** :

    {
        "Transaction": [
            {
                "AMOUNT": "R$ 11.39",
                "ID": "TRAN0264",
                "PATIENT": {
                    "DATE OF BIRTH": "1984-11-16",
                    "FIRST NAME": "CRISTIANO",
                    "ID": "PATIENT0015",
                    "LAST NAME": "TEIXEIRA"
                },
                "PHARMACY": {
                    "CITY": "LIMEIRA",
                    "ID": "PHARM0004",
                    "NAME": "DROGAO SUPER"
                },
                "TRANSACTION DATE": "2020-02-10"
            },
            {
                "AMOUNT": "R$ 10.12",
                "ID": "TRAN0102",
                "PATIENT": {
                    "DATE OF BIRTH": "1979-09-27",
                    "FIRST NAME": "LETICIA",
                    "ID": "PATIENT0046",
                    "LAST NAME": "SANTOS"
                },
                "PHARMACY": {
                    "CITY": "RIBEIRAO PRETO",
                    "ID": "PHARM0003",
                    "NAME": "SUPER DROGAO"
                },
                "TRANSACTION DATE": "2020-05-29"
            },
            ...
        ]
    }

<a id="tests"></a>
## Testes

Nesta seção, você encontrará os testes relacionados às funcionalidades da API.


<a id="test_patients"></a>
### **1.** Testar as funcionalidades de Patients

A seguir, estão alguns cenários de teste para validar as funcionalidades relacionadas aos pacientes:

 - Listagem de pacientes para garantir a obtenção de uma lista válida.
 - Consulta de paciente pelo nome, validando a obtenção de informações corretas com um nome válido e a rejeição de nomes inválidos.
 - Consulta de paciente pela data de nascimento, assegurando a obtenção de informações corretas com uma data válida e a rejeição de datas inválidas.
 - Consulta de paciente pelo primeiro e último nome, verificando a obtenção de informações corretas com nomes válidos e a rejeição de nomes inválidos.

 Utilize o comando `make test_patient` para executar os casos de teste:

    make test_patient

<a id="test_pharmacies"></a>
### **2.** Testar as funcionalidades de Pharmacies

A seguir, estão alguns cenários de teste para validar as funcionalidades relacionadas às farmácies:

 - Listagem de Farmácias para garantir a obtenção de uma lista válida ao estar autenticado.
 - Obtenção de Farmácia por Nome Válido para verificar a obtenção de informações corretas com um nome válido e rejeição de nomes inválidos ao estar autenticado.
 - Obtenção de Farmácia por Nome Inválido para validar a impossibilidade de obter informações de farmácias com nome inválido, mesmo estando autenticado.
 - Obtenção de Farmácia por Cidade Válida para assegurar a obtenção de informações corretas por uma cidade válida ao estar autenticado.
 - Obtenção de Farmácia por Cidade Inválida para verificar a impossibilidade de obter informações de farmácias com cidade inválida, mesmo estando autenticado.
 - Obtenção de Farmácia por Nome e Cidade Válidos para garantir a obtenção de informações corretas com nome e cidade válidos ao estar autenticado.
 - Obtenção de Farmácia por Cidade Inválida e Nome Válido para validar a impossibilidade de obter informações de farmácias com cidade inválida, mesmo com nome válido, estando autenticado.
 - Obtenção de Farmácia por Cidade Válida e Nome Inválido para validar a impossibilidade de obter informações de farmácias com nome inválido, mesmo com cidade válida, estando autenticado.

 Utilize o comando `make test_pharmacy` para executar os casos de teste:

    make test_pharmacy


<a id="test_transactions"></a>
### **3.** Testar as funcionalidades de Transactions

A seguir, estão alguns cenários de teste para validar as funcionalidades relacionadas as transações:

 - Listagem de Transações para garantir a obtenção de uma lista válida ao estar autenticado.
 - Obtenção de Transações por Nome de Farmácia Válido para verificar a obtenção de informações corretas com um nome de farmácia válido e rejeição de nomes inválidos ao estar autenticado.
 - Obtenção de Transações por Nome de Farmácia Inválido para validar a impossibilidade de obter informações de transações com nome de farmácia inválido, mesmo estando autenticado.
 - Obtenção de Transações por Nome de Farmácia e Data de Transação Válidos para garantir a obtenção de informações corretas com nome de farmácia e data válidos ao estar autenticado.
 - Obtenção de Transações por Nome de Farmácia Inválido e Data de Transação Válida para validar a impossibilidade de obter informações de transações com nome de farmácia inválido, mesmo com data válida, estando autenticado.

 Utilize o comando `make test_transactions` para executar os casos de teste:

    make test_transactions

<a id="test_user"></a>
### **4.** Testar as funcionalidades de User

A seguir, estão alguns cenários de teste para validar as funcionalidades relacionados aos usuários:

 - Obtenção de Informações do Usuário com Nome de Usuário Válido: Garante que seja possível obter informações do usuário com um nome de usuário válido ao estar autenticado.
 - Obtenção de Informações do Usuário com Nome de Usuário Inválido: Garante que não seja possível obter informações do usuário com um nome de usuário inválido ao estar autenticado.
 - Logout: Verifica se o processo de logout ocorre corretamente, encerrando a sessão do usuário autenticado.
 - Login com Nome de Usuário Válido e Senha Inválida: Valida que não seja possível realizar o login com um nome de usuário válido e senha inválida.
 - Login com Nome de Usuário Inválido e Senha Válida: Valida que não seja possível realizar o login com um nome de usuário inválido e senha válida.

 Utilize o comando `make test_user` para executar os casos de teste:

    make test_user

<a id="code_patterns"></a>
## Garantir Padrões e estilo de códigos de forma automatizada

A utilização do comando `make lint` é uma prática fundamental para garantir a padronização e o estilo do código de maneira automatizada. Este comando incorpora diversas ferramentas e processos que analisam o código-fonte, assegurando sua conformidade com as diretrizes estabelecidas. Para utilizá-lo, entre no diretório raiz do projeto e execute o seguinte comando:

    make lint