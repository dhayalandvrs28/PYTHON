class Scientist:
   def __init__(self):
      self.name='Dr.kalam'
      self.info=self.Info()
   def method(self):
      print("Name:",self.name)
   class Info:
      def __init__(self):
         self.height=5.7
         self.weight=70
         self.color="Dark"
      def method(self):
         print("Height:{} weight:{} color:{}".format(self.height,self.weight,self.color))
s=Scientist()
s.method()
o=s.Info()
o.method()
