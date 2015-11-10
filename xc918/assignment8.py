#Author: Xing Cui
#NetID: xc918
#Data: 11/08

from investment import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys



try:
    """
    This is the main program that runs with positions set to [1, 10, 100, 1000] and num_trials set to 10000.
    It will save four histograms and a results.txt file. 
    """
    while True:
        positions = raw_input('Please enter a list of numbers of shares like [1,10,100,1000] or type "quit" to exit. ')
        #convert an input string [1,10,100,1000] into a list.
        positions = positions.split(',')
        positions[0] = positions[0][1:]
        positions[-1] = positions[-1][:-1]
        positions = [int(i) for i in positions]


        if positions == [1,10,100,1000]:
            num_trials = 10000
            initial_amount = investment(1000)
            result_table = pd.DataFrame(columns = ["position", "mean", "std"])
            n = 0

            for position in positions:
                daily_ret = initial_amount.daily_investment(position, num_trials)
                result_table.loc[n] = [position, np.mean(daily_ret), np.std(daily_ret)]
                n = n + 1
                picture = plt.figure()
                plt.hist(daily_ret, 100, range=[-1,1])    # plot histogram
                plt.title('Histogram of Daily Return for Position {}'.format(position))
                plt.xlabel('Daily Return')
                picture.savefig('histogram_{}_pos.pdf'.format(str(position)))
                result_table.to_csv('results.txt', sep=',')
                print "Histograms have been saved as .pdf at current directory."
            print "Text file has been saved as \"results.txt\" at current directory."
        elif positions == 'quit':
            print "Bye~"
            sys.exit()


except KeyboardInterrupt:
	print 'Oops, interruption.'
except TypeError:
	print 'Oops, invalid type.'
except ValueError:
	print 'Oops, invalid value.'





