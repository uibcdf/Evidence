from .database import DataBase

name = 'NCBI Taxonomy'

class NCBI_Taxonomy(DataBase):

    def __init__(self, id=None):

        self.name = 'NCBI Taxonomy'
        self.id = id
        self.long_name = 'The NCBI Taxonomy Database'
        self.web = 'https://www.ncbi.nlm.nih.gov/Taxonomy'
        self.webid = 'https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id={self.id}'
        self.info = ''

