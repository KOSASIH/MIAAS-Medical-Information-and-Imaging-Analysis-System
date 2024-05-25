import unittest
import json

from fastapi.testclient import TestClient
from app.main import app

class HospitalAPITestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_create_hospital(self):
        response = self.client.post("/hospitals", json={"name": "Hospital A", "location": "City A"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", json.loads(response.content))

    def test_get_hospital(self):
        response = self.client.post("/hospitals", json={"name": "Hospital B", "location": "City B"})
        self.assertEqual(response.status_code, 201)
        hospital_id = json.loads(response.content)["id"]

        response = self.client.get(f"/hospitals/{hospital_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("name", json.loads(response.content))
        self.assertIn("location", json.loads(response.content))

    def test_update_hospital(self):
        response = self.client.post("/hospitals", json={"name": "Hospital C", "location": "City C"})
        self.assertEqual(response.status_code, 201)
        hospital_id = json.loads(response.content)["id"]

        response = self.client.put(f"/hospitals/{hospital_id}", json={"name": "Hospital C", "location": "City C"})
        self.assertEqual(response.status_code, 200)

    def test_delete_hospital(self):
        response = self.client.post("/hospitals", json={"name": "Hospital D", "location": "City D"})
        self.assertEqual(response.status_code, 201)
        hospital_id = json.loads(response.content)["id"]

        response = self.client.delete(f"/hospitals/{hospital_id}")
        self.assertEqual(response.status_code, 204)
