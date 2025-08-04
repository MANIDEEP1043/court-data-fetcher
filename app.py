from flask import Flask, render_template, request, jsonify
from models import db, CaseQuery
from scraper import fetch_case_details
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch_case():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    filing_year = request.form['filing_year']

    # Call scraper
    result = fetch_case_details(case_type, case_number, filing_year)

    # Save in DB
    query = CaseQuery(case_type=case_type, case_number=case_number,
                      filing_year=filing_year, raw_response=str(result))
    db.session.add(query)
    db.session.commit()

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
