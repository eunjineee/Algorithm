k, n = map(int,input().split())
nums = []
for _ in range(k):
    nums.append(int(input()))

start = 1
number = max(nums)

while start <= number:
    mid = (start + number)//2
    b = 0
    for j in nums:
        b += j//mid
    if b >= n:
        start = mid + 1
    else:
        number = mid - 1
print(number)