import unittest
import requests
import jaydebeapi
from requests.auth import HTTPBasicAuth


class DeletePerson(unittest.TestCase):

    def setUp(self):
        self.auth_read = HTTPBasicAuth('testUsername', 'testPassword')
        self.auth_write = HTTPBasicAuth('admin', 'testPassword')
        self.url = 'http://localhost:8083/v1/delete-person/'
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
        res = requests.delete(url=self.url + str(id))
        self.assertNotEqual(res.status_code, 200)

    # Authentication check-read
    def test_getperson_2_read(self):
        curs = self.conn.cursor()
        curs.execute('select * from PERSON')
        person = curs.fetchone()
        # person = curs.fetchall()
        curs.close()
        id = person[0]
        res = requests.delete(url=self.url + str(id), auth=self.auth_read)
        self.assertNotEqual(res.status_code, 200)

    # Parameter verification - do not fill in the parameters
    def test_getperson_3_null(self):
        self.url = 'http://localhost:8083/v1/delete-person'
        res = requests.delete(url=self.url, auth=self.auth_write)
        self.assertNotEqual(res.status_code, 200)

    # delete non-existent data
    def test_getperson_4_non_existent(self):
        self.url = 'http://localhost:8083/v1/delete-person/9999'
        res = requests.delete(url=self.url, auth=self.auth_write)
        self.assertNotEqual(res.status_code, 200)

    # delete
    def test_getperson_5_normal(self):
        curs = self.conn.cursor()
        curs.execute('select * from PERSON')
        person = curs.fetchone()
        # person = curs.fetchall()
        curs.close()
        global id
        id = person[0]
        res = requests.delete(self.url + str(id), auth=self.auth_write)
        self.assertEqual(200, res.status_code)
        sql = 'select * from PERSON where id=' + str(id)
        curs.execute(sql)
        curs.close()
        self.assertIsNone(curs.fetchone())

    #  repeat delete
    def test_getperson_6_repeat(self):
        url= self.url + str(id)
        print(url)
        res = requests.delete(url=self.url + str(id), auth=self.auth_write)
        self.assertNotEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
