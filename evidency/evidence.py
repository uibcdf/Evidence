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

    def add_JournalArticle(title=None, authors=None, journal=None, volume=None,
            first_page=None, last_page=None, year=None, DOI=None, PubMed=None):

        tmp_ref = ref.JournalArticle(title=None, authors=None, journal=None, volume=None,
            first_page=None, last_page=None, year=None, DOI=None, PubMed=None)

        pass

    def add_DOI(name=None, id=None):

        tmp_ref = ref.DOI(name=name, id=id)
        self.references.append(tmp_ref)

        pass

    def add_PubMed(name=None, id=None):

        tmp_ref = ref.PubMed(name=name, id=id)
        self.references.append(tmp_ref)

        pass

    def add_UniProtKB(name=None, id=None):

        tmp_ref = ref.UniProtKB(name=name, id=id)
        self.references.append(tmp_ref)

        pass

