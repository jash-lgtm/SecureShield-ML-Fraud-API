import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# --- ૧. મશીન લર્નિંગ મોડલ ટ્રેનિંગ (જે આપણે પહેલા કર્યું તે જ) ---
data = {
    'AMOUNT': [500.00, 95000.00, 1200.00, 85000.00, 300.00],
    'LOCATION_CODE': [0, 1, 0, 1, 0],  # 0 = Domestic, 1 = International
    'IS_FRAUD': [0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)
X = df[['AMOUNT', 'LOCATION_CODE']]
y = df['IS_FRAUD']

model = RandomForestClassifier(n_estimators=10)
model.fit(X, y)
print("🧠 ML મોડલ બેકએન્ડમાં રેડી છે...")

# --- ૨. વેબ API એન્ડપોઇન્ટ (Route) બનાવવો ---
@app.route('/predict_fraud', methods=['POST'])
def predict_fraud():
    try:
        # સામેથી આવતો ડેટા (JSON ફોર્મેટમાં) મેળવો
        json_data = request.get_json()
        
        amount = float(json_data['amount'])
        location_code = int(json_data['location_code'])
        
        # મોડલ પાસે પ્રેડિક્શન કરાવો
        input_data = pd.DataFrame([[amount, location_code]], columns=['AMOUNT', 'LOCATION_CODE'])
        prediction = model.predict(input_data)
        
        # રિઝલ્ટ નક્કી કરો
        result = "FRAUD" if prediction[0] == 1 else "SAFE"
        
        return jsonify({
            "status": "success",
            "amount": amount,
            "prediction": result
        })
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# --- ૩. સર્વર લાઈવ કરો ---
if __name__ == '__main__':
    print("🚀 SecureShield API સર્વર ચાલુ થઈ રહ્યું છે...")
    app.run(host='0.0.0.0', port=5000, debug=True)