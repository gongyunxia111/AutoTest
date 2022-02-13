import unittest
import requests
from requests.auth import HTTPBasicAuth


class DeletePerson(unittest.TestCase):

    def setUp(self):
        self.auth_read = HTTPBasicAuth('testUsername', 'testPassword')
        self.auth_write = HTTPBasicAuth('admin', 'testPassword')

    # Authenticated check - not authenticated
    def test_getperson_1_unauthorized(self):
        self.url = 'http://localhost:8083/v1/delete-person/1'
        res = requests.delete(url=self.url)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)
        print(res, result)

    # Authentication check-read
    def test_getperson_2_read(self):
        self.url = 'http://localhost:8083/v1/delete-person/1'
        res = requests.delete(url=self.url, auth=self.auth_read)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)
        print(res, result)

    # Parameter verification - do not fill in the parameters
    def test_getperson_3_null(self):
        self.url = 'http://localhost:8083/v1/delete-person'
        res = requests.delete(url=self.url, auth=self.auth_write)
        self.assertNotEqual(res.status_code, 200)
        print(res)

    # delete non-existent data
    def test_getperson_4_non_existent(self):
        self.url = 'http://localhost:8083/v1/delete-person/1000'
        res = requests.delete(url=self.url, auth=self.auth_write)
        self.assertNotEqual(res.status_code, 200)
        print(res)

    # delete
    def test_getperson_5_normal(self):
        self.url = 'http://localhost:8083/v1/delete-person/1'
        res = requests.delete(url=self.url, auth=self.auth_write)
        self.assertEqual(200, res.status_code)
        print(res)

    #  repeat delete
    def test_getperson_6_repeat(self):
        self.url = 'http://localhost:8083/v1/delete-person/1'
        res = requests.delete(url=self.url, auth=self.auth_write)
        self.assertNotEqual(res.status_code, 200)
        print(res)


if __name__ == '__main__':
    unittest.main()
