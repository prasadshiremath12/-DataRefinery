# # def isPalindrome(x):
# #     """
# #     :type x: int
# #     :rtype: bool
# #     """
# #     # x1 = str(x)
# #     # rev = 0
# #     # for i in x1:
# #     #     rev = rev * 10 + int(i)
# #     # print(rev)
# #     #
# #     # # Check if the reversed number matches the original number
# #     # if rev == x:
# #     #     print("True")
# #     #     return True
# #     # else:
# #     #     return False
# #     x1=str(x)
# #     if x1==x1[::-1]:
# #         print("Palindrome")
# #     else:
# #         print("Not Palindrome")
# #
# # P1 = isPalindrome(121)
#
# # a,b=[1,3,5], [2,4,6]
# class sfleknk:
#     def __init__(self):
#     out=[]
#
#     i=j=0
#     while i<len(a) and j<len(b):
#         if a[i]<b[j]:
#             out.append(a[i])
#             i+=1
#         else:
#             out.append(b[j])
#             j+=1
#     out.extend(a[i:])
#     out.extend(b[j:])
#     print(out)












# Delete duplicates from the table

# with duplicate AS (select *, ROW_NUMBER() OVER(PARTITION BY NAME, SALARY ORDER BY Emp_id DESC) rn from Employee)
# Delete from Employee where rn>1;
#
# s='aabbccccdeha'
# count=1
# A=''
# for i in range (len(s)):
#     if i<len(s)-1 and s[i]==s[i+1]:
#         count+=1
#     else:
#         A+= str(count)+s[i]
#         count=1
# print(A)
# result=''
# A="Ditya Rammannavar"
# b=A.split()
# for x in b:
#     result+=x[::-1]+""
# print(result)
# print(A[::-1])

# freq={}
# s="Mechanical Engineering"
# word=s.lower()
# vowels=['a','e','i','o','u']
# count=0
# for x in word:
#     if x in vowels:
#         freq[x]=freq.get(x,0)+1
# print(freq)

# s=input("Enter a string")
# result=""
# for i in s:
#     if i not in result:
#         result+=i
# print(result)

# s1='silent'
# s2='listen'
# if sorted(s1)==sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")
#
# a="Suiyyugkjjvh,k.h;j.n;oivk.bjccess"
# max=0
# b=a.lower()
# freq={}
# for i in b:
#     freq[i]=freq.get(i,0)+1
# print(freq)
# for key, value in freq.items():
#     if value>max:
#         max=value
#         result=key
# print(result, max)

# rev=''
# word='prasad'
# for x in word:
#     rev= x+rev
# if rev==word:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# To check if a number is Prime
# n=int(input("Enter a number to check if it is prime"))
# if n<=1:
#     print("Enter a valid number greater than 1")
# else:
#         for i in range(2,int(n**0.5)+1):
#             if n%i==0:
#                 print("Not Prime")
#                 break
#             else:
#                 print("Prime")

# st=[1,2,2,3,1,4]
# seen=set()
# res=[]
# for i in st:
#     if i not in seen:
#         seen.add(i)
#         res.append(i)
# print(seen)
# print(res)
#
# l1=[2,7,11,15]
# for i in range(len(l1)):
#     for j in range(len(l1)):
#         if (l1[i]+l1[j]) ==9:
#             print(i,j)
#             break
# a=[1,3,5]
# b=[2,4,6]
# i=j=0
# out=[]
# while i<len(a) and j<len(b):
#         if a[i]<b[j]:
#             out.append(a[i])
#             i+=1
#         else:
#             out.append(b[j])
#             j+=1
# # out.extend(a[i:])
# # out.extend(b[j:])
# print(out)

# To find duplicates
# data=[1,2,3,4,2,3,5,1]
# duplicates=[]
# for i in data:
#     if data.count(i)>1 and i not in duplicates:
#         duplicates.append(i)
# print(duplicates)

a= (input("Enter the elements in the array\n").split())
b= (input("Enter the elements in the array\n").split())
# a=[1,3,5]
# b=[2,4,6]
c=[]
i=j=0
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1

c.extend(a[i:])
c.extend(b[j:])
print((c))

d=[]
d.extend(a)
d.extend(b)
print(d, "Simple")


a=[1,2,2,3,1,4]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)

A=[1,[5,3],4,[9,8],6]
out=[]
for i in A:
    if isinstance(i,list):
        out.extend(i)
    else:
        out.append(i)
print(sorted(out))

s="Hey Prasad are you looking for a job change"
freq={}
word=s.split()
for i in word:
    freq[i]=freq.get(i,0)+1
print(freq)


import heapq
nums=[1,2,3,4,5,6,7,8,9]
print(heapq.nlargest(1,nums))

number=[1,2,3,4,5,6,7,8,9]
import heapq
print(heapq.nsmallest(2,number))




