import json
import unittest

from app.main import app
from fastapi.testclient import TestClient


class PatientAPITestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_create_patient(self):
        response = self.client.post(
            "/patients", json={"name": "John Doe", "age": 30, "gender": "Male"}
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", json.loads(response.content))

    def test_get_patient(self):
        response = self.client.post(
            "/patients", json={"name": "Jane Doe", "age": 25, "gender": "Female"}
        )
        self.assertEqual(response.status_code, 201)
        patient_id = json.loads(response.content)["id"]

        response = self.client.get(f"/patients/{patient_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("name", json.loads(response.content))
        self.assertIn("age", json.loads(response.content))
        self.assertIn("gender", json.loads(response.content))

    def test_update_patient(self):
        response = self.client.post(
            "/patients", json={"name": "John Doe", "age": 30, "gender": "Male"}
        )
        self.assertEqual(response.status_code, 201)
        patient_id = json.loads(response.content)["id"]

        response = self.client.put(
            f"/patients/{patient_id}",
            json={"name": "John Doe", "age": 31, "gender": "Male"},
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_patient(self):
        response = self.client.post(
            "/patients", json={"name": "John Doe", "age": 30, "gender": "Male"}
        )
        self.assertEqual(response.status_code, 201)
        patient_id = json.loads(response.content)["id"]

        response = self.client.delete(f"/patients/{patient_id}")
        self.assertEqual(response.status_code, 204)
