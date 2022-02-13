import unittest
import requests
import jaydebeapi
from requests.auth import HTTPBasicAuth
from common.connectDB import ConnectDataPerson


class GetPerson(unittest.TestCase):

    def setUp(self):
        self.auth_read = HTTPBasicAuth('testUsername', 'testPassword')
        self.auth_write = HTTPBasicAuth('admin', 'testPassword')
        self.url = 'http://localhost:8083/v1/get-person/'
        self.conn = jaydebeapi.connect("org.h2.Driver",
                                       "jdbc:h2:tcp://localhost:8091/mem:personDB",
                                       ["testDBUsername", "testDBPassword"],
                                       "D:/AutoTest/h2-1.4.200.jar")

    # Authenticated check - not authenticated
    def test_getperson_1_unauthorized(self):
        curs = self.conn.cursor()
        curs.execute('select * from PERSON')
        person = curs.fetchone()
        # person = curs.fetchall()
        curs.close()
        id = person[0]
        firstname = person[1]
        lastname = person[2]
        phone = person[3]
        res = requests.get(url=self.url + str(id))
        self.assertNotEqual(res.status_code, 200)

    # Authentication check-read
    def test_getperson_2_read(self):
        curs = self.conn.cursor()
        curs.execute('select * from PERSON')
        person = curs.fetchone()
        # person = curs.fetchall()
        curs.close()
        id = person[0]
        firstname = person[1]
        lastname = person[2]
        phone = person[3]
        res = requests.get(url=self.url + str(id), auth=self.auth_read)
        result = res.json()
        self.assertEqual(res.status_code,200)
        self.assertEqual(result['id'], id)
        self.assertEqual(str(result["firstName"]), firstname)
        self.assertEqual(str(result["lastName"]), lastname)
        self.assertEqual(result["phoneNumber"], phone)

    # Authentication check-write
    def test_getperson_3_write(self):
        curs = self.conn.cursor()
        curs.execute('select * from PERSON')
        person = curs.fetchone()
        # result = curs.fetchall()
        curs.close()
        id = person[0]
        firstname = person[1]
        lastname = person[2]
        phone = person[3]
        res = requests.get(url=self.url + str(id), auth=self.auth_write)
        result = res.json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(result['id'], id)
        self.assertEqual(str(result["firstName"]), firstname)
        self.assertEqual(str(result["lastName"]), lastname)
        self.assertEqual(result["phoneNumber"], phone)

    # Parameter check - request parameter does not exist
    def test_getperson_4_non_existent(self):
        url = 'http://localhost:8083/v1/get-person/9999'
        res = requests.get(url=url, auth=self.auth_write)
        self.assertNotEqual(res.status_code, 200)

    # Parameter verification - do not fill in the parameters
    def test_getperson_5_null(self):
        url = 'http://localhost:8083/v1/get-person'
        res = requests.get(url=url, auth=self.auth_write)
        self.assertNotEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
