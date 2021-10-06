class Pfam():

    def __init__(self, id=None):

        self.database = 'Pfam'
        self.id = id
        self._long_name = 'Pfam: The protein families database'
        self._web = 'http://pfam.xfam.org/'

    def __call__(self):

        tmp_dict = {
                'database' : 'Pfam',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<Pfam: {self.id}>'

    def __str__(self):

        return f'Pfam: {self.id}'

    def __deepcopy__(self):

        return Pfam(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="{self._webid()}">{self.database}: {self.id}</a>'

