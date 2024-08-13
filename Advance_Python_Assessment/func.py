import mysql.connector

def create_conn():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Bank"
    )
class Customer:
    def register_cust(self):
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into Customer(ac_no,fn,ln,dob,username,password,Balance) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        ac_no=int(input("Enter account number"))
        fn=input("Enter your First Name")
        ln=input("Enter your Last Name")
        dob=input("Enter your Date of Birth")
        username=input("Enter your Username")
        cursor.execute('SELECT * FROM Customer WHERE username = %s',(username,))
        if cursor.fetchone():
            print(f'username "{username}" Not available')
            username=input("Enter your Username")
        else:
            print(f'username "{username}" Available')
            
        password=input("Enter your Password")
        Balance=int(input("Enter the Balance"))
        cursor.execute(query, (ac_no,fn,ln,dob,username,password,Balance))
        conn.commit()
        print("Customer successfully Registered")
        cursor.close()
        conn.close()

    def login_cust(self):
        conn=create_conn()
        cursor=conn.cursor()
        query="SELECT * FROM Customer Where username= %s and password =%s"
        username=input("Enter your Username")
        password=input("Enter your Password")
        cursor.execute(query,(username,password))
        result=cursor.fetchone()
        if result:
            print("Login Successful")
            return True
        else:
            
            return False
        cursor.close()
        conn.close()
    def withdraw(self,ac_no):
        conn=create_conn()
        cursor=conn.cursor()
        cursor.execute(("SELECT Balance FROM Customer WHERE ac_no = %s"),(ac_no,))
        result= cursor.fetchone()
        Balance=result[0]
        withd=int(input("Enter Amount to withdraw"))
        if withd <= Balance:
            Balance=Balance-withd
        else:
            print("Insufficient Balance")
        
        query = "UPDATE Customer SET Balance=%s where ac_no = %s "
        cursor.execute(query, (Balance,ac_no,))
        conn.commit()
        print("Amount withdrawn successfully!")
        cursor.close()
        conn.close()

    def depo(self,ac_no):
        conn=create_conn()
        cursor=conn.cursor()
        cursor.execute("SELECT Balance FROM Customer WHERE ac_no = %s",(ac_no,))
        result= cursor.fetchone()
        if result:
            Balance=result[0]
            depos=int(input("Enter Amount to deposite"))
            Balance=Balance+depos
            query = "UPDATE Customer SET Balance=%s where ac_no = %s "
            cursor.execute(query, (Balance,ac_no))
            conn.commit()
            print("Amount Deposited successfully!")
        else:
            print("Account No Not Found!")
        cursor.close()
        conn.close()
        
    def check_bal(self,ac_no):
        conn=create_conn()
        cursor=conn.cursor()
        query="SELECT (Balance) FROM Customer where ac_no = %s"
        cursor.execute(query, (ac_no,))
        result=cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return result[0]
        else:
            print("Account not found")
            return None


class Banker(Customer):
    def register_banker(self):
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into Banker(fname,lname,dob,username,password) values(%s, %s, %s, %s, %s)"
        fname=input("Enter your First Name")
        lname=input("Enter your Last Name")
        dob=input("Enter your Date of Birth")
        username=input("Enter your Username")
        cursor.execute('select * from Banker where username = %s',(username,))
        if cursor.fetchone():
            print(f'username "{username}" Not available')
            username=input("Enter your Username")
        else:
            print(f'username "{username}" Available')
            
        password=input("Enter your Password")
        cursor.execute(query, (fname,lname,dob,username,password))
        conn.commit()
        print("Banker successfully Registered")
        cursor.close()
        conn.close()
    def login_banker(self):
        conn=create_conn()
        cursor=conn.cursor()
        query="SELECT * FROM Banker Where username= %s and password =%s"
        username=input("Enter your Username")
        password=input("Enter your Password")
        cursor.execute(query,(username,password))
        result=cursor.fetchone()
        if result:
            print("Login Successful")
            return True
        else:
            
            return False
        cursor.close()
        conn.close()

    def update_cust(self):
        conn=create_conn()
        cursor=conn.cursor()
        ac_no=int(input("Enter Account Number"))
        query="SELECT * FROM Customer WHERE ac_no= %s"
        cursor.execute(query, (ac_no,))
        result=cursor.fetchone()
        if not result:
            print(f"No customer founr with {ac_no}")
        else:
            print(f"Customer details for {ac_no}")

            print(f"First Name:{result[2]}")
            print(f"Last Name:{result[3]}")
            print(f"DOB:{result[4]}")

            fin=input("Enter new First name")
            lan=input("Enter new last name")
            daob=input("Enter new dob")

            updates = []
            up_que = []
    
            if fin:
                up_que.append("fn = %s")
                updates.append(fin)
            if lan:
                up_que.append("ln = %s")
                updates.append(lan)
            if daob:
                up_que.append("dob = %s")
                updates.append(daob)
    
    
    
            up_que_str = "UPDATE Customer SET " + ", ".join(up_que) + " WHERE ac_no = %s"
            updates.append(ac_no)
    
    
            cursor.execute(up_que_str, tuple(updates))
            conn.commit()
            print("Customer Updated Successfully")
            cursor.close()
            conn.close()
            
            
    def view_all(self):
        conn=create_conn()
        cursor=conn.cursor()
        query = "SELECT * FROM Customer"
        cursor.execute(query)
        result=cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def delete_cust(self):
        conn=create_conn()
        cursor=conn.cursor()
        ac_no=int(input("Enter Account No to delete"))
        query= " DELETE FROM Customer WHERE ac_no= %s "
        cursor.execute(query , (ac_no,))
 
        conn.commit()
        if cursor.rowcount >0:
            
            print('f {ac_no}DELETED Successfully!')
        else:
            print("No account Found")
        cursor.close()
        conn.close()
        
        

        



