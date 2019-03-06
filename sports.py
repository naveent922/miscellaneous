class store:
    shopname="Sportsline"
    shopadd="yelahanka, Bangalore"
    shopno=908798800
    rackets=2000
    shoes=1000
    shirt=500
    pant=600

    
    def racket(racket1):
        if racket1==True:
            n=int(input("enter the quantiy of rackets"))
            return n*store.rackets
        else:
            return 0
    def shoe(shoe1):
        if shoe1==True:
            n=int(input("enter the quantiy of shoes"))
            return n*store.shoes
        else:
            return 0

    def shirts(shirt1):
        if shirt1==True:
            n=int(input("enter the quantiy of shirt"))
            return n*store.shirt
        else:
            return 0    

    def pants(pant1):
        if pant1==True:
            n=int(input("enter the quantiy of pants"))
            return n*store.pant
        else:
            return 0    

    def __init__(self,name,phno,racket1=False,shoe1=False,shirt1=False,pant1=False):
        self.name=name
        self.phno=phno
        self.racket=store.racket(racket1)
        self.shoe=store.shoe(shoe1)
        self.shirts=store.shirts(shirt1)
        self.pantz=store.pants(pant1)
        
                          
    def disp(self):
        print("name of store : ",store.shopname)
        print("adress of shop : ",store.shopadd)
        print("shop number : " ,store.shopno)
        print("cost of rackets" ,self.racket)
        print("cost of shoes : ",self.shoe)
        print("cost of shirts : ",self.shirts)
        print("cost of pants : ",self.pantz)
        
        #total cost
        
        total=self.racket+self.shoe+self.shirts+self.pantz
        print("total cost : ",total)

ob1=store("naveen",+9189898988,True,True,True,True)
ob1.disp()
