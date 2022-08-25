from .database import DataBase

name = 'ELM'

class ELM(DataBase):

    def __init__(self, id=None):

        self.name = 'ELM'
        self.id = id
        self.long_name = 'The Eukaryotic Linear Motif resource for Functional Sites in Proteins'
        self.web = 'http://elm.eu.org/'
        self.webid = 'http://elm.eu.org/'
        self.info = 'The Eukaryotic Linear Motif resource for Functional Sites in Proteins'

