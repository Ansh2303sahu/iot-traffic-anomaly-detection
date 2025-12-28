# IoT Network Traffic Anomaly Detection using Machine Learning 🔐📡

## 📌 Project Overview
This project implements an **end-to-end machine learning pipeline** to detect **anomalous and malicious network traffic** in **IoT environments**.

It focuses on processing large-scale network traffic logs, extracting meaningful features, and evaluating multiple machine learning models to classify **benign vs malicious behavior**.

The project is designed as a **clean, modular, and reproducible ML workflow**, suitable for learning and experimentation in **cybersecurity and applied machine learning**.

---

## 🎯 Objectives
- Analyze IoT network traffic data  
- Perform data cleaning and feature engineering  
- Train and compare multiple machine learning models  
- Detect anomalous or malicious traffic patterns  
- Build a reusable ML experimentation pipeline  

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Machine Learning:** scikit-learn  
- **Data Processing:** Pandas, NumPy  

### Models Implemented
- Logistic Regression  
- Decision Tree  
- Random Forest  
- Naive Bayes  
- Linear Support Vector Machine (SVM)  

---

## 📂 Project Structure
iot-traffic-anomaly-detection/
│
├── src/
│ ├── train_models.py # Main training pipeline
│ ├── iot23.py # Dataset schema, features & utilities
│ └── helpers/
│ ├── log_helper.py
│ └── process_helper.py
│
├── data/ # Dataset directories (not included)
│ ├── scenarios/
│ ├── attacks/
│ └── processed/
│
├── experiments/ # Generated results & reports
├── app_config.py # Centralized configuration
└── README.md

---

## 🧪 Feature Engineering
The project evaluates model performance using different feature groups, including:

### 🔹 Basic Network Features
- Ports, protocols, services  
- Packet and byte-level statistics  

### 🔹 Statistical Traffic Features
- Extended traffic behavior metrics  
- Connection-level statistics  

This enables effective comparison of models under different feature representations.

---

## 🚀 Workflow
1. **Data Ingestion**  
   Network traffic logs are loaded from scenario-based datasets.

2. **Data Cleaning & Preprocessing**
   - Handling missing values  
   - Encoding categorical attributes  
   - Scaling numerical features  

3. **Model Training**  
   Multiple machine learning models are trained using standardized pipelines.

4. **Evaluation & Comparison**  
   Model performance is evaluated and saved for comparison.

---

## ▶️ How to Run

⚠️ **The dataset is not included in this repository due to size constraints.**

### Clone the repository
```bash
git clone https://github.com/Ansh2303sahu/iot-traffic-anomaly-detection.git
cd iot-traffic-anomaly-detection
Install dependencies
pip install -r requirements.txt

Configure dataset paths

Edit paths inside:

app_config.py

Run the training pipeline
python src/train_models.py

📊 Output
Trained machine learning models

Model performance comparison report (Excel format)

Experiment logs for further analysis

All outputs are stored inside the experiments/ directory.

📈 Learning Outcomes
Built an end-to-end ML pipeline for anomaly detection

Gained experience working with network traffic data

Implemented and compared classical ML algorithms

Improved understanding of feature engineering in cybersecurity

🔒 Notes
The dataset used is publicly available and commonly used for IoT traffic analysis

Raw dataset files are not committed to this repository

This project is intended for educational and learning purposes

👤 Author

Ansh Sahu
Aspiring Software / Machine Learning Engineer

🔗 GitHub: https://github.com/Ansh2303sahu
