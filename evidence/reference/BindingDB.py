from .database import DataBase

names = 'BindingDB'

class BindingDB(DataBase):

    def __init__(self, id=None):

        self.database = 'BindingDB'
        self.id = None
        self.web = 'https://www.bindingdb.org'
        self.webid = 'https://www.bindingdb.org'
        self.info = ''

