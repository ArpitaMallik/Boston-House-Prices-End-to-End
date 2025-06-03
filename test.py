import unittest
import json
from app import app, model, scalar

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Boston House Price Prediction', response.data)

    def test_predict_api(self):
        test_data = {'data': {'CRIM': 0.1, 'ZN': 18.0, 'INDUS': 2.31, 
                              'CHAS': 0, 'NOX': 0.538, 'RM': 6.575, 
                              'Age': 65.2, 'DIS': 4.09, 'RAD': 1.0, 
                              'TAX': 296.0, 'PTRATIO': 15.3, 'B': 396.9, 
                              'LSTAT': 4.98}}

        response = self.app.post('/predict_api', data=json.dumps(test_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'prediction', response.data)

    def test_predict_form(self):
        form_data = {
            'CRIM': 0.1, 'ZN': 18.0, 'INDUS': 2.31, 
            'CHAS': 0, 'NOX': 0.538, 'RM': 6.575, 
            'Age': 65.2, 'DIS': 4.09, 'RAD': 1.0, 
            'TAX': 296.0, 'PTRATIO': 15.3, 'B': 396.9, 
            'LSTAT': 4.98
        }
        response = self.app.post('/predict', data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The house price prediction is', response.data)

if __name__ == '__main__':
    unittest.main()