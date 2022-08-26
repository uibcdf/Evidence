from .database import DataBase

name = 'OMIM'

class OMIM(DataBase):

    def __init__(self, id=None):

        self.database = 'OMIM'
        self.id = id
        self.web = 'https://www.omim.org/'
        self.webid = 'https://www.omim.org/entry/{self.id}'
        self.info = 'Online Mendelian Inheritance in Man'

