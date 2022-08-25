from .database import DataBase

name = 'InterPro'

class InterPro(DataBase):

    def __init__(self, id=None):

        self.name = 'InterPro'
        self.id = id
        self.long_name = 'InterPro'
        self.web = 'https://www.ebi.ac.uk/interpro/'
        self.webid = 'https://www.ebi.ac.uk/interpro/'
        self.info = ''

