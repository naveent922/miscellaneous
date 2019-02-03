class govt:
    cardname='aadarcard'

    def disp(self):
        print('card name is:',self.cardname)
        print('name of the candidate:',self.name)
        print('phno of th candidate:',self.phno)
        print('date of birth of the candidate:',self.dob)
        print('address of the candidate',self.address)
        print('father name of the candidate:',self.fname)

    def __init__(self,name,phno,dob,address,fname):
        self.name=name
        self.phno=phno
        self.dob=dob
        self.address=address
        self.fname=fname
    @staticmethod
    def modify():
        govt.cardname='voter id card'

    def modifyadhaar(self,name,dob):
        self.name=name
        self.dob=dob
        
govt.modify()
obj1=govt('Naveen',5678943210,'24/02/1998','bharathinagar,chennai','Satyam')
govt.disp(obj1)
govt.modifyadhaar(obj1,'Naveen','23/02/1999')
print()
govt.disp(obj1)
