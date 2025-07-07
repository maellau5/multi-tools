# pip install beautifulsoup4
from bs4 import BeautifulSoup

def html_scanner(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup.prettify())

if __name__ == "__main__":
    with open('example.html', 'r') as file:
        html_content = file.read()
        html_scanner(html_content)