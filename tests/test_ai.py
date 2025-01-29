import unittest
import json
from api import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_analyze(self):
        response = self.client.post('/analyze', json={"data": [0.5, 0.7, 0.2]})
        self.assertEqual(response.status_code, 200)
        self.assertIn("analysis", response.json)

if __name__ == '__main__':
    unittest.main()
