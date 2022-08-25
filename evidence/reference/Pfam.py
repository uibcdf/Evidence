from .database import DataBase

name = 'Pfam'

class Pfam(DataBase):

    def __init__(self, id=None):

        self.name = 'Pfam'
        self.id = id
        self.long_name = 'Pfam: The protein families database'
        self.web = 'http://pfam.xfam.org/'
        self.webid = 'http://pfam.xfam.org/'
        self.info = ''

