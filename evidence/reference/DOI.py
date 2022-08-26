from .database import DataBase

keyname = 'DOI'
alternative_keynames = []

class DOI(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'DOI'
        self.id = id
        self.web = 'https://www.doi.org/'
        self.webid = 'https://www.doi.org/'
        self.info = 'Digital Object Indentifier System'
