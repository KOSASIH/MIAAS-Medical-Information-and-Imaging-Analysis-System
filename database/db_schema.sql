-- Create the patients table
CREATE TABLE patients (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW()
);

-- Create the doctors table
CREATE TABLE doctors (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone VARCHAR(20),
  address VARCHAR(255),
  specialty VARCHAR(100),
  hospital_id INTEGER REFERENCES hospitals(id),
  created_at TIMESTAMP DEFAULT NOW()
);

-- Create the hospitals table
CREATE TABLE hospitals (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  zip VARCHAR(10) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Create the medical_images table
CREATE TABLE medical_images (
  id SERIAL PRIMARY KEY,
  patient_id INTEGER REFERENCES patients(id),
  doctor_id INTEGER REFERENCES doctors(id),
  hospital_id INTEGER REFERENCES hospitals(id),
  image_path VARCHAR(255) NOT NULL,
  image_type VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Create the medical_reports table
CREATE TABLE medical_reports (
  id SERIAL PRIMARY KEY,
  patient_id INTEGER REFERENCES patients(id),
  doctor_id INTEGER REFERENCES doctors(id),
  hospital_id INTEGER REFERENCES hospitals(id),
  report_path VARCHAR(255) NOT NULL,
  report_type VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Create the medical_records table
CREATE TABLE medical_records (
  id SERIAL PRIMARY KEY,
  patient_id INTEGER REFERENCES patients(id),
  doctor_id INTEGER REFERENCES doctors(id),
  hospital_id INTEGER REFERENCES hospitals(id),
  medical_record_path VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);
