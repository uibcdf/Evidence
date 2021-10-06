class PhosphoSitePlus():

    def __init__(self, id=None):

        self.database = 'PhosphoSitePlus'
        self.id = id
        self._long_name = 'PhosphoSitePlus'
        self._web = 'https://www.phosphosite.org/homeAction.action'

    def __call__(self):

        tmp_dict = {
                'database' : 'PhosphoSitePlus',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<PhosphoSitePlus: {self.id}>'

    def __str__(self):

        return f'PhosphosSitePlus: {self.id}'

    def __deepcopy__(self):

        return PhosphoSitePlus(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="{self._webid()}">{self.database}: {self.id}</a>'

