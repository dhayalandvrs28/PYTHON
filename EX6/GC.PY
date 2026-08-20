import gc
class student:
   def __init__(self,name):
      self.name=name
      print("student",self.name,"created")
      def __del__(self):
         print("student",self.name,"destroyed")
gc.enable()
s=student("Alan")
print("calling garbage collection manually")
gc.collect()
print("End of program")
