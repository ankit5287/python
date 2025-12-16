vowel = "aeiouAEIOU"
string = input("Enter a string: ")
count = 0

for char in string:
    if char in vowel:
        count += 1
print("Number of vowels in the string:", count)

print(len(string))
print(string[::-1])

s1 = input("Enter the substring to find:")
find = string.find(s1)
r1 = input("Enter the substring to replace:")
string1 = string.replace(s1,r1)
print("Index of substring:", find)
print("String after replacement:", string1)

palinndrome = string[::-1]
if string == palinndrome:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")