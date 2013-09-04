import matplotlib
import numpy as np

from Data_store import Data_store
from matplotlib import pyplot as plt

class Graphing:

   fig = plt.figure()
   ax1 = fig.add_subplot(221)
   ax2 = fig.add_subplot(222)


   #grabs users information
   var1 = float(raw_input("? "))
   var2 = float(raw_input("? "))

   ds = Data_store()


   #logs user data
   ds.dump_data(var1, var2, 'output.txt')

   height = var2-var1
   Months = 12
   height_array = np.array([height]*Months)
   
   #plots the lines for graph 1
   ax1.bar(np.arange(Months), height_array, 0.35, color = 'b')
 
   #plots the lines for graph 2
   p1 = ax2.plot([1,2,3,4,5,6,7,8,9,10,11,12], [var1,var1,var1,var1,var1,var1,var1,var1,var1,var1,var1,var1])
   p2 = ax2.plot([1,2,3,4,5,6,7,8,9,10,11,12], [var2,var2,var2,var2,var2,var2,var2,var2,var2,var2,var2,var2])

   #sets y-axis limits
   if var1 > var2:
      plt.ylim(var2-100, var1+100)
   else:
      plt.ylim(var1-100, var2+100)

   ax1.set_title("Amount Left Per Day", fontsize=15)
   ax2.set_title("Income Rate and Expenses", fontsize=15)

   plt.show()

