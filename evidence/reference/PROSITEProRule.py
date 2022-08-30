from .database import DataBase

keyname = 'PROSITE ProRule'
alternative_keynames = ['PROSITE_ProRule', 'PROSITE-ProRule']

class PROSITEProRule(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'PROSITE ProRule'
        self.id = id
        self.web = 'https://prosite.expasy.org/prorule.html'
        self.webid = 'https://prosite.expasy.org/rule/{self.id}'
        self.info = 'ProRule section of PROSITE'

