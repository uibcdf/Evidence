from .database import DataBase

name = 'ELM'

class ELM(DataBase):

    def __init__(self, id=None):

        self.database = 'ELM'
        self.id = id
        self.web = 'http://elm.eu.org/'
        self.webid = 'http://elm.eu.org/'
        self.info = 'The Eukaryotic Linear Motif resource for Functional Sites in Proteins'

