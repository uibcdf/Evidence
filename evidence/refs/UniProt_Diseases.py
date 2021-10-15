class UniProt_Diseases():

    def __init__(self, id=None):

        self.database = 'UniProt_Diseases'
        self.id = id
        self._long_name = 'UniProt Human diseases'
        self._web = 'https://www.uniprot.org/diseases/'

    def __call__(self):

        tmp_dict = {
                'database' : 'UniProt_Diseases',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<UniProt_Diseases: {self.id}>'

    def __str__(self):

        return f'UniProt_Diseases: {self.id}'

    def __deepcopy__(self):

        return UniProt_Diseases(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="https://www.uniprot.org/diseases/{self.id}">{self.database}: {self.id}</a>'

