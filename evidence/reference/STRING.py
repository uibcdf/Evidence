from .database import DataBase

keyname = 'STRING'
alternative_keynames = []

class STRING(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'STRING'
        self.id = id
        self.web = 'https://string-db.org/'
        self.webid = 'https://string-db.org/'
        self.info = ''

