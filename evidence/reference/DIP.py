from .database import DataBase

name = 'DIP'

class DIP(DataBase):

    def __init__(self, id=None):

        self.database = 'DIP'
        self.id = id
        self.web = 'http://dip.doe-mbi.ucla.edu'
        self.webid = 'http://dip.doe-mbi.ucla.edu'
        self.info = 'Database of Interacting Proteins'

