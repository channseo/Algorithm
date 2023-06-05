n = int(input())
nums = list(map(int, input().split()))
result = 0

for num in nums:
    count = 0 
    if num > 1:
        for i in range(2, num+1):
            if num % i == 0:
                count += 1

    if count == 1:
        result += 1
        
print(result)
     
        