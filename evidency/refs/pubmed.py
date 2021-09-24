class PubMed():

    def __init__(self, id=None):

        self.id = id

    def __call__(self):

        tmp_dict = {
                'database' : 'PubMed',
                'id' : self.id
                }

        return tmp_dict

