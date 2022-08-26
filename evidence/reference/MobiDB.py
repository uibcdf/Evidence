from .database import DataBase

name = 'MobiDB'

class MobiDB(DataBase):

    def __init__(self, id=None):

        self.database = 'MobiDB'
        self.id = id
        self.web = 'https://mobidb.bio.unipd.it/'
        self.webid = 'https://mobidb.bio.unipd.it/{self.id}'
        self.info = 'MobiDB, a database of protein disorder and mobility annotations.'

