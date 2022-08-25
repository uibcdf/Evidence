class MobiDB():

    def __init__(self, id=None):

        self.database = 'MobiDB'
        self.id = id
        self._long_name = 'MobiDB, a database of protein disorder and mobility annotations.'
        self._web = 'https://mobidb.bio.unipd.it/'

    def __call__(self):

        tmp_dict = {
                'database' : 'MobiDB',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<MobiDB: {self.id}>'

    def __str__(self):

        return f'MobiDB: {self.id}'

    def __deepcopy__(self):

        return MobiDB(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="https://mobidb.bio.unipd.it/{self.id}">{self.database}: {self.id}</a>'

