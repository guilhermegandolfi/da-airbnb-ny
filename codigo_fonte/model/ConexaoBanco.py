'''
    Autor: Guilherme Gandolfi
    Data: 2020-08-19
    Desc: The class is a connection with database and other functions
'''

import psycopg2


class ConexaoBanco:

    # construtor
    def __init__(self):
        self.conn = ""
        self.cursor = ""
        self.user = "postgres"
        self.password="mysecretpassword"
        self.host = "localhost"
        self.database="postgres"
        self.port="5432"

    # metodo de conexao
    def conexao(self):
        self.conn = psycopg2.connect(user=self.user, host=self.host, password=self.password, port=self.port,
                                     database=self.database)
        self.cursor = self.conn.cursor()

    def execute_sql(self, query):
        self.cursor.execute(query)
        self.conn.close()

    def execute_query(self, query):
        self.cursor.execute(query)
        for a in self.cursor.fetchall():
            print(a)
        self.conn.close()



if __name__ == "__main__":
    cb = ConexaoBanco()
    cb.conexao()
    cb.execute_query("select * from pg_catalog.pg_aggregate")
