''' A small OOPS based appications for a coffe shop to get orders from the customers
    The avaiable products are 
    
    Espresso   ----  Milk (60) , Cream (75) , Latte(100)
    Cappuccino ----  Milk (80) , Cream (90) , Latte(125)
    Latte      ----  Milk (100) , Cream (125) , Latte(150)
   
    The Outcome must be like 
    1. All the combinations that customer has ordered
    2. Total Bill included with the individual breakdown of each sample
'''

class CoffeeHouse:
    
    def __init__(self):
        self.combinations()
        self.amount = 0
        self.bill = []
        self.orderedProduct = []
        self.l={}
        self.ProductsManager()
        
    def ProductsManager(self):
        
        d = self.Products()
        prods = []
        
        for i in d:
            prods.append(i)
        prods.append("Exit")
        
        print("------MENU------\n")
        for i in range(len(prods)):
            print("{}. {}".format(i+1,prods[i]))
            
        a = int(input("Enter Your Choice :"))
        
        while(a!=4):
            print("Selected Item: {}\n".format(prods[a-1]))
            print("Select any Add-On's \n")
            
            order = d[prods[a-1]]
            sample = []
            
            b = 1
            for i,j in order.items():
                sample.append(i)
                print(f"{b}. {i} Rs.{j}".format(b,i,j))
                b+=1
                
            print('')
            
            addon = int(input("Enter the Add-on's: "))
            print("Selected Add-On :{}\n".format(sample[addon-1]))
            
            if prods[a-1] not in self.l:
                self.l[prods[a-1]]=[sample[addon-1]]
            else:
                self.l[prods[a-1]].append(sample[addon-1])
                
            self.orderedProduct.append([prods[a-1]])
            
            self.bill.append([[sample[addon-1]],order[sample[addon-1]]])
            
            self.amount+=order[sample[addon-1]]
            
            print("------MENU------")
            
            for i in range(len(prods)):
                print("{}. {}".format(i+1,prods[i]))
            a = int(input('Enter Your Choice:'))
            
            
        print('')
        print("----Final Bill----\n")
        print("----INVOICE----")
        print(self.billamount())
        print("Total Amount To Be Paid : Rs.{}\n".format(self.amount))
        print("ThankYou Visit Again")

        
    def billamount(self):
        a=0
        n=len(self.orderedProduct)
        if(n==0):
            print("Sorry! You Have Not Ordered Anything")
        while(a<n):
            print("{}. {} {} ----> Rs.{}".format(a+1,self.orderedProduct[a][0],self.bill[a][0][0],self.bill[a][1]))
            a+=1

        return ''

        
    def Products(self):
        return {
                'Espresso':{
                            "Milk":60,
                            "Cream":75,
                            "Latte":100
                            },
                "Cappuccino":{
                            "Milk":80,
                            "Cream":90,
                            "Latte":125
                            },
                "Latte":{
                        "Milk":100,
                        "Cream":125,
                        "Latte":150
                            }
               }
    def combinations(self):
        print("| -----------COFFEE HOUSE------------ |")
        print("| ----------------------------------- |")
        print("| Espresso   ----  Milk, Cream, Latte |")
        print("| Cappuccino ----  Milk, Cream, Latte |")
        print("| Latte      ----  Milk, Cream, Latte |")
        print("| ----------------------------------- |")
        print("")


        return ''


coffeeHouseObj = CoffeeHouse()
