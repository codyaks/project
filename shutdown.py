password=(input("please set an alphabetical password-"))
if password<="z" and password>="a" or password<="Z" and password>="A":
    print("password is successfully set")
else:
    print("please try again!")

def codition_r():
    print("before restart make sure-")
    print("that you have saved all your documents")
    print("no importanttad is opened in browser")
    print("any update is not going on")
    f=input("do you want to proceed?,enter your option y or n-")
    if f=="y":
        print("initiating restart")
    else:
        print("restart cancelled")

def codition_s():
    print("before shutdown make sure-")
    print("that you have saved all your documents")
    print("no important is opened in browser")
    print("any update is not going on")
    f=input("do you want to proceed?,enter your option y or n-")
    if f=="y":
        print("starting the shutdown")
    else:
        print("shutdown cancelled")
print("please select the operation")
print("for shutdown type s")
print("for restart type r")
op=input("please enter an option s/r--")
if op=="s":
    p=input("please enter the password-")
    if p==password:
        codition_s()
    else:
        print("incorrect password")
else:
    codition_r()