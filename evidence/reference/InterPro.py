from .database import DataBase

keyname = 'InterPro'
alternative_keynames = []

class InterPro(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'InterPro'
        self.id = id
        self.web = 'https://www.ebi.ac.uk/interpro/'
        self.webid = 'https://www.ebi.ac.uk/interpro/'
        self.info = ''

