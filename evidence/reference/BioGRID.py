from .database import DataBase

keyname = 'BioGRID'
alternative_keynames = []

class BioGRID(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'BioGRID'
        self.id = id
        self.web = 'https://thebiogrid.org'
        self.webid = 'https://thebiogrid.org'
        self.info = ''
