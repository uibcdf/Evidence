from .database import DataBase

name = 'IntAct'

class IntAct(DataBase):

    def __init__(self, id=None):

        self.name = 'IntAct'
        self.id = id
        self.long_name = 'IntAct Molecular Interaction Database'
        self.web = 'https://www.ebi.ac.uk/intact/home'
        self.webid = 'https://www.ebi.ac.uk/intact/home'
        self.info = ''

