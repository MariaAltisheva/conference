import requests
from bs4 import BeautifulSoup

#https://jsonkeeper.com/b/A34Y

def get_html(url):
    result = requests.get(url)
    return result.text

def get_date(html):
    soup = BeautifulSoup(html, 'lxml')
    print(soup)


def main():
    html = get_html('https://habr.com/ru/companies/kaspersky/articles/725730/')
    print(html)

if __name__ == '__main__':
    main()