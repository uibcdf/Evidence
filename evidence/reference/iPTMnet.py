from .database import DataBase

name = 'iPTMnet'

class iPTMnet(DataBase):

    def __init__(self, id=None):

        self.name = 'iPTMnet'
        self.id = id
        self.long_name = 'iPTMnet'
        self.web = 'https://research.bioinformatics.udel.edu/iptmnet/'
        self.webid = 'https://research.bioinformatics.udel.edu/iptmnet/'
        self.info = ''

