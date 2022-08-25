class PDB():

    def __init__(self, id=None):

        self.database = 'PDB'
        self.id = id
        self._long_name = 'Protein Data Bank'
        self._web = 'https://www.wwpdb.org/'

    def __call__(self):

        tmp_dict = {
                'database' : 'PDB',
                'id' : self
                }

        return tmp_dict

    def __repr__(self):

        return f'<PDB: {self.id}>'

    def __str__(self):

        return f'PDB: {self.id}'

    def __deepcopy__(self):

        return PDB(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="{self._webid()}">{self.database}: {self.id}</a>'

