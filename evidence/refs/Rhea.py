class Rhea():

    def __init__(self, id=None):

        self.database = 'Rhea'
        self.id = id
        self._name = 'Rhea'
        self._info = 'Rhea is an expert-curated knowledgebase of chemical and transport reactions of biological interest - and the standard for enzyme and transporter annotation in UniProtKB.'
        self._web = 'https://www.rhea-db.org/'

    def __call__(self):

        tmp_dict = {
                'database' : 'Rhea',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<Rhea: {self.id}>'

    def __str__(self):

        return f'Rhea: {self.id}'

    def __deepcopy__(self):

        return Rhea(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="https://www.rhea-db.org/rhea/{self.id}">{self.database}: {self.id}</a>'

