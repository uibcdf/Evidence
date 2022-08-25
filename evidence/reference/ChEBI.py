from .database import DataBase

name = 'ChEBI'

class ChEBI(DataBase):

    def __init__(self, id=None):

        self.name = 'ChEBI'
        self.id = id
        self.long_name = 'ChEBI'
        self.web = 'https://www.ebi.ac.uk/chebi/'
        self.webid = 'https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:{self.id}'
        self.info = 'Chemical Entities of Biological Interest (ChEBI) is a freely available dictionary of molecular entities focused on ‘small’ chemical compounds.'

