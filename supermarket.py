from datetime import datetime

name = input("Enter your name:- ")

lists = '''
Rice       Rs 20/kg
Sugar      Rs 30/kg
salt       Rs 10/kg
oil        Rs 80/liter
paneer     Rs 120/kg
maggie     Rs 50/kg
boost      Rs 100/each
closeup    Rs 45/each
'''
price = 0
pricelist =[]
totalprice = 0
finalprice = 0
ilist = []
qlist = []
plist = []



items = {'rice':20,'sugar':30,'oil':80,'paneer':120,'salt':10,'maggie':50,'boost':100,'closeup':45}
option = int(input("enter your option or press 1 : - "))
if option == 1:
    print(lists)
for i in range(len(items)):
    inp1 = int(input("if u want to buy the product press 1 or press 2 for exit : -  "))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input("Enter your items : -  ")
        quantity = int(input("Enter your product quantity :- "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount =gst+totalprice
        else:
            print("sorry you entered item is not available") 
    else:
        print("you entered wrong number")
    inp = input("can i bill the items yes or no:- ")
    if inp =='yes':
        pass
        if finalamount != 0:
            print(27*"=","DMART",25*"=")
            print(25*" ","AMALAPURAM")
            print("Name : ",name,30*" ","Date",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
            for i in range(len(pricelist)):
             print(i,8*' ',2*' ',ilist[i],10*' ',qlist[i],'KG',10*' ',plist[i],'/-')
            print(75*"-")
            print(50*" ",'TotalAmount:','RS',totalprice,'/-')
            print("Gst Amount",52*" ",'RS',gst)
            print(75*"-")
            print(50*" ",'FinalAmount:','RS',finalamount,'/-')
            print(75*"-")
            print(23*" ","THANKS FOR VISITING")
            print(75*"-")


