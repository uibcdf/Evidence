from .database import DataBase

name = 'DOI'

class DOI(DataBase):

    def __init__(self, id=None):

        self.database = 'DOI'
        self.id = id
        self.web = 'https://www.doi.org/'
        self.webid = 'https://www.doi.org/'
        self.info = 'Digital Object Indentifier System'
