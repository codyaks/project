amount=int(input("please enter the amount to be withdrawl"))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("100rs notes are-",note1)
print("50rs notes are-",note2)
print("10rs notes are-",note3)