from .database import DataBase

name = 'PROSITE ProRule'

class PROSITE_ProRule(DataBase):

    def __init__(self, id=None):

        self.database = 'PROSITE ProRule'
        self.id = id
        self.web = 'https://prosite.expasy.org/prorule.html'
        self.webid = 'https://prosite.expasy.org/rule/{self.id}'
        self.info = 'ProRule section of PROSITE'

