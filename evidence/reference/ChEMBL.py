from .database import DataBase

name = 'ChEMBL'

class ChEMBL(DataBase):

    def __init__(self, id=None):

        self.database = 'ChEMBL'
        self.id = id
        self.web = 'https://www.ebi.ac.uk/chembl/'
        self.webid = 'https://www.ebi.ac.uk/chembl/'
        self.info = ''

