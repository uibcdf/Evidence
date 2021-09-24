class DOI():

    def __init__(self, id=None):

        self.id = id

    def __call__(self):

        tmp_dict = {
                'database' : 'DOI',
                'id' : self
                }

        return tmp_dict

