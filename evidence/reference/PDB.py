from .database import DataBase

keyname = 'PDB'
alternative_keynames = []

class PDB(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'PDB'
        self.id = id
        self.web = 'https://www.wwpdb.org/'
        self.webid = 'https://www.wwpdb.org/'
        self.info = 'Protein Data Bank'

