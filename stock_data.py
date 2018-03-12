# coding: utf-8


import pandas as pd

class Stock_Data:
    def load_data(self,filename):
        self.__df = pd.read_csv(filename , header=None)
        self.__features = self.__df.values

        return self.__features[:-1]
    
        
        
        
            

