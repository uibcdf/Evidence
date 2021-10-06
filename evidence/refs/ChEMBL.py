class ChEMBL():

    def __init__(self, id=None):

        self.database = 'ChEMBL'
        self.id = id
        self._long_name = 'ChEMBL'
        self._web = 'https://www.ebi.ac.uk/chembl/'

    def __call__(self):

        tmp_dict = {
                'database' : 'ChEMBL',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<ChEMBL: {self.id}>'

    def __str__(self):

        return f'ChEMBL: {self.id}'

    def __deepcopy__(self):

        return ChEMBL(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="{self._webid()}">{self.database}: {self.id}</a>'

