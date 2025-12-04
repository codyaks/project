import matplotlib.pyplot as plt
import numpy as np
x=np.array([3,7,8,1])
y=np.array([2,9,3,6])
plt.plot(x,y,marker='o',ms=10,mec='r')
plt.show()
student=['ram','sita','gita','hari']
marks=[45,20,40,50]
 
marks_percent=[]
for x in marks:
    res=(x/50)*100
    marks_percent.append(res)
print(marks_percent)
def line_graph():
    plt.plot(student,marks_percent)
    plt.title('Student Marks Percentage')
    plt.xlabel('Students')
    plt.ylabel('Marks Percentage')
    plt.show()
line_graph()

def bar_graph():
    plt.bar(student,marks)
    plt.title('Student Marks')
    plt.xlabel('Students')
    plt.ylabel('Marks')
    plt.show()
bar_graph()