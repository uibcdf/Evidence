class UniProtKB():

    def __init__(self, name=None, id=None):

        self.id = id

    def __call__(self):

        tmp_dict = {
                'database' : 'UniProtKB',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<UniProtKB: {self.id}>'

    def __str__(self):

        return f'UniProtKB: {self.id}'
