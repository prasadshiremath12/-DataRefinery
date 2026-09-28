n=[1,3,[2,4],[5,7],0]
flat=[]
for value in n:
    if isinstance(value,list):
        flat.extend(value)
    else:
        flat.append(value)

print(flat)

# sentence="hello hello world"
# freq={}
# for i in sentence.split():
#     freq[i]= freq.get(i,0)+1
# print(freq)
# rev=""
# word= "dwekjlw"
# for ch in word:
#     rev=ch+rev
# print(rev)

# n=11
# if n<=1:
#     print(False)
# else:
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             print(False)
#             break
#         else:
#             print(True)

# numbers=[3,2,50,5,6,48]
# k=2
# import heapq
# print(heapq.nlargest(k, numbers))
# print(heapq.nsmallest(k, numbers))
# print((numbers[2:])+(numbers[:2]))

# data=['ds','fd','sd','ds']
# fre={}
# for item in data:
#     if item in fre:
#         fre[item]+=1
#     else:
#         fre[item]=1
# print(fre)

# data=['ds','fd','sd','ds']
# fre={}
# for item in data:
#     fre[item]= fre.get(item,0)+1
# print(fre)

# num=[12,1,5,6,6,6,8,8,6,8,9]
# largest=sorted(num, reverse=True)[2]
# print('largest:', largest)
#
# num=[12,1,5,6,6,6,8,8,6,8,9]
# k=3
# import heapq
# a=heapq.nlargest(k,num)[2]
# print(a)

# Deduplicate
# num=[12,1,5,6,6,6,8,8,6,8,9]
# out=[]
# for i in num:
#     if i in out:
#         continue
#     else:
#         out.append(i)
# print(out)

# Finding duplicates

# num=[12,1,5,6,6,6,8,8,6,8,9]
# duplicate=[]
# for i in num:
#     if num.count(i)>1 and i not in duplicate:
#         duplicate.append(i)
# print(duplicate)

# Merge two list into a dictionary
# keys= ['name','age','city']
# values= ['John', 26, 'Belagavi']
# merged= dict(zip(keys, values))
# print(merged, "Merged")
# To find all prime numbers between 1 and 50
# i=2
# a=[]
# for num in range(2,51):
#     for i in range(2, num):
#         if num%i==0:
#             break
#         else:
#             if num not in a:
#                 a.append(num)
#
# print(a)

# Find common keys in two dictionaries
# d1= {'a':1, 'b':2, 'c':3}
# d2={'a':4, 'b':5, 'e':4}
#
# common_keys=d1.keys() & d2.keys()
# print(list(common_keys))
# print(common_keys)

# To add the sum of the digits in a number
# sum=0
# num=123456
# for a in str(num):
#     sum+=int(a)
# print(sum)
#
# # Count upper case and lower case letters
# text="HelloWorld"
# upper=0
# lower=0
# for ch in text:
#     if ch.isupper():
#         upper+=1
#     elif ch.islower():
#         lower+=1
# print(upper)

# Find the longest word in a sentence
# sentence="Python makes coding enjoyable and powerfull"
# a=sentence.split()
# b=""
# max=0
# for word in a:
#     if len(word)>max:
#         max=len(word)
#         b=word
# print(b, max)

# To find the missing records
# a=[]
# nums=[1,2,4,6,7,9]
# for i in range(min(nums), max(nums) + 1):
#     if i not in nums:
#         a.append(i)dewqed
# print(a)

# Read a file and count number of lines (USe case: Count records in a log file)
# with open('D:\Python_practice\

# Write a list of strings in a file and count number of lines (USe case: Count records in a log file)
# Lines=['apple\n','banana\n','citrus\n']
# with open(r'D:\Python_practice\Practice6.py', 'a') as file: #'w' indicates override 'a' indicates append and 'r' indicates read mode
#     file.writelines(Lines)
# print("The strings are printed")





