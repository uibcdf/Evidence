from .database import DataBase

keyname = 'DIP'
alternative_keynames = []

class DIP(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'DIP'
        self.id = id
        self.web = 'http://dip.doe-mbi.ucla.edu'
        self.webid = 'http://dip.doe-mbi.ucla.edu'
        self.info = 'Database of Interacting Proteins'

