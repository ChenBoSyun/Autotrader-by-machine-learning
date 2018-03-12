
# coding: utf-8

import stock_data
import numpy as np


class Auto_trader:
    def __init__(self):
        self.__stock_in = 0

    def action_predict(self , testing_data):
        action = 0
        if self.__stock_in == 0 :
            self.__stock_in = self.__stock_in + 1  
            self.buy = testing_data[3]
            action = 1
            
        elif self.__stock_in == 1 :
            if testing_data[3] - self.buy > 5  :
                self.__stock_in = self.__stock_in - 1  
                action = -1
  
        return action


