
'''
    Autor: Guilherme Gandolfi
    Data: 2020-08-19
    Desc: The class is a connection with database and other functions
'''
import pandas as pd


class CargaArquivo:
    def __init__(self):
        self.path='/home/guilherme/Documentos/projetos_git/da-airbnb-ny/in'
        self.name_file='AB_NYC_2019.csv'
        self.df=""

    def carrega_data_frame(self):
        print(self.path)
        print(self.name_file)

        # carga do data frame
        df = pd.read_csv(self.path+'/'+self.name_file)
        return df


if __name__ == "__main__":
    ca = CargaArquivo()
    df = ca.carrega_data_frame()
    print (df.dtypes)
   
