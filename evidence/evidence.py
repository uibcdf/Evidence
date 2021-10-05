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

    def add_BindingDB(self, id=None):

        tmp_ref = refs.BindingDB(id=id)
        self.references.append(tmp_ref)

        pass

    def add_BioGRID(self, id=None):

        tmp_ref = refs.BioGRID(id=id)
        self.references.append(tmp_ref)

        pass

    def add_ChEMBL(self, id=None):

        tmp_ref = refs.ChEMBL(id=id)
        self.references.append(tmp_ref)

        pass

    def add_DIP(self, id=None):

        tmp_ref = refs.DIP(id=id)
        self.references.append(tmp_ref)

        pass

    def add_ELM(self, id=None):

        tmp_ref = refs.ELM(id=id)
        self.references.append(tmp_ref)

        pass

    def add_IntAct(self, id=None):

        tmp_ref = refs.IntAct(id=id)
        self.references.append(tmp_ref)

        pass

    def add_InterPro(self, id=None):

        tmp_ref = refs.InterPro(id=id)
        self.references.append(tmp_ref)

        pass

    def add_iPTMnet(self, id=None):

        tmp_ref = refs.iPTMnet(id=id)
        self.references.append(tmp_ref)

        pass

    def add_iPTMnet(self, id=None):

        tmp_ref = refs.iPTMnet(id=id)
        self.references.append(tmp_ref)

        pass

    def add_JournalArticle(self, title=None, authors=None, journal=None, volume=None,
            first_page=None, last_page=None, year=None, DOI=None, PubMed=None):

        tmp_ref = refs.JournalArticle(title=None, authors=None, journal=None, volume=None,
            first_page=None, last_page=None, year=None, DOI=None, PubMed=None)

        self.references.append(tmp_ref)

        pass

    def add_MINT(self, id=None):

        tmp_ref = refs.MINT(id=id)
        self.references.append(tmp_ref)

        pass

    def add_NCBI_Taxonomy(self, id=None):

        tmp_ref = refs.NCBI_Taxonomy(id=id)
        self.references.append(tmp_ref)

        pass

    def add_PDB(self, id=None):

        tmp_ref = refs.PDB(id=id)
        self.references.append(tmp_ref)

        pass

    def add_Pfam(self, id=None):

        tmp_ref = refs.Pfam(id=id)
        self.references.append(tmp_ref)

        pass

    def add_PhosphoSitePlus(self, id=None):

        tmp_ref = refs.PhosphoSitePlus(id=id)
        self.references.append(tmp_ref)

        pass

    def add_ProDom(self, id=None):

        tmp_ref = refs.ProDom(id=id)
        self.references.append(tmp_ref)

        pass

    def add_ProteinModelPortal(self, id=None):

        tmp_ref = refs.ProteinModelPortal(id=id)
        self.references.append(tmp_ref)

        pass

    def add_PubMed(self, id=None):

        tmp_ref = refs.PubMed(id=id)
        self.references.append(tmp_ref)

        pass

    def add_STRING(self, id=None):

        tmp_ref = refs.STRING(id=id)
        self.references.append(tmp_ref)

        pass

    def add_SUPFAM(self, id=None):

        tmp_ref = refs.SUPFAM(id=id)
        self.references.append(tmp_ref)

        pass

    def add_Swiss_Model(self, id=None):

        tmp_ref = refs.Swiss_Model(id=id)
        self.references.append(tmp_ref)

        pass

    def add_UniProtKB(self, id=None):

        tmp_ref = refs.UniProtKB(id=id)
        self.references.append(tmp_ref)

        pass

