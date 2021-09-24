class UniProtKB():

    def __init__(self, name=None, id=None):

        self.id = id

    def __call__(self):

        tmp_dict = {
                'database' : 'UniProtKB',
                'id' : self.id
                }

        return tmp_dict

