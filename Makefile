SHELL := /bin/bash

install:
	python3.10 -m venv venv && \
	source venv/bin/activate && \
	pip install --upgrade pip && \
	pip install --upgrade setuptools && \
	pip install -e .[all]

run:
	python app.py

build:
	docker build -t healthcare-finance-api . && \
	docker run -d --name hf-api -p 5000:5000 healthcare-finance-api 

test_patient:
	python healthcare_finance_api/tests/test_patient.py

test_pharmacy:
	python healthcare_finance_api/tests/test_pharmacy.py

test_transactions:
	python healthcare_finance_api/tests/test_transactions.py

test_user:
	python healthcare_finance_api/tests/test_user_without_delete_put.py
	python healthcare_finance_api/tests/test_user_put.py
	python healthcare_finance_api/tests/test_user_delete.py

lint:
	isort .
	flake8 .
	black .

install_docker:
	sudo apt update && \
    sudo apt install -y apt-transport-https ca-certificates curl software-properties-common && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu focal stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    sudo apt update && \
    sudo apt install -y docker-ce docker-ce-cli containerd.io