
import unittest
from app import app

class CommandControlTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Command and Control System", response.get_json()["message"])

    def test_analyze_command(self):
        response = self.app.post('/analyze_command', json={"command": "Deploy resources immediately."})
        self.assertEqual(response.status_code, 200)
        self.assertIn("analysis", response.get_json())

    def test_geospatial_event(self):
        event_data = {"latitude": 34.05, "longitude": -118.25, "event_type": "Deployment"}
        response = self.app.post('/geospatial_event', json=event_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.get_json())

if __name__ == '__main__':
    unittest.main()
