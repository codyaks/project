a=9
b=5
c=5
if a and b and c:
    print("all of them have boolean value ture")
else:
    print("any one of them have boolean value false")
#using "or" operator
if a>0 or b>0:
    print("any one of the no. is greater than zero")
else:
    print("none of the no. is greater than zero")
#using "not equal to" operator
print(a != b)
print(5 != c)

d="coding"
s="science" 
if d != s:
    print("both are different")
else:
    print("both are same")

f=4
g=3
if (f==4) != (g==3):
    print("both are differnt")
else:
    print("both are same")
# bmi checker
height=float(input("please enter the hieght in cm"))
weight=float(input("please enter the weight in kg"))
bmi=weight/(height/100)**2
print("your BMI is {0}".format(bmi))
if bmi<=18.4:
    print("you are underwieght")
elif bmi<=24.9:
    print("print you are healthy")
elif bmi<=29.9:
    print("print you are overweight")
elif bmi<=34.9:
    print("print you are severely over weight")
elif bmi<=39.9:
    print("print you are obese")
else:
    print("you are severely obese")