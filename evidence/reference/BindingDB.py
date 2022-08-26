from .database import DataBase

keyname = 'BindingDB'
alternative_keynames = []

class BindingDB(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'BindingDB'
        self.id = None
        self.web = 'https://www.bindingdb.org'
        self.webid = 'https://www.bindingdb.org'
        self.info = ''

