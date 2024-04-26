import unittest
import requests


class TestUsersResourceWithoutDeleteAndPut(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:5000/"

        payload = {"username": "Yuri", "password": "teste1234"}
        response = requests.post(f"{self.base_url}/login", json=payload)
        self.token = response.json().get("access_token")

    # TESTS IN {self.base}/user/{username}
    def test_get_user_informations_with_valid_username(self):
        username = "Yuri"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{self.base_url}/user?username={username}", headers=headers)

        self.assertEqual(response.status_code, 200)

    def test_get_user_informations_with_invalid_username(self):
        username = "1"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{self.base_url}/user?username={username}", headers=headers)

        self.assertNotEqual(response.status_code, 200)

    # TESTS IN {self.base}/logout
    def test_logout(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(f"{self.base_url}/logout", headers=headers)

        self.assertEqual(response.status_code, 200)

    # TESTS IN {self.base}/login
    def test_user_login_with_valid_username_and_invalid_password(self):
        payload = {"username": "Yuri", "password": "teste"}
        response = requests.post(f"{self.base_url}/login", json=payload)

        self.assertNotEqual(response.status_code, 200)

    def test_user_login_with_invalid_username_and_valid_password(self):
        payload = {"username": "YuRi", "password": "teste1234"}
        response = requests.post(f"{self.base_url}/login", json=payload)

        self.assertNotEqual(response.status_code, 200)

    # TESTS IN {self.base}/register
    def test_register_user_with_valid_username_and_password(self):
        payload = {"username": "maria", "password": "teste@"}
        response = requests.post(f"{self.base_url}/register", json=payload)

        self.assertEqual(response.status_code, 201)

    def test_register_user_with_valid_username_and_invalid_password(self):
        payload = {"username": "arthur", "password": ""}
        response = requests.post(f"{self.base_url}/register", json=payload)

        self.assertNotEqual(response.status_code, 200)

    def test_register_user_with_invalid_username_and_valid_password(self):
        payload = {"username": "", "password": "teste@"}
        response = requests.post(f"{self.base_url}/register", json=payload)

        self.assertNotEqual(response.status_code, 200)


if __name__ == "__main__":

    unittest.main(verbosity=2)
