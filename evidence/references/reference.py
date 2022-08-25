class Reference():

    def __init__(self, database=None, id=None, long_name=None, web=None, webid=None):

        self.database = database
        self.id = id
        self.long_name = long_name
        self.web = web
        self.webid = webid

    def __call__(self):

        tmp_dict = {
                'database' : self.database,
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<{self.database}: {self.id}>'

    def __str__(self):

        return f'{self.database}: {self.id}'

    def __deepcopy__(self):

        return self.__class__(database=self.database, id=self.id, long_name=self.long_name, web=self.web, webid=self.webid)

    def _repr_html_(self):

        return f'<a href="{self.webid}">{self.database}: {self.id}</a>'

