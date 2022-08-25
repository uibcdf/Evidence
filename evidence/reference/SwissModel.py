from .database import DataBase

name = 'SwissModel'

class SwissModel(DataBase):

    def __init__(self, id=None):

        self.name = 'SwissModel'
        self.id = id
        self.long_name = 'Swiss-Model Repository'
        self.web = 'https://swissmodel.expasy.org/'
        self.webid = 'https://swissmodel.expasy.org/'
        self.info = ''

