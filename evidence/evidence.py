from . import refs

class Evidence():

    def __init__(self, value=None):

        self.value = value
        self.references = []

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

        return f"{self.value} <{len(self.references)} refs.>"

    def _repr_html_(self):

        output = f"{self.value}"

        output_refs = []
        for ref in self.references:
            output_refs.append(ref._repr_html_())

        if len(output_refs):
            output += ' <'+', '.join(output_refs)+'>'

        return output

    def __str__(self):

        output = f"{self.value}"

        output_refs = []
        for ref in self.references:
            output_refs.append(ref.__str__())

        if len(output_refs):
            output += ' <'+', '.join(output_refs)+'>'

        return output

    def add_reference(self, reference):

        from .tools import reference as _reference

        reference = _reference(reference)
        dict_reference = reference()

        new=True
        for aux in self.references:
            if aux()==dict_reference:
                new=False
                break

        if new:
            self.references.append(reference)

        pass

    def __deepcopy__(self):

        aux = Evidence()
        aux.value = self.value
        for ref in self.reference:
            aux.append(ref.__deepcopy__())

        return aux

