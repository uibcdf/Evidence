from .database import DataBase

keyname = 'NCBI Taxonomy'
alternative_keynames = ['NCBI_Taxonomy']

class NCBITaxonomy(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'NCBI Taxonomy'
        self.id = id
        self.web = 'https://www.ncbi.nlm.nih.gov/Taxonomy'
        self.webid = 'https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id={self.id}'
        self.info = 'The NCBI Taxonomy Database'

