from .database import DataBase

name = 'iPTMnet'

class iPTMnet(DataBase):

    def __init__(self, id=None):

        self.database = 'iPTMnet'
        self.id = id
        self.web = 'https://research.bioinformatics.udel.edu/iptmnet/'
        self.webid = 'https://research.bioinformatics.udel.edu/iptmnet/'
        self.info = ''

