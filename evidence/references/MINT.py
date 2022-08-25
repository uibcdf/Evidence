class MINT():

    def __init__(self, id=None):

        self.database = 'MINT'
        self.id = id
        self._long_name = 'MINT, the Molecular INTeraction database'
        self._web = 'https://mint.bio.uniroma2.it/'

    def __call__(self):

        tmp_dict = {
                'database' : 'MINT',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<MINT: {self.id}>'

    def __str__(self):

        return f'MINT: {self.id}'

    def __deepcopy__(self):

        return MINT(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="{self._webid()}">{self.database}: {self.id}</a>'

