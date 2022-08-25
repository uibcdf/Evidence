from .database import DataBase

name = 'PubMed'

class PubMed(DataBase):

    def __init__(self, id=None):

        self.name = 'PubMed'
        self.id = id
        self.long_name = 'PubMed'
        self.web = 'https://pubmed.ncbi.nlm.nih.gov/'
        self.webid = 'https://pubmed.ncbi.nlm.nih.gov/{self.id}'
        self.info = ''
