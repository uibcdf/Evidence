class ChEBI():

    def __init__(self, id=None):

        self.database = 'ChEBI'
        self.id = id
        self._name = 'ChEBI'
        self._info = 'Chemical Entities of Biological Interest (ChEBI) is a freely available dictionary of molecular entities focused on ‘small’ chemical compounds.'
        self._web = 'https://www.ebi.ac.uk/chebi/'

    def __call__(self):

        tmp_dict = {
                'database' : 'ChEBI',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<ChEBI: {self.id}>'

    def __str__(self):

        return f'ChEBI: {self.id}'

    def __deepcopy__(self):

        return ChEBI(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:{self.id}">{self.database}: {self.id}</a>'

