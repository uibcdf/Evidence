class DOI():

    def __init__(self, id=None):

        self.database = 'DOI'
        self.id = id
        self._long_name = 'Digital Object Indentifier System'
        self._web = 'https://www.doi.org/'

    def __call__(self):

        tmp_dict = {
                'database' : 'DOI',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<DOI: {self.id}>'

    def __str__(self):

        return f'DOI: {self.id}'

    def __deepcopy__(self):

        return DOI(id=self.id)

    def _repr_html_(self):

        return f'<a href="{self._webid()}">DOI: {self.id}</a>'

    def _webid(self):

        return 'https://www.doi.org/'

