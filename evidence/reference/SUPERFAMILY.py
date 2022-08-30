from .database import DataBase

keyname = 'SUPERFAMILY'
alternative_keynames = []

class SUPERFAMILY(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'SUPERFAMILY'
        self.id = id
        self.web = 'https://supfam.org/'
        self.webid = 'https://supfam.org/'
        self.info = 'SUPERFAMILY 2'

