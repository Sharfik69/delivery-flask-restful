import json
import os
import app
import unittest
import tempfile
from app import create_app
import test_data

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.db_fd, self.app.config['DATABASE'] = tempfile.mkstemp()
        self.app.config['TESTING'] = True
        self.app2 = self.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.remove(self.app.config['DATABASE'])

    def test_simple_connection(self):
        rv = self.app2.get('/')
        assert 'ok' in str(rv.data)

    def test_add_courier_empty(self):
        """
        Добавление курьера, пустой запрос
        """
        rv = self.app2.post('/couriers')
        data = json.loads(rv.data)
        assert data == {"validation_error": {"couriers": []}}
        assert rv.status_code == 400

    def test_add_courier_bad_time(self):
        """
        Добавление курьера с неправильным временем
        """
        req = json.dumps(test_data.courier_bad_time)
        rv = self.app2.post('/couriers', data=req, content_type='application/json')
        data = json.loads(rv.data)
        assert data == test_data.courier_bad_time_ans
        assert rv.status_code == 400

    def test_add_courier_bad_field(self):
        """
        Добавление курьера с некорректными или пустыми полями
        """
        req = json.dumps(test_data.courier_bad_field)
        rv = self.app2.post('/couriers', data=req, content_type='application/json')
        data = json.loads(rv.data)
        assert data == test_data.courier_bad_field_ans
        assert rv.status_code == 400

if __name__ == '__main__':
    unittest.main()
