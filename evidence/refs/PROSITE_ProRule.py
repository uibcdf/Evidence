class PROSITE_ProRule():

    def __init__(self, id=None):

        self.database = 'PROSITE_ProRule'
        self.id = id
        self._long_name = 'ProRule section of PROSITE'
        self._web = 'https://prosite.expasy.org/prorule.html'

    def __call__(self):

        tmp_dict = {
                'database' : 'PROSITE_ProRule',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<PROSITE-ProRule: {self.id}>'

    def __str__(self):

        return f'PROSITE-ProRule: {self.id}'

    def __deepcopy__(self):

        return PROSITE_ProRule(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="https://prosite.expasy.org/rule/{self.id}">{self.database}: {self.id}</a>'

