class ProDom():

    def __init__(self, id=None):

        self.database = 'ProDom'
        self.id = id
        self._long_name = 'ProDom'
        self._web = 'http://prodom.prabi.fr/prodom/current/html/home.php'

    def __call__(self):

        tmp_dict = {
                'database' : 'ProDom',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<ProDom: {self.id}>'

    def __str__(self):

        return f'ProDom: {self.id}'

    def __deepcopy__(self):

        return ProDom(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="{self._webid()}">{self.database}: {self.id}</a>'

