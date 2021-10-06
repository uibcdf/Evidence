class iPTMnet():

    def __init__(self, id=None):

        self.database = 'iPTMnet'
        self.id = id
        self._long_name = 'iPTMnet'
        self._web = 'https://research.bioinformatics.udel.edu/iptmnet/'

    def __call__(self):

        tmp_dict = {
                'database' : 'iPTMnet',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<iPTMnet: {self.id}>'

    def __str__(self):

        return f'iPTMnet: {self.id}'

    def __deepcopy__(self):

        return iPTMnet(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="{self._webid()}">{self.database}: {self.id}</a>'

