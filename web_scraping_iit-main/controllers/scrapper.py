import bs4
import requests
from .file_manager import FolderManager, FileManager

class BookScrapper():

    def __init__(self, url, categorie=''):
        self.url = url
        self.categorie = categorie
        self.int_scraper()

    # cette fonction sert 
    def int_scraper(self):
        r = requests.get(self.url)
        FileManager(self.categorie)
        self.bs4_parser(r)
        
    def bs4_parser(self, r):
        book_data = bs4.BeautifulSoup(r.text, 'html.parser')
        search_values = self.search(book_data)
        self.get_book_url(search_values)
        next = book_data.find_all('li', {'class': 'next'})
        if next:
            pass
            # BookScrapper(next, )

    def search(self, book_data):
        all_book = book_data.find_all('article', {'class': 'product_pod'})
            # search_value = soup.find_all(self.balise, {"class": self.class_name})
        return all_book
    
    def get_book_url(self, datas):
        book_urls = []
        for book in datas:
            book_urls.append([c.get("href").strip() for c in book.find_all("a")][0])
        return book_urls
    
    def get_book_data(self):
        pass
    

class CategorieScrapper():

    def __init__(self, url, BASE_URL=''):
        self.url = url
        self.BASE_URL = BASE_URL
        self.int_scraper() 

    # cette fonction sert 
    def int_scraper(self):
        r = requests.get(self.url)
        self.bs4_parser(r)
        
    def bs4_parser(self, r):
        cat_data = bs4.BeautifulSoup(r.text, 'html.parser')
        search_values = self.search_cat_adn_url(cat_data)
        self.get_all_cat_book_data(search_values)

    def search_cat_adn_url(self, book_data):

        cat_div = book_data.find_all("div", {"class": "side_categories"})
        all_cat = cat_div[0].find_all("a")
        all_cat_val = [a.get_text().strip() for a in all_cat]
        all_cat_url = [self.BASE_URL + a.get("href").strip() for a in all_cat]

        # search_value = soup.find_all(self.balise, {"class": self.class_name})
        return [all_cat_val, all_cat_url]
    
    
    def get_all_cat_book_data(self, urls):
        for i in range(len(urls[0])): 
            FolderManager(urls[0][i])
            BookScrapper(urls[1][i],urls[0][i])   
