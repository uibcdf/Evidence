class ELM():

    def __init__(self, id=None):

        self.database = 'ELM'
        self.id = id
        self._long_name = 'The Eukaryotic Linear Motif resource for Functional Sites in Proteins'
        self._web = 'http://elm.eu.org/'

    def __call__(self):

        tmp_dict = {
                'database' : 'ELM',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<ELM: {self.id}>'

    def __str__(self):

        return f'ELM: {self.id}'

    def __deepcopy__(self):

        return ELM(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="{self._webid()}">{self.database}: {self.id}</a>'

