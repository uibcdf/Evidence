from .database import DataBase

name = 'PhosphoSitePlus'

class PhosphoSitePlus(DataBase):

    def __init__(self, id=None):

        self.name = 'PhosphoSitePlus'
        self.id = id
        self.long_name = 'PhosphoSitePlus'
        self.web = 'https://www.phosphosite.org/homeAction.action'
        self.webid = 'https://www.phosphosite.org/homeAction.action'
        self.info = ''

