import unittest
import requests


class TestPharmaciesResources(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:5000/"

        payload = {"username": "yuri", "password": "teste1234"}
        response = requests.post(f'{self.base_url}/login', json=payload)
        self.token = response.json().get('access_token')

    def test_list_pharmacies_values_must_return_list(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f'{self.base_url}/pharmacies', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json()['Pharmacies'], list)

    def test_get_pharmacy_by_name_with_valid_name(self):
        name = 'Droga Mais'
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f'{self.base_url}/pharmacy/name/{name}', headers=headers)

        self.assertEqual(response.status_code, 200)

    def test_get_pharmacy_by_name_with_invalid_name(self):
        name = 'DROGA1SUPER'
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f'{self.base_url}/pharmacy/name/{name}', headers=headers)

        self.assertNotEqual(response.status_code, 200)

    def test_get_pharmacy_by_city_with_valid_city_name(self):
        name = 'Sao Simao'
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f'{self.base_url}/pharmacy/city/{name}', headers=headers)

        self.assertEqual(response.status_code, 200)

    def test_get_pharmacy_by_city_with_invalid_city_name(self):
        name = ''
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f'{self.base_url}/pharmacy/city/{name}', headers=headers)

        self.assertNotEqual(response.status_code, 200)

    def test_get_pharmacy_by_name_and_city_with_valid_city_and_pharmacy_name(self):
        city, name = 'Sao Paulo', 'Droga Mais'
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f'{self.base_url}/pharmacy/city/{city}/name/{name}', headers=headers)

        self.assertEqual(response.status_code, 200)

    def test_get_pharmacy_by_name_and_city_with_invalid_city_and_valid_pharmacy_name(self):
        city, name = 'Sa1 Paulo', 'Droga Mais'
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f'{self.base_url}/pharmacy/city/{city}/name/{name}', headers=headers)

        self.assertNotEqual(response.status_code, 200)

    def test_get_pharmacy_by_name_and_city_with_valid_city_and_invalid_pharmacy_name(self):
        city, name = 'Sao Paulo', ''
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f'{self.base_url}/pharmacy/city/{city}/name/{name}', headers=headers)

        self.assertNotEqual(response.status_code, 200)


if __name__ == "__main__":

    unittest.main(verbosity=2)

