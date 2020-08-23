
class Per_Emp:

      basic_salary = 5000
      def calculatesalary(self,exp):
            if(exp >= 15):
                  return self.basic_salary + ((self.basic_salary*20)/100)
            
            elif( exp<15 and exp>=10):
                  return self.basic_salary + ((self.basic_salary*10)/100)
            
            elif( exp<10 and exp>=5):
                  return self.basic_salary + ((self.basic_salary*5)/100)
            
            elif(exp<5):
                  return self.basic_salary + ((self.basic_salary*0)/100)
                        
                  
            
