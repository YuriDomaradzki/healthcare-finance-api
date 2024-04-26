import unittest
import requests


class TestTransactionsResources(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:5000/"

        payload = {"username": "Yuri", "password": "teste1234"}
        response = requests.post(f"{self.base_url}login", json=payload)
        self.token = response.json().get("access_token")

    # TEST IN {self.base_url}/transactions
    def test_list_transactions_values_must_return_list(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{self.base_url}transactions", headers=headers)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json()["Transactions"], list)

    # TESTS IN {self.base_url}/transactions/pharmacy/{name}
    def test_get_transactions_by_pharmacy_name_with_valid_name(self):
        name = "Droga Mais"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
<<<<<<< HEAD
            f"{self.base_url}/transactions?pharmacy_name={name}", headers=headers
=======
            f"{self.base_url}transactions/pharmacy/{name}", headers=headers
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117
        )

        self.assertEqual(response.status_code, 200)

    def test_get_transactions_by_pharmacy_name_with_invalid_name(self):
        name = ""
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
<<<<<<< HEAD
            f"{self.base_url}/transactions?pharmacy_name={name}", headers=headers
=======
            f"{self.base_url}transactions/pharmacy/{name}", headers=headers
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117
        )

        self.assertNotEqual(response.status_code, 200)

    # TESTS IN {self.base_url}/transactions/pharmacy/{name}/date/{transaction_date}
    def test_get_transactions_by_pharmacy_name_and_transaction_date_with_valid_name_and_date(
        self,
    ):
        name = "DROGAO SUPER"
        transaction_date = "2020-02-05"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
<<<<<<< HEAD
            f"{self.base_url}/transactions?pharmacy_name={name}&date={transaction_date}",
=======
            f"{self.base_url}transactions/pharmacy/{name}/date/{transaction_date}",
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117
            headers=headers,
        )

        self.assertEqual(response.status_code, 200)

    def test_get_transactions_by_pharmacy_name_and_transaction_date_with_invalid_name_and_valid_date(
        self,
    ):
        name = "Droga Mais_1"
        transaction_date = "2020-02-05"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
<<<<<<< HEAD
            f"{self.base_url}/transactions?pharmacy_name={name}&date={transaction_date}",
=======
            f"{self.base_url}transactions/pharmacy/{name}/date/{transaction_date}",
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117
            headers=headers,
        )

        self.assertNotEqual(response.status_code, 200)

    def test_get_transactions_by_pharmacy_name_and_transaction_date_with_valid_name_and_invalid_date(
        self,
    ):
        name = "Droga Mais"
        transaction_date = "20 de abril de 2020"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
<<<<<<< HEAD
            f"{self.base_url}/transactions?pharmacy_name={name}&date={transaction_date}",
=======
            f"{self.base_url}transactions/pharmacy/{name}/date/{transaction_date}",
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117
            headers=headers,
        )

        self.assertNotEqual(response.status_code, 200)

    # TESTS IN {self.base_url}/transactions/patient/{first_name}/{last_name}
    def test_get_transactions_by_patient_first_and_last_name_with_valid_first_and_last_name(
        self,
    ):
        first_name, last_name = "Joana Silva".split(" ")
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
<<<<<<< HEAD
            f"{self.base_url}/transactions?patient_name={first_name}&patient_last_name={last_name}",
=======
            f"{self.base_url}transactions/patient/{first_name}/{last_name}",
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117
            headers=headers,
        )

        self.assertEqual(response.status_code, 200)

    def test_get_transactions_by_patient_first_and_last_name_with_invalid_first_name_and_valid_last_name(
        self,
    ):
        first_name, last_name = "Joana1 Silva".split(" ")
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
<<<<<<< HEAD
            f"{self.base_url}/transactions?patient_name={first_name}&patient_last_name={last_name}",
=======
            f"{self.base_url}transactions/patient/{first_name}/{last_name}",
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117
            headers=headers,
        )

        self.assertNotEqual(response.status_code, 200)

    def test_get_transactions_by_patient_first_and_last_name_with_valid_first_name_and_invalid_last_name(
        self,
    ):
        first_name, last_name = "Joana ".split(" ")
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
<<<<<<< HEAD
            f"{self.base_url}/transactions?patient_name={first_name}&patient_last_name={last_name}",
=======
            f"{self.base_url}transactions/patient/{first_name}/{last_name}",
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117
            headers=headers,
        )

        self.assertNotEqual(response.status_code, 200)

    # TESTS IN {self.base_url}/transactions/byPeriod/{start_date}/{end_date}
    def test_get_transactions_by_period_with_valid_first_and_last_date(self):
        start_date, end_date = "2020-01-01/2020-01-08".split("/")
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
<<<<<<< HEAD
            f"{self.base_url}/transactions?date={start_date}&end_date={end_date}",
=======
            f"{self.base_url}transactions/byPeriod/{start_date}/{end_date}",
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117
            headers=headers,
        )

        self.assertEqual(response.status_code, 200)

    def test_get_transactions_by_period_with_invalid_first_and_valid_last_date(self):
        start_date, end_date = "20 de janeiro de 2020/2020-01-08".split("/")
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
<<<<<<< HEAD
            f"{self.base_url}/transactions?date={start_date}&end_date={end_date}",
=======
            f"{self.base_url}transactions/byPeriod/{start_date}/{end_date}",
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117
            headers=headers,
        )

        self.assertNotEqual(response.status_code, 200)

    def test_get_transactions_by_period_with_valid_first_and_invalid_last_date(self):
        start_date, end_date = "2020-01-01/ ".split("/")
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
<<<<<<< HEAD
            f"{self.base_url}/transactions?date={start_date}&end_date={end_date}",
=======
            f"{self.base_url}transactions/byPeriod/{start_date}/{end_date}",
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117
            headers=headers,
        )

        self.assertNotEqual(response.status_code, 200)

    # TESTS IN {self.base_url}/transactions/byValues/{min_value}/{max_value}
    def test_get_transactions_by_values_with_valid_min_and_max_values(self):
        min_value, max_value = "10.00", "20.99"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
<<<<<<< HEAD
            f"{self.base_url}/transactions?min_value={min_value}&max_value={max_value}",
=======
            f"{self.base_url}transactions/byValues/{min_value}/{max_value}",
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117
            headers=headers,
        )

        self.assertEqual(response.status_code, 200)

    def test_get_transactions_by_values_with_invalid_min_and_valid_max_values(self):
        min_value, max_value = "R$ 10,00", "20.99"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
<<<<<<< HEAD
            f"{self.base_url}/transactions?min_value={min_value}&max_value={max_value}",
=======
            f"{self.base_url}transactions/byValues/{min_value}/{max_value}",
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117
            headers=headers,
        )

        self.assertNotEqual(response.status_code, 200)

    def test_get_transactions_by_values_with_valid_min_and_invalid_max_values(self):
        min_value, max_value = "10.00", ""
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
<<<<<<< HEAD
            f"{self.base_url}/transactions?min_value={min_value}&max_value={max_value}",
=======
            f"{self.base_url}transactions/byValues/{min_value}/{max_value}",
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117
            headers=headers,
        )

        self.assertNotEqual(response.status_code, 200)


if __name__ == "__main__":

    unittest.main(verbosity=2)
