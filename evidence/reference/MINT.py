from .database import DataBase

keyname = 'MINT'
alternative_keynames = []

class MINT(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'MINT'
        self.id = id
        self.web = 'https://mint.bio.uniroma2.it/'
        self.webid = 'https://mint.bio.uniroma2.it/'
        self.info = 'The Molecular INTeraction database'

