n= int(input())
dp = [1]*n

nums= list(map(int, input().split()))

for i in range(1,n):
    for j in range(0,i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))