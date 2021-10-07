class UniProtKB():

    def __init__(self, id=None):

        self.database = 'UniProtKB'
        self.id = id
        self._long_name = 'UniProtKB'
        self._web = 'https://www.uniprot.org/'

    def __call__(self):

        tmp_dict = {
                'database' : 'UniProtKB',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<UniProtKB: {self.id}>'

    def __str__(self):

        return f'UniProtKB: {self.id}'

    def __deepcopy__(self):

        return UniProtKB(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="https://www.uniprot.org/uniprot/{self.id}">{self.database}: {self.id}</a>'

