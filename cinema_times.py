from bs4 import BeautifulSoup
from fpdf import FPDF
import requests


# cinema times
def get_cinema_times():
    # enter url
    url = ''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = soup.find_all('ul', {'class': 'Sessions'})
    cinema_times = []
    for movie in movies:
        title = movie.find('li', {'data-name': True}).get('data-name').strip()
        times = [time.text for time in movie.find_all(
            'span', {'class': 'Time'})]
        cinema_times.append({'title': title, 'times': times})

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, f"Tomorrow's Cinema Times:", 0, 1)
    pdf.set_font('Arial', '', 12)
    for movie in cinema_times:
        pdf.cell(0, 10, movie['title'], 0, 1)
        for time in movie['times']:
            pdf.cell(10)
            pdf.cell(0, 10, time, 0, 1)
        pdf.cell(0, 10, '', 0, 1)

    pdf.output('cinema_times.pdf')


get_cinema_times()
