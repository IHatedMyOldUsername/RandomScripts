import numpy as np
import matplotlib.pyplot as plt

def fibbon(length):
    FibList = []
    A=1
    B=1
    for i in range(1,length):
        A,B = B,A+B
        FibList.append(B);
    return FibList

y = fibbon(10)
x = range(1,10)

print(x)
plt.scatter(x,y)
plt.show()