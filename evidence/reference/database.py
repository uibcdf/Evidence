class DataBase():

    def __init__(self, database=None, id=None, web=None, webid=None, info=None):

        self.database = database
        self.id = id
        self.web = web
        self.webid = webid
        self.info = info

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

        return self.__class__(database=self.database, id=self.id, web=self.web, webid=self.webid, info=self.info)

    def _repr_html_(self):

        return f'<a href="{self.webid}">{self.database}: {self.id}</a>'

