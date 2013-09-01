import matplotlib
import numpy as np
from matplotlib import pyplot as plt


class Graphing:

   fig = plt.figure()
   ax1 = fig.add_subplot(221)
   ax2 = fig.add_subplot(222)

   var1 = 200
   var2 = 300
   height = var2-var1


   if var1 > var2:
      plt.ylim(var2-100, var1+100)
   else: 
      plt.ylim(var1-100, var2+100)
  
   Months = 12
   se = height/Months
   height_array = np.array([height]*Months)

   
   #plots the lines for graph 1
   ax1.bar(np.arange(Months), height_array, 0.35, color = 'b')
 
   #plots the lines for graph 2
   p1 = ax2.plot([1,2,3,4,5,6,7,8,9,10,11,12], [var1,var1,var1,var1,var1,var1,var1,var1,var1,var1,var1,var1])
   p2 = ax2.plot([1,2,3,4,5,6,7,8,9,10,11,12], [var2,var2,var2,var2,var2,var2,var2,var2,var2,var2,var2,var2])

   #ax1.title("Income and Rent Expense")
   #wax2.title("Amount left per Day")

   plt.show()

