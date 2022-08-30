from .database import DataBase

keyname = 'SMR'
alternative_keynames = ['SwissModel']

class SMR(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'SwissModel'
        self.id = id
        self.web = 'https://swissmodel.expasy.org/repository/'
        self.webid = 'https://swissmodel.expasy.org/repository/uniprot/{self.id}'
        self.info = 'Swiss-Model Repository'

