from .database import DataBase

name = 'UniProtKB'

class UniProtKB(DataBase):

    def __init__(self, id=None):

        self.database = 'UniProtKB'
        self.id = id
        self.web = 'https://www.uniprot.org/'
        self.webid = 'https://www.uniprot.org/uniprot/{self.id}'
        self.info = 'UniProtKB'

