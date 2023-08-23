import unittest
from app import application

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        application.testing = True
        self.app = application.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contoh Flask-MySQL', response.data)

    def test_insert(self):
        data = {
            'nama': 'John Doe',
            'no_telp': '1234567890'
        }
        response = self.app.post('/insert', data=data)
        self.assertEqual(response.status_code, 302)  # Redirect to index after insert

    def test_update(self):
        response = self.app.get('/update/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ubah Data', response.data)

    def test_delete(self):
        response = self.app.get('/delete/1')
        self.assertEqual(response.status_code, 302)  # Redirect to index after delete

if __name__ == '__main__':
    unittest.main()
