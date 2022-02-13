import unittest
import requests
from requests.auth import HTTPBasicAuth


class PostPerson(unittest.TestCase):

    def setUp(self):
        self.url = 'http://localhost:8083/v1/post-person'
        self.auth_read = HTTPBasicAuth('testUsername', 'testPassword')
        self.auth_write = HTTPBasicAuth('admin', 'testPassword')
        self.headers = {'Content-Type': 'application/json'}

    # Required check- json data is empty
    def test_postperson_1_null(self):
        json = {

        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_write)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)
        print(res, result)

    # Required check-firstName is null
    def test_postperson_2_firstname_null(self):
        json = {
            "firstName": "",
            "lastName": "roberts",
            "phoneNumber": "1234567892"
        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_write)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)
        print(res, result)

    # Required check-last Name is empty
    def test_postperson_3_lastname_null(self):
        json = {
            "firstName": "John",
            "lastName": "",
            "phoneNumber": "1234567893"
        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_write)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)
        print(res, result)

    # Required check-phone Number is empty
    def test_postperson_4_phonenumber_null(self):
        json = {
            "firstName": "Meg",
            "lastName": "Ryan",
            "phoneNumber": ""
        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_write)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)
        print(res, result)

    # phoneNumber length check - more than 10 digits
    def test_postperson_5_phonenumber_eleven(self):
        json = {
            "firstName": "Mariah",
            "lastName": "Carey",
            "phoneNumber": "12345678912"
        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_write)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)
        print(res, result)

    # phone Number length check - less than 10 digits
    def test_postperson_6_phonenumber_nine(self):
        json = {
            "firstName": "Gareth",
            "lastName": "Gates",
            "phoneNumber": "123456789"
        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_write)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)
        print(res, result)

    # Authenticated check - unauthenticated
    def test_postperson_7_unauthorized(self):
        json = {
            "firstName": "Michael",
            "lastName": "Jackson",
            "phoneNumber": "1234567894"
        }
        res = requests.post(url=self.url, json=json, headers=self.headers)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)
        print(res, result)

    # Authenticated check -read only
    def test_postperson_8_read(self):
        json = {
            "firstName": "Michael",
            "lastName": "Jackson",
            "phoneNumber": "1234567894"
        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_read)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)
        print(res, result)

    # data request
    def test_postperson_9_normal(self):
        json = {
            "firstName": "lucy",
            "lastName": "han",
            "phoneNumber": "1234567895"
        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_write)
        result = res.json()
        self.assertEqual(200, res.status_code)
        print(res, result)

    # Repeat data request
    def test_postperson_10_repeat(self):
        json = {
            "firstName": "lucy",
            "lastName": "han",
            "phoneNumber": "1234567895"
        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_write)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)
        print(res, result)

    # add "id": "1" parameter
    def test_postperson_11_addid(self):
        json = {
            "id": "1",
            "firstName": "lily",
            "lastName": "pan",
            "phoneNumber": "1934567800"
        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_write)
        result = res.json()
        self.assertEqual(200, res.status_code)
        print(res, result)


if __name__ == '__main__':
    unittest.main()
