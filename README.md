[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![API Badge](https://img.shields.io/badge/API-healthcare_finance_api-brightgreen)

<h1 style="text-decoration: none; border-bottom: none;"> healthcare-finance-api </h1>
<hr style="border:1px solid #000;">
<br>

<p style="text-align=justify; font-size: 16px;">
Este repositório contém a implementação de uma API REST privada para o setor financeiro de uma empresa de saúde. A API fornece acesso seguro a informações sobre compras feitas pelos pacientes/clientes da empresa, abrangendo dados sobre pacientes, farmácias e transações.
</p>

<h2 style="text-decoration: none;border-bottom: none;"> Sumário </h2>
<hr style="border:1px solid #000;">
<br>

<ol>
    <li> <a href="#instalation" style="font-size: 16px;">Instalação</a>
    <li> <a href="" style="font-size: 16px;">Rotas</a>
</ol>

<h2 class="instalation" style="text-decoration: none;border-bottom: none;"> Instalação </h2>
<hr style="border:1px solid #000;">
<br>

<p style="text-align=justify; font-size: 16px;">
A implementação do healthcare-finance-api depende essencialmente de:
</p>
<ul>
    <li> <a href="https://flask.palletsprojects.com/en/latest/" style="font-size: 16px;"> Flask </a>
    <li> <a href="https://flask-smorest.readthedocs.io/en/latest/" style="font-size: 16px;"> Flask-smorest </a>
    <li> <a href="https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/" style="font-size: 16px;"> Flask-sqlalchemy </a>
    <li> <a href="https://flask-jwt-extended.readthedocs.io/en/stable/" style="font-size: 16px;"> Flask-jwt-extended </a>
    <li> <a href="https://www.sqlalchemy.org/" style="font-size: 16px;"> SQLAlchemy </a>
    <li> <a href="https://passlib.readthedocs.io/en/stable/" style="font-size: 16px;"> Passlib </a>
</ul>

<h2 class="develpment_installation" style="text-decoration: none;border-bottom: none;"> Instalação em modo desenvolvedor - GitHub </h2>
<hr style="border:1px solid #000;">

<br>

**1.** Crie um novo ambiente virtual vinculado ao Python 3.10:

    python3.10 -m venv venv


**2.** Ativar o novo ambiente:

    source venv/bin/activate


**3.** Atualizar pip e setuptools:

    pip3 install --upgrade pip
    pip3 install --upgrade setuptools


Use o ``git`` para clonar o repositório de software:

    git clone https://github.com/YuriDomaradzki/healthcare-finance-api.git

Vá para a pasta do código-fonte:

    cd healthcare-finance-api

Instalar no modo de desenvolvimento:

    pip3 install -e .[all]

<br>

<h2 class="develpment_installation" style="text-decoration: none;border-bottom: none;"> Instalação em modo desenvolvedor - GitHub </h2>
<hr style="border:1px solid #000;">

