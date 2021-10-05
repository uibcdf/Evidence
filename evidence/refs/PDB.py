class PDB():

    def __init__(self, id=None):

        self.id = id

    def __call__(self):

        tmp_dict = {
                'database' : 'PDB',
                'id' : self
                }

        return tmp_dict

    def __repr__(self):

        return f'<PDB: {self.id}>'

    def __str__(self):

        return f'PDB: {self.id}'
