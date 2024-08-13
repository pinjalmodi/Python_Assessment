import func

while True:
    print("Press 1 for Banker")
    print("Press 2 for Customer")
    print('*'*40)

    r_id=int(input("Enter your choice of Role id"))
    print('*'*40)

    if r_id==1:
        print("Press 1 for register")
        print("Press 2 for Login")
        print('*'*40)

        choice=int(input("Enter what process you wish to follow"))
        print('*'*40)
        banker=func.Banker()
        if choice==1:
            banker.register_banker()
        elif choice==2:
            
            if banker.login_banker():
                while True:
                    print("Press 1 to update customer")
                    print("Press 2 to View Customer")
                    print("Press 3 to delete customer")
                    print("Press 4 to Exit")
                    ch=int(input("Which operation you wish to perform"))
                    print('*'*40)
                    if ch==1:
            
            
                        banker.update_cust()
                    elif ch==2:
                    
                        customers=banker.view_all()
                        for i in customers:
                            print(i)
                    elif ch==3:
                    
                        banker.delete_cust()
                    elif ch==4:
                        break
            else:
                print("Invalid Username or password")
                print('*'*40)
    
                
    elif r_id==2:
        print("Press 1. for register")
        print("Press 2. for Login")
        print('*'*40)

        c=int(input("Enter your choice which process you want to follow"))
        print('*'*40)
        if c==1:
            cust=func.Customer()
            cust.register_cust()
        elif c==2:
            cust=func.Customer()
            if cust.login_cust():
                ac_no=int(input("Enter Account Number"))
                while True:
                    
                    print("Press 1.Withdraw")
                    print("Press 2.Deposite")
                    print("Press 3.View Balance")
                    print("Press 4.Exit")
                    print('*'*40)
        

                    h=int(input("Enter which operation you wish to perform"))
                    print('*'*40)
            
                    if h == 1:
                        cust.withdraw(ac_no)
                    elif h == 2:
                        cust.depo(ac_no)
                    elif h == 3:
                        Balance=cust.check_bal(ac_no)
                        if Balance is not None:
                            print(f"Your balance is {Balance}")
                    elif h==4:
                        break

            else:
                print("Invalid Username or password")
                print('*'*40)

            
