
import fun

student={}


while True:
    print("Press 1. for counsellor")
    print("Press 2. for faculty")
    print("Press 3. for student")

    print("*"*40)


    r_id=int(input("Enter a role id"))
    

    if r_id==1:
        while True:
                   
            print("1.Add Student")
            print("2.Remove Student")
            print("3.View Specific Student")
            print("4.View All Students")
        
            print("*"*40)

            choice=int(input("Enter your choice"))
        
            if choice==1:
                sn=input("Enter a Serial Number")
                fn=input("Enter a First Name")
                ln=input("Enter a Last Name")
                cn=int(input("Enter Contact Number"))
                sub1=input("Enter a Subject1")
                marks1=int(input("Enter a Marks1"))
                fees1=int(input("Enter a Fees1"))
                sub2=input("Enter a Subject2")
                marks2=int(input("Enter a Marks2"))
                fees2=int(input("Enter a Fees2"))
                fc=input("Enter a Faculty")
                fun.add_stu(sn,fn,ln,cn,sub1,marks1,fees1,sub2,marks2,fees2,fc)
                print("*"*40)

            elif choice==2:
                sn=input("Enter Sn")
                fun.remove_stu(sn)
                print("*"*40)
            elif choice==3:
                sn=input("Enter Sn")
                fun.view_spe_stu(sn)
                print("*"*40)
            elif choice==4:
                fun.view_all()
                print("*"*40)
            else:
                print("Wrong entry")
                print("*"*40)

            y=(input("Do you want to perform any more operations?y/n"))

            if y.lower()=='n':
                print("*"*40)
                break
        
            

        
                print("*"*40)

                r_id=int(input("Enter a role id"))

            """
            if r_id==1:
                   
                print("1.Add Student")
                print("2.Remove Student")
                print("3.View Specific Student")
                print("4.View All Students")
                
                print("*"*40)

                choice=int(input("Enter your choice"))
        
                if choice==1:
                    sn=input("Enter a Serial Number")
                    fn=input("Enter a First Name")
                    ln=input("Enter a Last Name")
                    cn=int(input("Enter Contact Number"))
                    sub1=input("Enter a Subject1")
                    marks1=int(input("Enter a Marks1"))
                    fees1=int(input("Enter a Fees1"))
                    sub2=input("Enter a Subject2")
                    marks2=int(input("Enter a Marks2"))
                    fees2=int(input("Enter a Fees2"))
                    fc=input("Enter a Faculty")
                    fun.add_stu(sn,fn,ln,cn,sub1,marks1,fees1,sub2,marks2,fees2,fc)
                    print("*"*40)

                elif choice==2:
                    sn=input("Enter Sn")
                    fun.remove_stu(sn)
                    print("*"*40)
                elif choice==3:
                    sn=input("Enter Sn")
                    fun.view_spe_stu(sn)
                    print("*"*40)
                elif choice==4:
                    fun.view_all()
                    print("*"*40)
                else:
                    print("Wrong entry")
                    print("*"*40)
"""
    elif r_id==2:
        while True:
            

            print("1.Add marks to student")
            print("2.View All students")
           

            choice1=int(input("Enter faculty choice:"))

            if choice1==1:
                sn=input("Enter Sn")
                marks3=int(input("Enter marks3"))
            
                fun.add_mar(sn,marks3)
                print("*"*40)
            
            elif choice1==2:
                fun.view_all_fac()
                print("*"*40)
  #  elif choice1==3:
   #     print("*"*40)
    #    break
            else:
                print("Wrong Entry!")
                print("*"*40)
            y=(input("Do you want to perform any more operations?y/n"))

            if y.lower()=='n':
                print("*"*40)
                break


    elif r_id==3:
        break
 #   print("*"*40)
  #  break



