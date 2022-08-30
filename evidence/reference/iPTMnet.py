from .database import DataBase

keyname = 'iPTMnet'
alternative_keynames = []

class iPTMnet(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'iPTMnet'
        self.id = id
        self.web = 'https://research.bioinformatics.udel.edu/iptmnet/'
        self.webid = 'https://research.bioinformatics.udel.edu/iptmnet/'
        self.info = ''

