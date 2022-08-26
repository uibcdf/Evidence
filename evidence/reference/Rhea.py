from .database import DataBase

keyname = 'Rhea'
alternative_keynames = []

class Rhea(DataBase):

    def __init__(self, id=None):

        self.database = keyname
        self.name = 'Rhea'
        self.id = id
        self.web = 'https://www.rhea-db.org/'
        self.webid = 'https://www.rhea-db.org/rhea/{self.id}'
        self.info = 'Rhea is an expert-curated knowledgebase of chemical and transport reactions of biological interest - and the standard for enzyme and transporter annotation in UniProtKB.'
