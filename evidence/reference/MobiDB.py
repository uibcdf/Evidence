from .database import DataBase

name = 'MobiDB'

class MobiDB(DataBase):

    def __init__(self, id=None):

        self.name = 'MobiDB'
        self.id = id
        self.long_name = 'MobiDB, a database of protein disorder and mobility annotations.'
        self.web = 'https://mobidb.bio.unipd.it/'
        self.webid = 'https://mobidb.bio.unipd.it/{self.id}'
        self.info = ''

