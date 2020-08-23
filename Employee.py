from connect import myconnect 
from PermanentEmployee import Per_Emp
from validation import Validation as vail
class Employee:
      
      _empname=""
      _emptype=""
      _empemail=""
      _empsalary=""

      def __init__(self):
            self._empname = input("enter name: ")
            self._empemail=input("enter email: ")
            v_no = vail()
            while(not v_no.valid_email_id(self._empemail)):
                  self._empemail = input("enter email:")
            self._empmob=input("enter mobile no: ")
            while(not v_no.valid_contact_no(self._empmob)):
                  self._empmob = input("enter mobile no:")
            self._emptype = input("enter type: ")
            self._empexp = int(input("enter experience : "))
            self._empsalary = self.getsalary()
            
      def getsalary(self):
            if self._emptype=="P" or self._emptype=="p":
                  Opemp = Per_Emp()
                  return Opemp.calculatesalary(self._empexp)
            else:
                  print("Invalid Employee. Please enter only 'p' or 'P'")
                  
      @staticmethod
      def addnote(self):
            self.str = input("Enter your note :")
            f =open("Note.txt","a")
            f.write(self.str+"\n")
            print("Add note")
            f.close()
            
                  
print("1. Add Emp")
print("2. Display Emp")
print("3. Add Notes")
choice = int(input("Enter your Choice:"))
if choice == 1:
      c = Employee()
      obj = myconnect()
      obj.savetodb(c._empname,c._empemail,c._empmob,c._emptype,c._empexp,c._empsalary)
elif choice==2:
      obj = myconnect()
      obj.display()
elif choice==3:
      Employee.addnote()
else:
      print("invalid choice")
      
