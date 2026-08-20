class Employee:
   def __init__(self,name,base_sal,bonus,deduction):
      self.n=name
      self.salary=self.SalaryEmp(base_sal,bonus,deduction)
   def __del__(self):
      print("destructor called")
   def show_details(self):
      print(self.salary.gross_salary())
      print(self.salary.net_salary())
   class SalaryEmp:
      def __init__(self,b_sal,bon,ded):
         self.b_sal=b_sal
         self.bon=bon
         self.ded=ded
      def gross_salary(self):
         return self.b_sal+self.bon
      def net_salary(self):
         return (self.b_sal+self.bon)-self.ded
emp1=Employee("Ruthra",10000,5000,1000)
