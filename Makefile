SHELL := /bin/bash

install:
	python3.10 -m venv venv && \
	source venv/bin/activate && \
	pip install --upgrade pip && \
	pip install --upgrade setuptools && \
	pip install -e .[all]

run:
	python app.py

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