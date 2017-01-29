from bs4 import BeautifulSoup
import requests
from subprocess import call

# Global Variables

URL = 'http://www.geeksforgeeks.org/tag/amazon/page/'
# TODO: Make the number of pages dynamic
PAGES = 1

links_to_crawl = []
file_names = []


def get_crawl_links():
    page = 1
    while page <= PAGES:
        url = URL + str(page)
        print("Getting from Page Number: " + str(page))
        # Create a Beautiful Soup Object
        soup = create_soup(url)

        links = soup.select(".entry-title > a")
        for link in links:
            links_to_crawl.append(link.get('href'))
            file_names.append(link.text.replace("|", "-"))
        page += 1


def create_soup(url):
    r = requests.get(url)
    return BeautifulSoup(r.text, 'html.parser')


def generate_html():
    i = 0
    for link in links_to_crawl:
        print("Getting file" + file_names[i])
        # Uses wkhtmltopdf which is installed via a windows excecutable. Files are saved in D drive.
        PATH_TO_WKHTML = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe "
        OUTPUT_FOLDER = "D:\\Study\\Amazon1\\"
        command = PATH_TO_WKHTML + "\"" + link + "\" \"" + OUTPUT_FOLDER + file_names[i] + ".pdf\""

        call(command)
        i += 1


def main():
    get_crawl_links()
    generate_html()

if __name__ == '__main__':
    main()
