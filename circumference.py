def cir(r):
  return int(2*(22//7)*r)
def area(r):
  return (22//7)*r*r
print("for circumference enter 'c' and for area enter 'a'")
choice=input("please enter the choice (a,c)-")
num=int(input("please enter the radius of the circle-"))
if choice=="c":
  print("the circumference of the circle is-",cir(num))
else:
  print("the circumference of the circle is-",area(num))