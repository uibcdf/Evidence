from . import reference as refs

class Evidence():

    def __init__(self, value=None, references=None, ecos=None):

        self.value = value
        self.references = []
        self.ecos = []

    def __call__(self, references=False):

        if references==False:
            return self.value
        else:
            return [ii() for ii in self.references]

    def __bytes__(self):

        return __call__(self)

    def __len__(self):

        return len(self.value)

    def __repr__(self):

        if len(self.ecos):
            return f"{self.value} <{len(self.references)} refs.; {len(self.ecos)} ECOs>"
        else:
            return f"{self.value} <{len(self.references)} refs.>"

    def _repr_html_(self):

        output = f"{self.value}"

        output_refs = []
        for ref in self.references:
            output_refs.append(ref._repr_html_())

        output_ecos = []
        for eco in self.eco:
            output_ecos.append(eco._repr_html_())

        if len(output_refs):
            output += ' <'+', '.join(output_refs)
            if len(output_ecos):
                output += ' | ECOs'+', '.join(output_ecos)
            output +='>'

        return output

    def __str__(self):

        output = f"{self.value}"

        output_refs = []
        for ref in self.references:
            output_refs.append(ref.__str__())

        output_ecos = []
        for eco in self.eco:
            output_ecos.append(eco._str_())

        if len(output_refs):
            output += ' <'+', '.join(output_refs)
            if len(output_ecos):
                output += ' | ECOs'+', '.join(output_ecos)
            output +='>'

        return output

    def add_reference(self, reference):

        if is_reference(reference):
 
            if type(reference) is not dict:
 
                reference = reference.__deepcopy__()
 
            else:
 
                if 'database' in reference:

                    database = reference.pop('database')
                    reference = refs.dict_ref[database](**reference)
 
                elif ('authors' in reference) and ('journal' in reference):

                    reference = refs.dict_ref['JournalArticle'](**reference)
 
                else:

                    raise ValueError('The input argument is not valid as reference')
 
        else:

            raise ValueError('The input argument is not valid as reference')

        return output

        dict_reference = reference()

        new=True
        for aux in self.references:
            if aux()==dict_reference:
                new=False
                break

        if new:
            self.references.append(reference)

        pass

    def add_eco(self, eco):

        if is_eco(eco):

            if not isinstance(eco, str):



    def __deepcopy__(self):

        aux = Evidence()
        aux.value = self.value
        for ref in self.reference:
            aux.reference.append(ref.__deepcopy__())
        for eco in self.ecos:
            aux.ecos.append(eco.__deepcopy__())

        return aux

