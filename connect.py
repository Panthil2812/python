import sqlite3
class myconnect:
      
      def __init__(self):
            self.conn = sqlite3.connect("Emp.db")
            self.conn.cursor()
            self.conn.execute("""CREATE TABLE IF NOT EXISTS Employee(
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name TEXT,
                        Email_id TEXT,
                        Contact_no INTEGER,
                        Type_e TEXT,
                        Salary INTEGER,
                        Experience INTEGER
                  )""")
            self.conn.commit()     
                  
      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
            self.conn.execute("INSERT INTO Employee VALUES(NULL,'{}','{}','{}','{}','{}','{}')".format(ename,eemail,emob,etype,esalary,eexp))
            self.conn.commit()

      def display(self):
            inputdata = input("Enter email_id :")
            data = self.conn.execute("SELECT * FROM Employee")
            for i in data:
                 print(i)
