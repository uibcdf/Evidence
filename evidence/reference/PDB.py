from .database import DataBase

name = 'PDB'

class PDB(DataBase):

    def __init__(self, id=None):

        self.name = 'PDB'
        self.id = id
        self.long_name = 'Protein Data Bank'
        self.web = 'https://www.wwpdb.org/'
        self.webid = 'https://www.wwpdb.org/'
        self.info = ''

