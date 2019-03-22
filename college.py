class College:
    college_name="Atria"
    principal="Ram"
    college_code="1At01"
    annual_fees=1

    
    @classmethod
    def modcoll(cls):
        a=int(input("enter choice 1.collname,2.pricipal,3.code"))
        if a==1:
            cls.college_name=input("Enter the coll name to be updated")
        elif a==2:
            cls.principal=input("Enter principal name to be updated")
        elif a==3:
            cls.college_code=input("Enter code to be updated")
        else:
            cls.college_name=input("Enter the coll name to be updated")
            cls.principal=input("Enter principal name to be updated")
            cls.college_code=input("Enter code to be updated")
                    
    
    def __init__(self,name,usn,branch,phno,exam_fee):#hod:
        self.name=name
        self.usn=usn
        self.branch=branch
        self.phno=phno
        self.exam_fee=exam_fee
        #self.hod=hod
        
        
    def disp(self):
        print("Name of college: ",self.college_name)
        print("Name of principal: ",self.principal)
        print("College code: ",self.college_code)
        print("Name of student: ",self.name)
        print("Usn of student: ",self.usn)
        print("Branch of student: ",self.branch)
        print("Ph no of student: ",self.phno)
    
    @staticmethod
    def fees():
        total_fee=student1.exam_fee+College.annual_fees
        print("total fees: " ,total_fee)
    
student1=College("nav","1at11","mech",1234,500)
student2=College("ravi","1at12","civil",12345,600)
student3=College("rao","1at13","e&c",1345,1000)

student1.disp()
student1.fees()
