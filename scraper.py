from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

def fetch_case_details(case_type, case_number, filing_year):
    url = "https://delhihighcourt.nic.in/"  # Change to chosen court
    data = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        # Fill form (example, adapt to actual site structure)
        page.fill('input[name="case_type"]', case_type)
        page.fill('input[name="case_number"]', case_number)
        page.fill('input[name="filing_year"]', filing_year)
        page.click('button[type="submit"]')

        time.sleep(3)  # wait for results

        html = page.content()
        soup = BeautifulSoup(html, 'html.parser')

        # Parse required details (adjust selectors)
        data['parties'] = [x.text.strip() for x in soup.select('.party')]
        data['dates'] = [x.text.strip() for x in soup.select('.date')]
        data['pdf_links'] = [a['href'] for a in soup.select('a[href$=".pdf"]')]

        browser.close()

    return data
