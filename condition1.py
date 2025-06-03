num=int(input("plese enter the no. you want to check-" ))
if num>0:
    print(num,"is a positive number")
if num<0:
    print(num,"is a negative number")

actamont=float(input("plese enter the amount you want to check-"))
saleamount=float(input("plese enter the sale amount -"))
if actamont<saleamount:
    profit= float(saleamount-actamont)
    print("profit is- {0}".format(profit))
else:
    loss=float(saleamount-actamont)
    print("loss is {0}".format(loss))
#check even odd
digit=int(input("plese enter the digit you want to check-"))
if digit%2==0:
    print("digit {0} is an even number".format(digit))
else:
    print("digit {0} is an odd number".format(digit))
 
