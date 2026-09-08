def evensquared(nums):
    return [num**2 for num in nums if num%2==0]

nums = [1,2,3,4,5]
answer = evensquared(nums)
print(answer)