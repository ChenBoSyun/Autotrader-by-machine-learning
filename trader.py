
# coding: utf-8

# In[6]:


import stock_data
import autoTrader
import numpy as np

if __name__ == '__main__':
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                       default='training_data.csv',
                       help='input training data file name')
    parser.add_argument('--testing',
                        default='testing_data.csv',
                        help='input testing data file name')
    parser.add_argument('--output',
                        default='output.csv',
                        help='output file name')
    args = parser.parse_args()
    
    # The following part is an example.
    # You can modify it at will.
    
    ##I don't fave training process
    #trader.train(training_data)

    
    stock = stock_data.Stock_Data()
    testing_data = stock.load_data(filename = args.testing)
    trader = autoTrader.Auto_trader()
    
    
    with open(args.output, 'w') as output_file:
        for row in testing_data:
            # We will perform your action as the open price in the next day.
            data = np.asarray(row)

            action = trader.action_predict(data)

            output_file.write(str(action))
            output_file.write('\n')
            # this is your option, you can leave it empty.
            #trader.re_training(i)

    
    

