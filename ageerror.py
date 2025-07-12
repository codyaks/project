try:
   age=int(input("please enter the age"))
   if age%2==0:
      print(age,"age entered is even")
   else:
      print(age,"age entered is odd")
except ValueError:
   print("the value is not correct")