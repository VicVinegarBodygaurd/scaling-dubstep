import cPickle
from os import path, access, R_OK, W_OK
from utility import Util

class Data_store:  
   def dump_data(self, var1, var2, fname):
      PATH = '%s' % fname
    
      if path.isfile(PATH) and access(PATH, W_OK):
         with file(fname, 'r+') as f:
            cPickle.dump(var1, f, -1)
            cPickle.dump(var2, f, -1)
            f.close()
      else:
         output = open(fname, 'w')
         cPickle.dump(var1, output, -1)
         cPickle.dump(var2, output, -1)
         output.close()
   def load_data(self, fname):
      obj = Util()
      lnum = obj.file_len(fname)
      with open(fname, 'r') as f:
      	#output = open(fname, 'r')
     	 for i in range(0, lnum+1):  
            data = cPickle.load(f)
            print data 
      f.close()
