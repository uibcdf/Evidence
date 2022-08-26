from .database import DataBase

keyname = 'ChEMBL'
alternative_keynames = []

class ChEMBL(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'ChEMBL'
        self.id = id
        self.web = 'https://www.ebi.ac.uk/chembl/'
        self.webid = 'https://www.ebi.ac.uk/chembl/'
        self.info = ''

