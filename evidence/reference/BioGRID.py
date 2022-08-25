from .database import DataBase

name = 'BioGrid'

class BioGRID(DataBase):

    def __init__(self, id=None):

        self.name = 'BioGrid'
        self.id = id
        self.long_name = 'BioGrid'
        self.web = 'https://thebiogrid.org'
        self.webid = 'https://thebiogrid.org'
        self.info = ''
