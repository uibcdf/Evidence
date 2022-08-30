from .database import DataBase

keyname = 'HGNC'
alternative_keynames = []

class HGNC(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'HGNC'
        self.id = id
        self.web = 'https://www.genenames.org'
        self.webid = 'https://www.genenames.org/data/gene-symbol-report/#!/{self.id}/%s'
        self.info = 'Human Gene Nomenclature Database'

