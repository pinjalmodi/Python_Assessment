student={}

def add_stu(sn,fn,ln,cn,sub1,marks1,fees1,sub2,marks2,fees2,fc):
    #student[sn]=sn
    #student[fn]=fn
    #student[ln]=ln
    #global student
    student2={
        "sno":sn,
        "fname":fn,
        "lname":ln,
        "Contact Number":cn,
        "Subject":[
            {"sub1":sub1,"Marks1":marks1,"fees1":fees1},
            {"sub2":sub2,"Marks2":marks2,"fees2":fees2},
             
            ],
        "Faculty":fc
        }
    student[sn]=student2
    print(f"{fn} added successfully!")
    print(student)

def remove_stu(sn):
    if sn in student:
        del student[sn]
        print(f"{fname} deleted successfully!")
    else:
        print(f"{fname} Not Found!")
    
def view_spe_stu(sn):
    if sn in student:
        student2=student[sn]
        print(student2)
    else:
        print("Student Not found")

def view_all():
    print(student)

    

def add_mar(sn,marks3):
    global student
    if student:
 
        if sn in student:
        
            student[sn].update({"marks3":marks3})
            #student[sn]["marks"]=marks3
            print("Marks added successfully")
        else:
            print("Student Not Found!")
    else:
        print("Empty")

    
"""
def add_mar(sn, sub, marks, fees):
    if sn in student:
        # Find the subject to update
        found = False
        for subj in student[sn]["Subject"]:
            if subj["subject"] == sub:
                subj["Marks"] = marks
                subj["Fees"] = fees
                found = True
                break
        if not found:
            # If subject is not found, add a new subject entry
            student[sn]["Subject"].append({"subject": sub, "Marks": marks, "Fees": fees})
        print("Marks added/updated successfully")
    else:
        print("Student Not Found!")
"""
def view_all_fac():
    print(student)
