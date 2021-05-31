print('Given a range of the first 10 numbers, Iterate from the start number to the end number, and In each iteration print the sum of the current number and previous number')

nums=0;
nums1=0;


for i in range(0,10):    
    nums=i+nums1
    print(nums)
    nums1=i
