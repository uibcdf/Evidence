from .database import DataBase

keyname = 'ChEBI'
alternative_keynames = []

class ChEBI(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'ChEBI'
        self.id = id
        self.web = 'https://www.ebi.ac.uk/chebi/'
        self.webid = 'https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:{self.id}'
        self.info = 'Chemical Entities of Biological Interest is a freely available dictionary of molecular entities focused on ‘small’ chemical compounds.'

