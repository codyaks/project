bill=int(input("please enter the bill amount"))
given=int(input("please enter the given amount"))
def due(b,g):
    return g-b
print("the due amount is-",due(bill,given))