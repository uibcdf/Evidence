from .database import DataBase

name = 'Uniprot Diseases'

class UniProt_Diseases(DataBase):

    def __init__(self, id=None):

        self.database = 'UniProt Diseases'
        self.id = id
        self.web = 'https://www.uniprot.org/diseases/'
        self.webid = 'https://www.uniprot.org/diseases/{self.id}'
        self.info = 'UniProt Human diseases'

