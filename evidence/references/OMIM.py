class OMIM():

    def __init__(self, id=None):

        self.database = 'OMIM'
        self.id = id
        self._long_name = 'Online Mendelian Inheritance in Man (OMIM)'
        self._web = 'https://www.omim.org/'

    def __call__(self):

        tmp_dict = {
                'database' : 'OMIM',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<OMIM: {self.id}>'

    def __str__(self):

        return f'OMIM: {self.id}'

    def __deepcopy__(self):

        return OMIM(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="https://www.omim.org/entry/{self.id}">{self.database}: {self.id}</a>'

