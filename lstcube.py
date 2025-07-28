print("please enter the range of no. in min and max values")
usermin=int(input("please enter the minimum value of range"))
usermax=int(input("please enter the maximum value of range"))
lst=[]
lstodd=[]
lsteven=[]
lstcube=[]
for num in range(usermin,usermax+1):
    lst.append(num)
print("the list created-",lst)
def cube(list):
    for num in list:
        cubenum=num**3
        lstcube.append(cubenum)
        if cubenum%2==0:
            lsteven.append(cubenum)
        else:
            lstodd.append(cubenum)
    print("all cube no. in the given range are-",lstcube)
    print("even cube no. in the given range are-",lsteven)
    print("odd cube no. in the given range are-",lstodd)
cube(lst)