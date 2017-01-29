from bs4 import BeautifulSoup
import requests


def create_soup(url):
    r = requests.get(url)
    return BeautifulSoup(r.text, 'html.parser')


def main():
    url = 'http://www.geeksforgeeks.org/tag/amazon/page/1/'
    soup = create_soup(url)
    print(soup.title.text)

if __name__ == '__main__':
    main()
