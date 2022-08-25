def ECO():

    def __init__(self, number):

        self.number = number

    def __call__(self):

        tmp_dict = {
                'number' : self.number,
                }

        return tmp_dict

    def __repr__(self):

        return f'<ECO:{self.number}>'

    def __str__(self):

        return f'ECO:{self.number}'

    def __deepcopy__(self):

        return self.__class__(number=self.number)

    def _repr_html_(self):

        return f'<a href="https://evidenceontology.org/browse/#ECO_{self.number}">ECO:{self.number}</a>'

