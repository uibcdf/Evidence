from .database import DataBase

name = 'Uniprot Diseases'

class UniProt_Diseases(DataBase):

    def __init__(self, id=None):

        self.name = 'UniProt Diseases'
        self.id = id
        self.long_name = 'UniProt Human diseases'
        self.web = 'https://www.uniprot.org/diseases/'
        self.webid = 'https://www.uniprot.org/diseases/{self.id}'
        self.info = ''

