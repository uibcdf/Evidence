from .database import DataBase

name = 'SUPERFAMILY'

class SUPERFAMILY(DataBase):

    def __init__(self, id=None):

        self.name = 'SUPERFAMILY'
        self.id = id
        self.long_name = 'SUPERFAMILY 2'
        self.web = 'https://supfam.org/'
        self.webid = 'https://supfam.org/'
        self.info = ''

