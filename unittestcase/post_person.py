import unittest
import requests
import jaydebeapi
from requests.auth import HTTPBasicAuth


class PostPerson(unittest.TestCase):

    def setUp(self):
        self.url = 'http://localhost:8083/v1/post-person'
        self.auth_read = HTTPBasicAuth('testUsername', 'testPassword')
        self.auth_write = HTTPBasicAuth('admin', 'testPassword')
        self.headers = {'Content-Type': 'application/json'}
        self.conn = jaydebeapi.connect("org.h2.Driver",
                                       "jdbc:h2:tcp://localhost:8091/mem:personDB",
                                       ["testDBUsername", "testDBPassword"],
                                       "D:/AutoTest/h2-1.4.200.jar")

    # Required check- json data is empty
    def test_postperson_null(self):
        json = {

        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_write)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)

    # Required check-firstName is null
    def test_postperson_firstname_null(self):
        json = {
            "firstName": "",
            "lastName": "roberts",
            "phoneNumber": "1234567892"
        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_write)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)

    # Required check-last Name is empty
    def test_postperson_lastname_null(self):
        json = {
            "firstName": "John",
            "lastName": "",
            "phoneNumber": "1234567893"
        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_write)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)

    # Required check-phone Number is empty
    def test_postperson_phonenumber_null(self):
        json = {
            "firstName": "Meg",
            "lastName": "Ryan",
            "phoneNumber": ""
        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_write)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)

    # phoneNumber length check - more than 10 digits
    def test_postperson_phonenumber_eleven(self):
        json = {
            "firstName": "Mariah",
            "lastName": "Carey",
            "phoneNumber": "12345678912"
        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_write)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)

    # phone Number length check - less than 10 digits
    def test_postperson_phonenumber_nine(self):
        json = {
            "firstName": "Gareth",
            "lastName": "Gates",
            "phoneNumber": "123456789"
        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_write)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)

    # Authenticated check - unauthenticated
    def test_postperson_unauthorized(self):
        json = {
            "firstName": "Michael",
            "lastName": "Jackson",
            "phoneNumber": "1234567894"
        }
        res = requests.post(url=self.url, json=json, headers=self.headers)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)

    # Authenticated check -read only
    def test_postperson_read(self):
        json = {
            "firstName": "Michael",
            "lastName": "Jackson",
            "phoneNumber": "1234567894"
        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_read)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)

    # data request
    def test_postperson_1_normal(self):
        json = {
            "firstName": "Mark",
            "lastName": "Li",
            "phoneNumber": "2234567899"
        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_write)
        result = res.json()
        self.assertEqual(200, res.status_code)
        id= result['id']
        firstname = result["firstName"]
        lastname = result["lastName"]
        phone = result["phoneNumber"]
        curs = self.conn.cursor()
        sql = 'select * from PERSON where id=' + str(id)
        curs.execute(sql)
        person = curs.fetchone()
        # person = curs.fetchall()
        curs.close()
        self.assertEqual(person[0], id)
        self.assertEqual(str(person[1]), firstname)
        self.assertEqual(str(person[2]), lastname)
        self.assertEqual(person[3], phone)

    # Repeat data request
    def test_postperson_2_repeat(self):
        json = {
            "firstName": "Mark",
            "lastName": "Li",
            "phoneNumber": "2234567899"
        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_write)
        result = res.json()
        self.assertNotEqual(res.status_code, 200)

    # add "id": "1" parameter
    def test_postperson_3_addid(self):
        json = {
            "id": "1",
            "firstName": "Kate",
            "lastName": "Mary",
            "phoneNumber": "1934567800"
        }
        res = requests.post(url=self.url, json=json, headers=self.headers, auth=self.auth_write)
        result = res.json()
        self.assertEqual(200, res.status_code)


if __name__ == '__main__':
    unittest.main()
