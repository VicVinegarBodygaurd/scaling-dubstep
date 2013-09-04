import cPickle

class Data_store:
   def dump_data(self, var1, var2, file_name):
      output = open(file_name, 'wb')
      cPickle.dump(var1, output)
      cPickle.dump(var2, output)
      output.close()
       




