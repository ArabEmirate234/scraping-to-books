import xlsxwriter
import os


class FolderManager():
    
    def __init__(self, categorie):

        self.categorie = categorie
        self.create_folder()

    def create_folder(self):
        try:
            os.mkdir('datas')
        except:
            pass

        try:
            os.mkdir(self.categorie)
        except:
            pass
            

class FileManager():
    def __init__(self, categorie, book=None):

        self.book = book
        self.categorie = categorie
        self.create_file()
        self.create_image_folder()

    def create_image_folder(self):
        try:
            os.mkdir(self.categorie +'/'+'images')
        except:
            pass

    def create_file(self):
        wb = xlsxwriter.Workbook(self.categorie  + '/' +"data.xlsx")
        sheet1 = wb.add_worksheet()
        wb.close()