class InterPro():

    def __init__(self, id=None):

        self.database = 'InterPro'
        self.id = id
        self._long_name = 'InterPro'
        self._web = 'https://www.ebi.ac.uk/interpro/'

    def __call__(self):

        tmp_dict = {
                'database' : 'InterPro',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<InterPro: {self.id}>'

    def __str__(self):

        return f'InterPro: {self.id}'

    def __deepcopy__(self):

        return InterPro(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="{self._webid()}">{self.database}: {self.id}</a>'

