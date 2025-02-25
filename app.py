from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load("model/bike_price_model.pkl")
scaler = joblib.load("model/scaler.pkl")

# Define brand_Models globally or as a function to avoid redundancy
brand_Models = {
    "Bajaj": ["avenger 220", "ct 100", "dominar 400", "platina 110", "pulsar 150"],
    "Yamaha": ["fascino 125", "fz v3", "mt-15", "r15 v4", "ray zr"],
    "KTM": ["125 duke", "250 duke", "390 adventure", "duke 200", "rc 390"],
    "Royal Enfield": ["classic 350", "himalayan", "hunter 350", "interceptor 650", "meteor 350"],
    "Hero": ["glamour", "hf deluxe", "passion pro", "splendor plus", "xtreme 160r"],
    "TVS": ["apache rtr 160", "jupiter", "ntorq 125", "ronin", "sport"],
    "Honda": ["activa", "cbr 650r", "dio", "shine", "unicorn"],
    "Kawasaki": ["ninja 300", "ninja 400", "versys 650", "vulcan s", "z650"]
}

@app.route('/')
def home():
    return render_template('index.html', brand_Models=brand_Models)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        avg_distance = float(request.form['avg_distance'])
        brand = request.form['brand']
        model_name = request.form['model']
        price = float(request.form['price'])
        engine_capacity = float(request.form['engine_capacity'])
        mileage = float(request.form['mileage'])
        owner_type = request.form['owner_type']
        insurance_status = request.form['insurance_status']
        seller_type = request.form['seller_type']
        city_tier = request.form['city_tier']
        vehicle_age = float(request.form['vehicle_age'])

        # Convert categorical variables
        owner_map = {'first': 1, 'second': 2, 'third': 3}
        insurance_map = {'active': 1, 'expired': 0, 'not available': -1}
        seller_map = {'dealer': 1, 'individual': 0}
        city_map = {'tier 1': 1, 'tier 2': 2, 'tier 3': 3, 'metro': 0}

        owner_type = owner_map.get(owner_type, 0)
        insurance_status = insurance_map.get(insurance_status, 0)
        seller_type = seller_map.get(seller_type, 0)
        city_tier = city_map.get(city_tier, 0)

        brand_encoded = hash(brand) % 1000  # Simple encoding (use same encoding as in training)
        model_encoded = hash(model_name) % 1000

        # Feature vector
        features = np.array([[avg_distance, brand_encoded, model_encoded, price, engine_capacity,
                             mileage, owner_type, insurance_status, seller_type, city_tier, vehicle_age]])

        # Scale the features
        scaled_features = scaler.transform(features)

        # Predict resale price
        resale_price = model.predict(scaled_features)[0]

        return render_template('index.html', prediction=round(resale_price, 2), brand_Models=brand_Models)

    except Exception as e:
        return render_template('index.html', error=str(e), brand_Models=brand_Models)

if __name__ == '__main__':
    app.run(debug=True)