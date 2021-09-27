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

    def __repr__(self):

        return f"{self.value} <{len(self.references)} refs.>"

    def __str__(self):

        return str(self.value)

    def add_JournalArticle(self, title=None, authors=None, journal=None, volume=None,
            first_page=None, last_page=None, year=None, DOI=None, PubMed=None):

        tmp_ref = refs.JournalArticle(title=None, authors=None, journal=None, volume=None,
            first_page=None, last_page=None, year=None, DOI=None, PubMed=None)

        self.references.append(tmp_ref)

        pass

    def add_DOI(self, id=None):

        tmp_ref = refs.DOI(id=id)
        self.references.append(tmp_ref)

        pass

    def add_PubMed(self, id=None):

        tmp_ref = refs.PubMed(id=id)
        self.references.append(tmp_ref)

        pass

    def add_UniProtKB(self, id=None):

        tmp_ref = refs.UniProtKB(id=id)
        self.references.append(tmp_ref)

        pass

