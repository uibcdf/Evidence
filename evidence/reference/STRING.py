from .database import DataBase

name = 'STRING'

class STRING(DataBase):

    def __init__(self, id=None):

        self.name = 'STRING'
        self.id = id
        self.long_name = ''
        self.web = 'https://string-db.org/'
        self.webid = 'https://string-db.org/'
        self.info = ''

