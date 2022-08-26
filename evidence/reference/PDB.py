from .database import DataBase

name = 'PDB'

class PDB(DataBase):

    def __init__(self, id=None):

        self.database = 'PDB'
        self.id = id
        self.web = 'https://www.wwpdb.org/'
        self.webid = 'https://www.wwpdb.org/'
        self.info = 'Protein Data Bank'

