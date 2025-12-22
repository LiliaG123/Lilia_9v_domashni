def SumNums(nums):
    sum=0
    for i in nums:
        sum+=i
    return sum

def sum_recursion(numbers):
  #Towa e uslowieto za spirane na rekursiqta:
  if len(numbers) == 0:
    return 0
  else:
  #Samata rekursiq. Purwoto e purwiq element ot lista a wtoroto e funkciqta izwikana s wsichki 
  # elementi bez purwiq
    return numbers[0] + sum_recursion(numbers[1:])
  

nums=[3,2,5,2]

print("Sum is: ",SumNums(nums))
print("Sum with recursion: ",sum_recursion(nums))