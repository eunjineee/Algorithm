N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
nums.sort()
nums.sort(key=lambda x:x[1])

ans = 0
end = -1
while len(nums) != 0:
    s, e = nums.pop(0)
    if s >= end:
        end = e
        ans += 1
print(ans)