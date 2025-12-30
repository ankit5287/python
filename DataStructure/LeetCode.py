#  4.Median of two sorted array
a = [1,3]
b = [2]

c = sorted(a+b)
print(c)

end = len(c)
first = 0

mid = int((end-first)/2)
print(mid)
if len(c)%2 == 0:
    print((c[mid]+c[mid-1])/2)
else:
    print(c[mid])

# 26 Remove duplicate from sorted array

def remove(nums):
    s1 = set(nums)
    l1 = list(s1)

    nums[0:len(l1)] = l1
    return l1

print(remove([3,4,5,5,6,6]))


a1 = [1,2,3,4,5,5]
value = 5

a1.remove(value)
print(sorted(a1))

#14 Longest Common Subsequance

strs = ["flow","flower","flight"]

def func(strs):
    prifix = strs[0]

    for word in strs[1:]:
        while not word.startswith(prifix):
            prifix = prifix[:-1]
            if prifix == "":
                return ""
    return prifix

print(func(strs))

# 27 remove elements

nums = [2,3,4,5,6,6,1]

target = 6

while target in nums:
    for i in nums:
        if i == target:
            nums.remove(i)

print(nums)

