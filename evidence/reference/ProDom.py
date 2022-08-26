from .database import DataBase

name = 'ProDom'

class ProDom(DataBase):

    def __init__(self, id=None):

        self.database = 'ProDom'
        self.id = id
        self.web = 'http://prodom.prabi.fr/prodom/current/html/home.php'
        self.webid = 'http://prodom.prabi.fr/prodom/current/html/home.php'
        self.info = ''

