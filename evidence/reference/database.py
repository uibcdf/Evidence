class DataBase():

    def __init__(self, name=None, id=None, long_name=None, web=None, webid=None, info=None):

        self.name = name
        self.id = id
        self.long_name = long_name
        self.web = web
        self.webid = webid
        self.info = info

    def __call__(self):

        tmp_dict = {
                'name' : self.name,
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<{self.name}: {self.id}>'

    def __str__(self):

        return f'{self.name}: {self.id}'

    def __deepcopy__(self):

        return self.__class__(name=self.name, id=self.id, long_name=self.long_name, web=self.web, webid=self.webid)

    def _repr_html_(self):

        return f'<a href="{self.webid}">{self.name}: {self.id}</a>'

