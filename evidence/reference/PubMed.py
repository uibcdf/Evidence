from .database import DataBase

keyname = 'PubMed'
alternative_keynames = []

class PubMed(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'PubMed'
        self.id = id
        self.web = 'https://pubmed.ncbi.nlm.nih.gov/'
        self.webid = 'https://pubmed.ncbi.nlm.nih.gov/{self.id}'
        self.info = ''
