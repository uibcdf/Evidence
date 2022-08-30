from .database import DataBase

keyname = 'UniProtKB'
alternative_keynames = []

class UniProtKB(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'UniProtKB'
        self.id = id
        self.web = 'https://www.uniprot.org/'
        self.webid = 'https://www.uniprot.org/uniprot/{self.id}'
        self.info = 'UniProtKB'

