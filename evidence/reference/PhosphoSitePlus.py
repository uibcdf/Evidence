from .database import DataBase

keyname = 'PhosphoSitePlus'
alternative_keynames = []

class PhosphoSitePlus(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'PhosphoSitePlus'
        self.id = id
        self.web = 'https://www.phosphosite.org/homeAction.action'
        self.webid = 'https://www.phosphosite.org/homeAction.action'
        self.info = 'PhosphoSitePlus'

