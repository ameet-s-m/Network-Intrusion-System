# 🔐 Network Intrusion Detection System (NIDS)  
### Using Machine Learning with DevOps & MLOps Integration

---

## 📌 Overview

This project is a **Machine Learning-based Network Intrusion Detection System (NIDS)** that detects whether network traffic is **Normal or Malicious (Attack)**.

The system is built using:
- **Random Forest ML Model**
- **Flask Web Application**
- **Interactive Dashboard with Visualization**

It also integrates **DevOps and MLOps practices** for structured development, deployment, and model management.

---

## 🚀 Features

- ✅ Real-time Intrusion Detection  
- 📊 Live Graph Visualization (Chart.js)  
- 🚨 Alert System (Visual + Sound)  
- 🧠 Confidence Score for Predictions  
- ⚡ Simulation Mode (Auto Traffic Generation)  
- 🌐 Interactive Web Dashboard  
- 🔄 Hybrid Detection (ML + Rule-Based Logic)

---

## 🛠️ Technologies Used

### Programming & ML
- Python
- Scikit-learn
- Pandas
- NumPy

### Web Development
- Flask
- HTML, CSS, JavaScript

### Visualization
- Chart.js

### DevOps & MLOps
- Git & GitHub
- Model Serialization (Joblib)
- Flask Deployment

---

## 📂 Project Structure


NIDS_Project/
│
├── dataset/
│ ├── KDDTrain+.txt
│ ├── KDDTest+.txt
│
├── model/
│ ├── preprocess.py
│ ├── train_model.py
│ ├── nids_model.pkl
│ ├── feature_names.pkl
│
├── app/
│ ├── app.py
│ ├── templates/
│ │ └── index.html
│ ├── static/
│ │ ├── css/style.css
│ │ └── js/script.js
│
├── README.md


---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/your-username/NIDS-Project.git
cd NIDS-Project
2. Install Dependencies
pip install pandas numpy scikit-learn flask joblib
3. Run the Application
cd app
python app.py
4. Open in Browser
http://127.0.0.1:5000
🧠 How It Works
User inputs network parameters
Data is sent to Flask backend
Preprocessed and passed to ML model
Model predicts:
Normal Traffic
Attack
Result + Confidence displayed
Graph & alerts update in real-time
📊 Dataset
NSL-KDD Dataset
Standard dataset for intrusion detection research
Contains labeled network traffic data
🤖 Model Details
Algorithm: Random Forest Classifier
Accuracy: ~99%
Handles both binary classification (Normal vs Attack)
🔄 DevOps Practices
Version control using Git
GitHub repository management
Structured project organization
Local deployment using Flask
🔁 MLOps Practices
Data preprocessing pipeline
Model training and evaluation
Model saving using Joblib
Real-time inference via API
🚨 Demo Inputs
✅ Normal Traffic
Duration: 10  
Src Bytes: 300  
Dst Bytes: 200  
Protocol: TCP  
Flag: SF  
🚨 Attack Traffic
Duration: 0  
Src Bytes: 20000  
Dst Bytes: 0  
Protocol: ICMP  
Flag: REJ  
📈 Results
High accuracy (~99%)
Real-time detection
Dynamic visualization
Alert system for intrusion detection
🚀 Future Scope
Real-time packet capture (Wireshark)
Cloud deployment
Deep learning integration
CI/CD pipeline automation
Docker containerization
📚 References
NSL-KDD Dataset
Scikit-learn Documentation
Flask Documentation
👨‍💻 Author

Ameet Shankargouda Munavalli
USN: ENG23DS0002
Dayananda Sagar University

⭐ Acknowledgment

This project was developed as part of the DevOps + MLOps Minor Project coursework.
