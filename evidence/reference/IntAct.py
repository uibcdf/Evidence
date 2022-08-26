from .database import DataBase

name = 'IntAct'

class IntAct(DataBase):

    def __init__(self, id=None):

        self.database = 'IntAct'
        self.id = id
        self.web = 'https://www.ebi.ac.uk/intact/home'
        self.webid = 'https://www.ebi.ac.uk/intact/home'
        self.info = 'IntAct Molecular Interaction Database'

