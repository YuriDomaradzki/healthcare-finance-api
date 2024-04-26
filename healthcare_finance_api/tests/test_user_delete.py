import unittest
import requests


class TestUsersResourceWithoutDelete(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:5000/"

        payload = {"username": "Yuri", "password": "12345"}
        response = requests.post(f"{self.base_url}login", json=payload)
        self.token = response.json().get("access_token")

    # TESTS IN {self.base}/user/{username}
    def test_delete_user_informations_with_valid_username(self):
        username = "Yuri"
        headers = {"Authorization": f"Bearer {self.token}"}
<<<<<<< HEAD
        response = requests.delete(f"{self.base_url}/user?username={username}", headers=headers)
=======
        response = requests.delete(f"{self.base_url}user/{username}", headers=headers)
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117

        self.assertEqual(response.status_code, 200)

    def test_delete_user_informations_with_invalid_username(self):
        username = "1"
        headers = {"Authorization": f"Bearer {self.token}"}
<<<<<<< HEAD
        response = requests.delete(f"{self.base_url}/user?username={username}", headers=headers)
=======
        response = requests.delete(f"{self.base_url}user/{username}", headers=headers)
>>>>>>> df92161d17e6f9b62868867fcc59e7cf84603117

        self.assertNotEqual(response.status_code, 200)


if __name__ == "__main__":

    unittest.main(verbosity=2)
