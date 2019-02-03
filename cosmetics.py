class cosmetics:
    shopname='naturals'
    address='vijay nagar,murgeshpalya,bangalore'
    contactno=9234458199
    cfoundation=270
    cbbcream=250
    ceyeliner=175
    cmascara=180
    clipcolor=108
    clipstick=200

    
    def foundation1(foundation):
        if foundation==True:
            n=int(input('enter the quntity of the foundation'))
            return n*cosmetics.cfoundation
        else:
            return 0 
    def bbcream1(bbcream):
        if bbcream==True:
            n=int(input('enter the quntity of the bbcream'))
            return n*cosmetics.cbbcream
        else:
            return 0
    def eyeliner1(eyeliner):
        if eyeliner==True:
            n=int(input('enter the quntity of the eyeliner'))
            return n*cosmetics.ceyeliner
        else:
            return 0 
    def mascara1(mascara):
        if mascara==True:
            n=int(input('enter the quntity of the mascara'))
            return n*cosmetics.cmascara
        else:
            return 0
    def lipcolor1(lipcolor):
        if lipcolor==True:
            n=int(input('enter the quntity of the lipcolor'))
            return n*cosmetics.clipcolor
        else:
            return 0 
    def lipstick1(lipstick):
        if lipstick==True:
            n=int(input('enter the quntity of the lipstick'))
            return n*cosmetics.clipstick
        else:
            return 0

    def __init__(self,name,phoneno,foundation=False,bbcream=False,eyeliner=False,mascara=False,lipcolor=False,lipstick=False):
        self.name=name
        self.phoneno=phoneno
        
        self.foundation=cosmetics.foundation1(foundation)
        self.bbcream=cosmetics.bbcream1(bbcream)
        self.eyeliner=cosmetics.eyeliner1(eyeliner)
        self.mascara=cosmetics.mascara1(mascara)
        self.lipcolor=cosmetics.lipcolor1(lipcolor)
        self.lipstick=cosmetics.lipstick1(lipstick)

    def disp(self):
        print('name of the shop:',self.shopname)
        print('shop address:',self.address)
        print('contactno of shop:',self.contactno)
        print('name of the customer:',self.name)
        print('num of the customer:',self.phoneno)
        print('cost of foundation cream:',self.foundation)
        print('cost of the bbcream      :',self.bbcream)
        print('cost of the eyeliner     :',self.eyeliner)
        print('cost of the mascara     :',self.mascara)
        print('cost of the lipcolor    :',self.lipcolor)
        print('cost of the lipstick    :',self.lipstick)
        print('------------------------------------')
        n=self.foundation+self.bbcream+self.eyeliner+self.mascara+self.lipcolor+self.lipstick
        print('total cost is           :',n)
    
obj1=cosmetics('renu',65758947447,True,True,True,False,True,True)
cosmetics.disp(obj1)
