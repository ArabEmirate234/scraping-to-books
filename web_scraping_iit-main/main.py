from controllers import scrapper

def main():
    url = 'https://books.toscrape.com/'
    BASE_URL = "https://books.toscrape.com/"

    scrapper.CategorieScrapper(url, BASE_URL)


if __name__ == '__main__':
    main()


