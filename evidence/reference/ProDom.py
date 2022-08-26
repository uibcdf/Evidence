from .database import DataBase

keyname = 'ProDom'
alternative_keynames = []

class ProDom(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'ProDom'
        self.id = id
        self.web = 'http://prodom.prabi.fr/prodom/current/html/home.php'
        self.webid = 'http://prodom.prabi.fr/prodom/current/html/home.php'
        self.info = ''

