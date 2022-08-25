class EC():

    def __init__(self, id=None):

        self.database = 'EC'
        self.id = id
        self._long_name = 'EC (Enzyme Commission) number of the Nomenclature Committee of the International Union of Biochemistry and Molecular Biology (IUBMB) Database of Interacting Proteins'
        self._web = 'https://iubmb.qmul.ac.uk/enzyme/'

    def __call__(self):

        tmp_dict = {
                'database' : 'EC',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<EC: {self.id}>'

    def __str__(self):

        return f'EC: {self.id}'

    def __deepcopy__(self):

        return EC(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="https://enzyme.expasy.org/EC/{self.id}">{self.database}: {self.id}</a>'

