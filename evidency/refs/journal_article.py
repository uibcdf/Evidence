class JournalArticle():

    def __init__(self, title=None, authors=None, journal=None, volume=None, first_page=None,
            last_page=None, year=None, doi=None, pubmed=None):

        self.title = title
        self.authors = authors
        self.journal = journal
        self.volume = volume
        self.first_page = first_page
        self.last_page = last_page
        self.year = year
        self.doi = doi
        self.pubmed = pubmed

    def __call__(self):

        tmp_dict = {
                'title' : self.title,
                'authors' : self.authors,
                'journal' : self.journal,
                'volume' : self.volume,
                'first_page' : self.first_page,
                'last_page' : self.last_page,
                'year' : self.year,
                'doi' : self.doi,
                'pubmed' : self.pubmed,

                }

        return tmp_dict
