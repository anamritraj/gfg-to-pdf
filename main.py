from bs4 import BeautifulSoup
import requests

# Global Variables

URL = 'http://www.geeksforgeeks.org/tag/amazon/page/'
# TODO: Make the number of pages dynamic
PAGES = 30

to_crawl = []
crawled = []


def get_crawl_links():
    page = 1
    while page < PAGES:
        url = URL + str(page)
        print("Getting from Page Number: " + str(page))
        # Create a Beautiful Soup Object
        soup = create_soup(url)

        links = soup.select(".entry-title > a")
        for link in links:
            to_crawl.append(link.get('href'))
        page += 1


def create_soup(url):
    r = requests.get(url)
    return BeautifulSoup(r.text, 'html.parser')


def main():
    get_crawl_links()

if __name__ == '__main__':
    main()
