from .database import DataBase

name = 'DOI'

class DOI(DataBase):

    def __init__(self, id=None):

        self.name = 'DOI'
        self.id = id
        self.long_name = 'Digital Object Indentifier System'
        self.web = 'https://www.doi.org/'
        self.webid = 'https://www.doi.org/'
        self.info = ''
