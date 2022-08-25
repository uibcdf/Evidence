from .reference import Reference

class BindingDB():

    def __init__(self, id=None):

        database = 'BindingDB'
        long_name = 'BindingDB'
        web = 'https://www.bindingdb.org'
        webid = 'https://www.bindingdb.org'

        super().__init__(database=database, id=id, long_name=long_name, web=web, webid=webid)


