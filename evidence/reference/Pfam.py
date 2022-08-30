from .database import DataBase

keyname = 'Pfam'
alternative_keynames = []

class Pfam(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'Pfam'
        self.id = id
        self.web = 'http://pfam.xfam.org/'
        self.webid = 'http://pfam.xfam.org/'
        self.info = 'Pfam: The protein families database'

