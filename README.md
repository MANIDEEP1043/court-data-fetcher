# Court-Data Fetcher & Mini-Dashboard

## Court Chosen
**Delhi High Court** – [https://delhihighcourt.nic.in/](https://delhihighcourt.nic.in/)  
*(You can adapt the scraper for other District Courts via the eCourts portal.)*

---

## Setup Steps

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/court-data-fetcher.git
cd court-data-fetcher
```

### 2. Create Virtual Environment & Install Dependencies
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
playwright install
```

### 3. Set Environment Variables
Create a `.env` file with the following content:
```ini
COURT_URL=https://delhihighcourt.nic.in/
DB_URI=sqlite:///database.db
SECRET_KEY=your_secret_key
```
*(Replace `your_secret_key` with a securely generated key.)*

### 4. Run the Application
```bash
flask run
```
Visit: [http://localhost:5000](http://localhost:5000)

---

## CAPTCHA Strategy
Most Indian court portals use CAPTCHA to prevent bots.  
For this project:  
- We use **manual entry** or **session reuse** for CAPTCHA.  
- The scraper pauses for user input if CAPTCHA appears (or user can supply token manually).  
- Documented for legal compliance; **no automated CAPTCHA breaking**.  

---

## Project Structure
```
court-data-fetcher/
│
├── app.py                # Flask main app
├── scraper.py            # Playwright/Selenium scraping logic
├── models.py             # Database models (SQLite)
├── templates/
│   └── index.html        # UI (form + results)
├── static/
│   └── style.css         # Optional CSS
├── requirements.txt      # Python dependencies
├── README.md             # This documentation
├── .env                  # Environment variables
└── database.db           # SQLite database file
```

---
