# SecureShield: Real-Time Credit Card Fraud Detection API

An end-to-end Machine Learning solution built to analyze financial transactions and predict potential frauds in real-time.

## 🛠️ Tech Stack
- **Database:** Oracle SQL / Relational DB Structure
- **Core ML:** Python, Pandas, Scikit-Learn (Random Forest Classifier)
- **Backend/API:** Flask Web Framework

## 🚀 API Endpoint & Sample Request
- **URL:** `/predict_fraud` [POST]
- **Sample Request (cURL):**
curl -X POST http://127.0.0.1:5000/predict_fraud -H "Content-Type: application/json" -d "{\"amount\": 92000.00, \"location_code\": 1}"
