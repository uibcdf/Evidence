from .database import DataBase

name = 'SUPERFAMILY'

class SUPERFAMILY(DataBase):

    def __init__(self, id=None):

        self.database = 'SUPERFAMILY'
        self.id = id
        self.web = 'https://supfam.org/'
        self.webid = 'https://supfam.org/'
        self.info = 'SUPERFAMILY 2'

