from datetime import date
iny=int(input("please enter the year of reminder (yyyy)"))
inm=int(input("please enter the month of reminder "))
ind=int(input("please enter the date of reminder "))
r=input("what to remind you please enter-")
x=date.today()
y=date(iny,inm,ind)
print(y)
while True:
    if x==y:
        print(r)
        break