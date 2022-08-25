class SUPERFAMILY():

    def __init__(self, id=None):

        self.database = 'SUPERFAMILY'
        self.id = id
        self._long_name = 'SUPERFAMILY 2'
        self._web = 'https://supfam.org/'

    def __call__(self):

        tmp_dict = {
                'database' : 'SUPERFAMILY',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<SUPERFAMILY: {self.id}>'

    def __str__(self):

        return f'SUPERFAMILY: {self.id}'

    def __deepcopy__(self):

        return SUPERFAMILY(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="{self._webid()}">{self.database}: {self.id}</a>'

