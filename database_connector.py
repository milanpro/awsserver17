from sqlalchemy import create_engine

class database_connector:
    """Database connector to AWS Database"""
    def __init__(self):
        self.engine = create_engine('mysql+mysqlconnector://iamuser1:hackhpi2017@hackhpivis-cluster.cluster-csrsiurc1mom.eu-central-1.rds.amazonaws.com:3306/hackhpivis', echo=False)
        self.cnx = con.connect(user='iamuser1', password='hackhpi2017', host='hackhpivis-cluster.cluster-csrsiurc1mom.eu-central-1.rds.amazonaws.com', port='3306', database = 'hackhpivis')
        self.cursor = self.cnx.cursor()

    def cnx(self):
        return self.cnx

    def engine(self):
        return self.engine

    def cursor(self):
        return  self.cursor

    def query(self, query):
        self.cursor.execute(query)