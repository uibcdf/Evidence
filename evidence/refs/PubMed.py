class PubMed():

    def __init__(self, id=None):

        self.database = 'PubMed'
        self.id = id
        self._long_name = 'PubMed'
        self._web = 'https://pubmed.ncbi.nlm.nih.gov/'

    def __call__(self):

        tmp_dict = {
                'database' : 'PubMed',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<PubMed: {self.id}>'

    def __str__(self):

        return f'PubMed: {self.id}'

    def __deepcopy__(self):

        return PubMed(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="{self._webid()}">{self.database}: {self.id}</a>'

