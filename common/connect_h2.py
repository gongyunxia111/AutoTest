import unittest
import jaydebeapi
from requests.auth import HTTPBasicAuth


class ConnectDataPerson(unittest.TestCase):

    def setUp(self):
        self.url = 'http://localhost:8083/v1/get-person/1'
        self.auth = HTTPBasicAuth('admin', 'testPassword')
        self.headers = {'Content-Type': 'application/json'}

    def test_connect(self):
        self.driver = 'org.h2.Driver'
        driver = self.driver
        url = 'jdbc:h2:tcp://localhost:8083/mem:personDB'
        username = 'testDBUsername'
        password = 'testDBPassword'
        jar = 'D:/AutoTest/h2-1.4.200.jar'
        connect = jaydebeapi.connect(driver, [url, username, password], jar)
        # connect = jaydebeapi.connect(driver, url, [username, password], jar)
        curs = connect.cursor()
        curs.execute('select * from PERSON')
        data = curs.fetchall()
        print(data)
        curs.close()


if __name__ == '__main__':
    unittest.main()
