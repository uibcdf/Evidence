
keyname = 'web'
alternative_keynames = ['Web', 'www']

class Web():

    def __init__(self, web=None, name=None):

        self.web = web
        self.name = name

    def __call__(self):

        tmp_dict = {
                'web' : self.web,
                'name' : self.name,
                }

        return tmp_dict

    def __repr__(self):

        return f'<Web: {self.name}, {self.web}>'

    def __str__(self):

        return f'{self.name}, {self.web}'

    def __deepcopy__(self):

        return Web(web=self.web, name=self.name)

