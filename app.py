from flask import Flask, render_template, request
import joblib
import pandas as pd  
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__)

scaler = joblib.load('scaler.pkl')
svm_model = joblib.load('svm_model.pkl')

mappings = {
    'diet': {"Balanced": 0, "Low Carb": 1, "High Protein": 2, "Low Protein": 3, "High Carb": 4},
    'supplements': {"No": 0, "Yes": 1},
    'activity': {"Low": 0, "Medium": 1, "High": 2},
    'symptoms': {
        "None": 0, "Frequent Urination": 1, "Pain": 2, 
        "Nausea": 3, "Blood in Urine": 4, "Severe Pain": 5, 
        "Urgency": 6, "Difficulty Urinating": 7, "Burning Urination": 8
    },
    'color': {"Yellow": 0, "Dark Yellow": 1, "Amber": 2, "Cloudy": 3}
}

results = {0: "Healthy", 1: "UTI", 2: "Kidney Stones", 3: "Prostate Infection"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            form_data = {
                'age': float(request.form['age']),
                'weight': float(request.form['weight']),
                'blood_pressure': float(request.form['blood_pressure']),
                'body_temp': float(request.form['body_temp']),
                'protein_in_urine': float(request.form['protein_urine']),
                'urine_density': float(request.form['urine_density']),
                'urine_ph': float(request.form['urine_ph']),
                'diet': mappings['diet'][request.form['diet']],
                'supplements': mappings['supplements'][request.form['supplements']],
                'physical_activity': mappings['activity'][request.form['physical_activity']],
                'symptoms': mappings['symptoms'][request.form['symptoms']],
                'urine_color': mappings['color'][request.form['urine_color']]
            }
            
            if 20 <= form_data['age'] <= 45 and form_data['symptoms'] == mappings['symptoms']["Blood in Urine"]:
                return render_template('result.html', result="Kidney Stones")

            input_data = pd.DataFrame([[
                form_data['age'], form_data['weight'], form_data['diet'],
                form_data['supplements'], form_data['blood_pressure'],
                form_data['symptoms'], form_data['physical_activity'],
                form_data['body_temp'], form_data['protein_in_urine'],
                form_data['urine_density'], form_data['urine_ph'],
                form_data['urine_color']
            ]], columns=['age', 'weight', 'diet', 'supplements', 'blood_pressure', 'symptoms', 'physical_activity', 
                        'body_temp', 'protein_in_urine', 'urine_density', 'urine_ph', 'urine_color'])

            scaled_data = scaler.transform(input_data)
            prediction = svm_model.predict(scaled_data)[0]
            return render_template('result.html', result=results[prediction])

        except Exception as e:
            return render_template('result.html', result=f"Error: {str(e)}")
    
    return render_template('predict.html')


if __name__ == '__main__':
    app.run(debug=True)
