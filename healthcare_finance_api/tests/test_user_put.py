import unittest
import requests


class TestUsersResourcePut(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:5000/"

        payload = {"username": "Yuri", "password": "teste1234"}
        response = requests.post(f"{self.base_url}/login", json=payload)
        self.token = response.json().get("access_token")

    # TESTS IN {self.base}/user/{username}
    def test_put_user_informations_with_invalid_new_username(self):
        username = "Yuri"
        payload = {"new_username": "1"}
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.put(
            f"{self.base_url}/user?username={username}", headers=headers, json=payload
        )

        self.assertNotEqual(response.status_code, 200)

    def test_put_user_informations_with_invalid_new_password(self):
        username = "Yuri"
        payload = {"new_password": ""}
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.put(
            f"{self.base_url}/user?username={username}", headers=headers, json=payload
        )

        self.assertNotEqual(response.status_code, 200)

    def test_put_user_informations_with_and_valid_new_username_valid_new_password(self):
        username = "Yuri"
        payload = {"new_username": "yuri", "new_password": "12345"}
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.put(
            f"{self.base_url}/user?username={username}", headers=headers, json=payload
        )

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":

    unittest.main(verbosity=2)
