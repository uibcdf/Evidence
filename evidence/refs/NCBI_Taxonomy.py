class NCBI_Taxonomy():

    def __init__(self, name=None, id=None):

        self.id = id

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

