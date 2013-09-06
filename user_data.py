import json 

class testme:
   def dump_json(self, x, y, f):
      obj = [{'example': x, 'example2': y}]
      with open(f, 'a') as f:
         json.dump(obj, f, indent=2)
      f.close()
   
   #def load_json(self, f):
   
