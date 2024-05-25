import unittest

from .test_doctor_api import DoctorAPITestCase
from .test_hospital_api import HospitalAPITestCase
from .test_patient_api import PatientAPITestCase

__all__ = ["PatientAPITestCase", "DoctorAPITestCase", "HospitalAPITestCase"]
