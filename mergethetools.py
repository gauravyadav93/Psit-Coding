nums = list(map(int,input("enter the numbers:").split()))
target = int(input("enter the target:"))
for i in range(0, len(nums)):
    for j in range(1, len(nums)):
        if nums[i]+nums[j] == target:
            print(i, j)
           
