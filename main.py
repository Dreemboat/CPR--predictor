#  flask, pandas, scikit learn, pickle mixin.
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
car = pd.read_csv('cleaned_df.csv')

@app.route('/')
def index():
    company = sorted(car['company'].unique())
    name = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = sorted(car['fuel_type'].unique())
    return render_template('index.html', company=company, name=name, year=year, fuel_type=fuel_type)

@app.route('/predict', methods=['POST'])
def predict():
    company = request.form.get('company')
    name = request.form.get('name')
    year = request.form.get('year')
    fuel_type = request.form.get('fuel_type')
    kms_driven = request.form.get('kms_driven')

    return ''

if __name__ == '__main__':
    app.run(debug= True)