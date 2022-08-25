class NCBI_Taxonomy():

    def __init__(self, id=None):

        self.database = 'NCBI_Taxonomy'
        self.id = id
        self._long_name = 'The NCBI Taxonomy Database'
        self._web = 'https://www.ncbi.nlm.nih.gov/Taxonomy'

    def __call__(self):

        tmp_dict = {
                'database' : 'NCBI_Taxonomy',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<NCBI_Taxonomy: {self.id}>'

    def __str__(self):

        return f'NCBI_Taxonomy: {self.id}'

    def __deepcopy__(self):

        return NCBI_Taxonomy(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id={self.id}">{self.database}: {self.id}</a>'

