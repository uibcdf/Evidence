from ._private import digest_reference, digest_eco

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
        for eco in self.ecos:
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

    def has_reference(self, reference):

        output = False

        reference = digest_reference(reference)

        dict_reference = reference()

        for aux in self.references:
            if aux()==dict_reference:
                output=True
                break

        return output

    def add_reference(self, reference):

        reference = digest_reference(reference)

        if not self.has_reference(reference):
            self.references.append(reference)

    def has_eco(self, eco):

        output = False

        eco = digest_eco(eco)

        dict_eco = eco()

        for aux in self.ecos:
            if aux()==dict_eco:
                output=True
                break

        return output


    def add_eco(self, eco):

        eco = digest_eco(eco)

        if not self.has_eco(eco):
            self.ecos.append(eco)


    def __deepcopy__(self):

        aux = Evidence()
        aux.value = self.value
        for ref in self.reference:
            aux.reference.append(ref.__deepcopy__())
        for eco in self.ecos:
            aux.ecos.append(eco.__deepcopy__())

        return aux

