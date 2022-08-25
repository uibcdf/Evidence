from .database import DataBase

name = 'ChEMBL'

class ChEMBL(DataBase):

    def __init__(self, id=None):

        self.name = 'ChEMBL'
        self.id = id
        self.long_name = 'ChEMBL'
        self.web = 'https://www.ebi.ac.uk/chembl/'
        self.webid = 'https://www.ebi.ac.uk/chembl/'
        self.info = ''

