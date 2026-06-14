# Network Intrusion Detection System

A Machine Learning based cybersecurity application that detects malicious network activity from network traffic data.

The system analyzes network connection features and classifies traffic as either:

* Normal Traffic
* Intrusion / Attack

Built using Python, Scikit Learn, Random Forest, and Streamlit.

---

## Features

Intrusion Detection

Attack Classification

CSV Upload Support

Real Time Predictions

Attack Percentage Analysis

Downloadable Results

Interactive Streamlit Interface

---

## Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit Learn

### Model

* Random Forest Classifier

### Deployment

* Streamlit

---

## Dataset

NSL-KDD Dataset

https://www.kaggle.com/datasets/hassan06/nslkdd

Files Used:

* KDDTrain+.txt
* KDDTest+.txt

The dataset contains network traffic features including:

* Protocol Type
* Service
* Connection Flags
* Source Bytes
* Destination Bytes
* Login Information
* Connection Statistics
* Host Statistics

Target Variable:

* Normal Traffic (0)
* Attack Traffic (1)

---

## Machine Learning Pipeline

### 1. Data Preprocessing

* Loaded training and testing datasets
* Converted attack labels into binary classification
* Encoded categorical features
* Aligned train and test feature spaces

### 2. Feature Engineering

Applied One Hot Encoding to:

* protocol_type
* service
* flag

Generated 120+ machine learning features.

### 3. Model Development

Trained a Random Forest Classifier using network traffic features.

Configuration:

* n_estimators = 300
* max_depth = 20
* min_samples_split = 5

### 4. Model Evaluation

Performance on the test dataset:

| Metric    | Score              |
| --------- | ------------------ |
| Accuracy  | 77.3%              |
| Precision | 97% (Attack Class) |
| Recall    | 62% (Attack Class) |
| F1 Score  | 76%                |

---

## Key Findings

Top Features Influencing Intrusion Detection:

| Feature                | Importance |
| ---------------------- | ---------- |
| src_bytes              | 0.130      |
| dst_bytes              | 0.098      |
| flag_SF                | 0.086      |
| dst_host_srv_count     | 0.055      |
| same_srv_rate          | 0.055      |
| dst_host_same_srv_rate | 0.050      |
| diff_srv_rate          | 0.042      |
| logged_in              | 0.041      |

These features were the strongest indicators of malicious network activity.

---
## Results
<img width="1771" height="876" alt="image" src="https://github.com/user-attachments/assets/d6de12d0-4ebf-4f97-8d8a-f6f06623ecc2" />

---

## Project Structure

```text
NetworkIntrusionDetection/
│
├── app.py
├── intrusion.ipynb
├── model.pkl
├── feature_importance.csv
├── attack_traffic.csv
├── KDDTrain+.txt
├── KDDTest+.txt
├── normal_traffic.csv
├── sample_network_traffic.csv
├── requirements.txt
├── README.md
```

---

## Installation

```bash
git clone https://github.com/mugdhachalla/network-intrusion-detection.git
cd network-intrusion-detection
```

Create virtual environment:

```bash
python -m venv ml-env
```

Activate:

Linux / macOS

```bash
source ml-env/bin/activate
```

Windows

```bash
ml-env\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

Application:

```text
http://localhost:8501
```

---

## Learning Outcomes

This project provided practical experience in:

* Cybersecurity Machine Learning
* Intrusion Detection Systems
* Data Preprocessing
* One Hot Encoding
* Random Forest Classification
* Feature Importance Analysis
* Model Evaluation
* Streamlit Deployment

---

## Author

Mugdha Challa
