class STRING():

    def __init__(self, id=None):

        self.database = 'STRING'
        self.id = id
        self._long_name = ''
        self._web = 'https://string-db.org/'

    def __call__(self):

        tmp_dict = {
                'database' : 'STRING',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<STRING: {self.id}>'

    def __str__(self):

        return f'STRING: {self.id}'

    def __deepcopy__(self):

        return STRING(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="{self._webid()}">{self.database}: {self.id}</a>'

