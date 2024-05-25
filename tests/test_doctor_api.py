import unittest
import json

from fastapi.testclient import TestClient
from app.main import app

class DoctorAPITestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_create_doctor(self):
        response = self.client.post("/doctors", json={"name": "Dr. John Doe", "specialty": "Cardiology"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", json.loads(response.content))

    def test_get_doctor(self):
        response = self.client.post("/doctors", json={"name": "Dr. Jane Doe", "specialty": "Pediatrics"})
        self.assertEqual(response.status_code, 201)
        doctor_id = json.loads(response.content)["id"]

        response = self.client.get(f"/doctors/{doctor_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("name", json.loads(response.content))
        self.assertIn("specialty", json.loads(response.content))

    def test_update_doctor(self):
        response = self.client.post("/doctors", json={"name": "Dr. John Doe", "specialty": "Cardiology"})
        self.assertEqual(response.status_code, 201)
        doctor_id = json.loads(response.content)["id"]

        response = self.client.put(f"/doctors/{doctor_id}", json={"name": "Dr. John Doe", "specialty": "Cardiology"})
        self.assertEqual(response.status_code, 200)

    def test_delete_doctor(self):
        response = self.client.post("/doctors", json={"name": "Dr. John Doe", "specialty": "Cardiology"})
        self.assertEqual(response.status_code, 201)
        doctor_id = json.loads(response.content)["id"]

        response = self.client.delete(f"/doctors/{doctor_id}")
        self.assertEqual(response.status_code, 204)
