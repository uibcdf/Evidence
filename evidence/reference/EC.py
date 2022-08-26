from .database import DataBase

name = 'EC'

class EC(DataBase):

    def __init__(self, id=None):

        self.database = 'EC'
        self.id = id
        self.web = 'https://iubmb.qmul.ac.uk/enzyme/'
        self.webid = 'https://enzyme.expasy.org/EC/{self.id}'
        self.info = 'Enzyme Commission number of the Nomenclature Committee of the International Union of Biochemistry and Molecular Biology (IUBMB) Database of Interacting Proteins'

