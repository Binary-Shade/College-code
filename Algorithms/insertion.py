
def insertion_sort(arr):
# Traverse through 1 to len(arr)
for i in range(1, len(arr)):
key = arr[i]j
= i - 1
# Move elements of arr[0..i-1], that are greater than key, to one position ahead of their
current position
while j >= 0 and key < arr[j]:
arr[j + 1] = arr[j]
j -= 1
arr[j + 1] = key
#Function Call
import matplotlib.pyplot as plt
import time
ot=[]
T=int(input("Enter no of Excution"))
temp=0
x=[]
for j in range(0,T):
n=int(input("Enter n"))
x.append(n) my_list=[]
for i in range(0,n):
ele=int(input("Enter Element"))
my_list.append(ele)
start=time.time()
my_result = insertion_sort(my_list)
end=time.time()
time_comp=end-start
print("Sorted array is:", my_list)
temp=temp+1
ot.append(time_comp)
print("Execution Time",ot)
# Plot a graph
X=x
Y=ot
plt.plot(X,Y)
plt.show()

