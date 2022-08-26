from .database import DataBase

name = 'InterPro'

class InterPro(DataBase):

    def __init__(self, id=None):

        self.database = 'InterPro'
        self.id = id
        self.web = 'https://www.ebi.ac.uk/interpro/'
        self.webid = 'https://www.ebi.ac.uk/interpro/'
        self.info = ''

