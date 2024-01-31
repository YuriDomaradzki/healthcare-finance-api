import unittest
import requests


class TestPatientsResources(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:5000/"

        payload = {"username": "yuri", "password": "teste1234"}
        response = requests.post(f'{self.base_url}/login', json=payload)
        self.token = response.json().get('access_token')

    def test_list_patients_values_must_return_list(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f'{self.base_url}/patients', headers=headers)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json()['Patients'], list)

    def test_get_patient_by_name_with_valid_name(self):
        name = 'Joana'
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f'{self.base_url}/patient/name/{name}', headers=headers)

        self.assertEqual(response.status_code, 200)

    def test_get_patient_by_name_with_invalid_name(self):
        name = 'John1'
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f'{self.base_url}/patient/name/{name}', headers=headers)

        self.assertNotEqual(response.status_code, 200)

    def test_get_patient_by_birthday_with_valid_birthday(self):
        birthday = '1984-12-05'
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f'{self.base_url}/patient/birthday/{birthday}', headers=headers)

        self.assertEqual(response.status_code, 200)

    def test_get_patient_by_birthday_with_invalid_birthday(self):
        birthday = '27 de abril de 1999'
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f'{self.base_url}/patient/birthday/{birthday}', headers=headers)

        self.assertNotEqual(response.status_code, 200)

    def test_get_patient_by_first_and_last_name_with_valid_first_and_last_name(self):
        first_name, last_name = 'Joana Silva'.split(" ")
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f'{self.base_url}/patient/name/{first_name}/lastName/{last_name}', headers=headers)

        self.assertEqual(response.status_code, 200)

    def test_get_patient_by_first_and_last_name_with_invalid_first_and_last_name(self):
        first_name, last_name = '123 Silva'.split(" ")
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f'{self.base_url}/patient/name/{first_name}/lastName/{last_name}', headers=headers)

        self.assertNotEqual(response.status_code, 200)


if __name__ == "__main__":

    unittest.main(verbosity=2)

