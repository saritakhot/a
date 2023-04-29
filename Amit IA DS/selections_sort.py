#Program to demonstrate selection_sort

import time
import tracemalloc
import matplotlib.pyplot as plt
start=time.time()

def selection_sort (nums):
    for i in range (len(nums)-1):
        minpos=i
        for j in range (i,len(nums)):
            if nums[j]<nums[minpos]:
                minpos=j
                
            temp=nums[i]
            nums[i]=nums[minpos]
            nums[minpos]=temp
        print(nums)

tracemalloc.start()
nums=[15,10,14,12]
print("Before sorting the elements: ")
print(nums)
print("\n")

print("After sorting the elements: ")
selection_sort(nums)
print(nums)

print("Space complexity= ",tracemalloc.get_tracemalloc_memory(),"bytes")
end=time.time()
print("Run time program is: ",end-start)
tracemalloc.stop()

x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title ("Selection sort time complexity is 0(n\u00b2)")
plt.xlabel("input")
plt.ylabel("Time")
plt.show()
