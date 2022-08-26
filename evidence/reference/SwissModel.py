from .database import DataBase

name = 'SwissModel'

class SwissModel(DataBase):

    def __init__(self, id=None):

        self.database = 'SwissModel'
        self.id = id
        self.web = 'https://swissmodel.expasy.org/'
        self.webid = 'https://swissmodel.expasy.org/'
        self.info = 'Swiss-Model Repository'

