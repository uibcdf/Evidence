from .database import DataBase

name = 'DIP'

class DIP(DataBase):

    def __init__(self, id=None):

        self.name = 'DIP'
        self.id = id
        self.long_name = 'Database of Interacting Proteins'
        self.web = 'http://dip.doe-mbi.ucla.edu'
        self.webid = 'http://dip.doe-mbi.ucla.edu'
        self.info = 'Database of Interacting Proteins'

