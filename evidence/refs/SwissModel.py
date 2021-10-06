class SwissModel():

    def __init__(self, id=None):

        self.database = 'SwissModel'
        self.id = id
        self._long_name = 'Swiss-Model Repository'
        self._web = 'https://swissmodel.expasy.org/'

    def __call__(self):

        tmp_dict = {
                'database' : 'Swiss-Model',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<Swiss-Model: {self.id}>'

    def __str__(self):

        return f'Swiss-Model: {self.id}'

    def __deepcopy__(self):

        return SwissModel(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="{self._webid()}">{self.database}: {self.id}</a>'

