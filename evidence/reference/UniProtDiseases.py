from .database import DataBase

keyname = 'UniProt Diseases'
alternative_keynames = ['UniProt_Diseases']

class UniProtDiseases(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'UniProt Diseases'
        self.id = id
        self.web = 'https://www.uniprot.org/diseases/'
        self.webid = 'https://www.uniprot.org/diseases/{self.id}'
        self.info = 'UniProt Human diseases'

