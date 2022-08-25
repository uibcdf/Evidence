from .database import DataBase

name = 'OMIM'

class OMIM(DataBase):

    def __init__(self, id=None):

        self.name = 'OMIM'
        self.id = id
        self.long_name = 'Online Mendelian Inheritance in Man'
        self.web = 'https://www.omim.org/'
        self.webid = 'https://www.omim.org/entry/{self.id}'
        self.info = ''

