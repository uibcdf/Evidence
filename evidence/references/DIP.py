class DIP():

    def __init__(self, id=None):

        self.database = 'DIP'
        self.id = id
        self._long_name = 'Database of Interacting Proteins'
        self._web = 'http://dip.doe-mbi.ucla.edu'

    def __call__(self):

        tmp_dict = {
                'database' : 'DIP',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<DIP: {self.id}>'

    def __str__(self):

        return f'DIP: {self.id}'

    def __deepcopy__(self):

        return DIP(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="{self._webid()}">{self.database}: {self.id}</a>'

