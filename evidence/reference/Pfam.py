from .database import DataBase

name = 'Pfam'

class Pfam(DataBase):

    def __init__(self, id=None):

        self.database = 'Pfam'
        self.id = id
        self.web = 'http://pfam.xfam.org/'
        self.webid = 'http://pfam.xfam.org/'
        self.info = 'Pfam: The protein families database'

