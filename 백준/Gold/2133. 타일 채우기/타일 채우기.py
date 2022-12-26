n = int(input())
nums = [0]*(31)
nums[2] = 3
for i in range(4,n+1,2):
    nums[i] = nums[i-2] * 3 + sum(nums[:i-2]) *2 + 2
print(nums[n])