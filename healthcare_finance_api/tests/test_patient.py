import unittest
import requests


class TestPatientsResources(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:5000/"

        payload = {"username": "Yuri", "password": "teste1234"}
        response = requests.post(f"{self.base_url}login", json=payload)
        self.token = response.json().get("access_token")

    # TESTS IN {self.base_url}/patients
    def test_list_patients_values_must_return_list(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{self.base_url}patients", headers=headers)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json()["Patients"], list)

    # TESTS IN {self.base_url}/patient/name/{name}
    def test_get_patient_by_name_with_valid_name(self):
        name = "Joana"
        headers = {"Authorization": f"Bearer {self.token}"}
<<<<<<< HEAD
        response = requests.get(f"{self.base_url}/patient?name={name}", headers=headers)
=======
        response = requests.get(f"{self.base_url}patient/name/{name}", headers=headers)
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117

        self.assertEqual(response.status_code, 200)

    def test_get_patient_by_name_with_invalid_name(self):
        name = "John1"
        headers = {"Authorization": f"Bearer {self.token}"}
<<<<<<< HEAD
        response = requests.get(f"{self.base_url}/patient?name={name}", headers=headers)
=======
        response = requests.get(f"{self.base_url}patient/name/{name}", headers=headers)
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117

        self.assertNotEqual(response.status_code, 200)

    # TESTS IN {self.base_url}/patient/birthday/{birthday}
    def test_get_patient_by_birthday_with_valid_birthday(self):
        birthday = "1984-12-05"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
<<<<<<< HEAD
            f"{self.base_url}/patient?birthday={birthday}", headers=headers
=======
            f"{self.base_url}patient/birthday/{birthday}", headers=headers
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117
        )

        self.assertEqual(response.status_code, 200)

    def test_get_patient_by_birthday_with_invalid_birthday(self):
        birthday = "27 de abril de 1999"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
<<<<<<< HEAD
            f"{self.base_url}/patient?birthday={birthday}", headers=headers
=======
            f"{self.base_url}patient/birthday/{birthday}", headers=headers
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117
        )

        self.assertNotEqual(response.status_code, 200)

    # TESTS IN {self.base_url}/patient/name/{first_name}/lastName/{last_name}
    def test_get_patient_by_first_and_last_name_with_valid_first_and_last_name(self):
        first_name, last_name = "Joana Silva".split(" ")
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
<<<<<<< HEAD
            f"{self.base_url}/patient?name={first_name}&last_name={last_name}",
=======
            f"{self.base_url}patient/name/{first_name}/lastName/{last_name}",
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117
            headers=headers,
        )

        self.assertEqual(response.status_code, 200)

    def test_get_patient_by_first_and_last_name_with_invalid_first_and_last_name(self):
        first_name, last_name = "123 Silva".split(" ")
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
<<<<<<< HEAD
            f"{self.base_url}/patient?name={first_name}&last_name={last_name}",
=======
            f"{self.base_url}patient/name/{first_name}/lastName/{last_name}",
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117
            headers=headers,
        )

        self.assertNotEqual(response.status_code, 200)


if __name__ == "__main__":

    unittest.main(verbosity=2)
