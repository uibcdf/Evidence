from .database import DataBase

name = 'BindingDB'

class BindingDB(DataBase):

    def __init__(self, id=None):

        self.name = 'BindingDB'
        self.id = None
        self.long_name = 'BindingDB'
        self.web = 'https://www.bindingdb.org'
        self.webid = 'https://www.bindingdb.org'
        self.info = ''

