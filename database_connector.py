from sqlalchemy import create_engine

class database_connector:
    """Database connector to AWS Database"""
    def __init__(self):
        self.engine = create_engine('mysql+mysqlconnector://iamuser1:hackhpi2017@hackhpivis-cluster.cluster-csrsiurc1mom.eu-central-1.rds.amazonaws.com:3306/hackhpivis', echo=False)


    def engine(self):
        return self.engine
