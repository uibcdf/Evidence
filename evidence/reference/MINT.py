from .database import DataBase

name = 'MINT'

class MINT(DataBase):

    def __init__(self, id=None):

        self.name = 'MINT'
        self.id = id
        self.long_name = 'MINT, the Molecular INTeraction database'
        self.web = 'https://mint.bio.uniroma2.it/'
        self.webid = 'https://mint.bio.uniroma2.it/'
        self.info = ''

