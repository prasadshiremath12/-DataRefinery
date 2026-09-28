# s='aaabbccddddeefghiijjjkkklmnppqwrtymhjgklaaaaaa'
# count=1
# result1=""
# for i in range(len(s)):
#     if i<len(s)-1 and s[i]==s[i+1]:
#         count+=1
#     else:
#         result1+=str(count)+s[i]
#         count=1
# print(result1)
#
# result=[]
# count=1
# for i in range(len(s)-1):
#     if s[i]==s[i+1]:
#         count+=1
#     else:
#         result.append(f"{count}{s[i]}")
#         count=1
# result.append(f"{count}{s[-1]}")
# print("".join(result))

# Sentence="PrasadSHiremath"
# for char in Sentence.split():
#     a="".join(char[::-1])
# print(a)
#
# ae="".join(char[::-1] for char in Sentence.split())
# print(ae)

# for ch in s:
#     if s.count(ch)==1:
#         print(ch)
#         break;

# vowels = {'a','e','i','o','u'}
# freq={}
# for ch in s:
#     if ch in vowels:
#         freq[ch]=freq.get(ch,0)+1
# print(freq)

# result=""
# for char in s:
#     if char not in result:
#         result+=char
# print(result)
# s1='cds'
# if(sorted(s)==sorted(s1)):
#     print("Anagram")
# else:
#     print("Not Anagram")

# freq={}
# for ch in s:
#     freq[ch]=freq.get(ch,0)+1
# print(freq)
#
# print(max(freq, key=freq.get))
# print(min(freq, key=freq.get))
#
# a=19
# b=10
# a,b=b,a
# print(a,b)

# name="prasad"
# rev=""
# for character in name:
#     rev=character+rev
# print(rev)

# name="madam"
# if (name==name[::-1]):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# Num=int(input("Enter the number to test if it is a prime number"))
# if Num<=1:
#     print("Enter the number greater than 1")
# else:
#     for i in range(2,int(Num**0.5)+1):
#         if Num%i==0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")

# Num=int(input("Enter the number for fibonnaci"))
# fibonacci=[]
# for i in range(1,Num+1):
#     fibonacci.append(i)
# print(fibonacci)

# non_duplicate=[]
# List=[5,5,6,6,56,5,69,61,6,6,65,465,465,468]
# a=set()
# for i in List:
#     if i not in non_duplicate:
#         non_duplicate.append(i)
#         a.add(i)
# print(non_duplicate)
# print(a)

# out=[]
# a=[1,3,5]
# b=[2,4,6]
# for value in a:
#     out.append(value)
# for value in b:
#     out.append(value)
#
# print(sorted(out))
# out=[]
# s=[1,[1,3,5],[4,9,7],6,5,8,65,3]
# for value in s:
#     if isinstance(value, list):
#         out.extend(value)
#     else:
#         out.append(value)
# print(sorted(out))

# freq={}
# sentence="I am an entrepreneur I "
# for word in sentence.split():
#     freq[word]=freq.get(word,0)+1
# print(freq)

# list=[1,5,6,5,58,6]
# if(list==list[::-1]):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# nums=[1,6,2,5,6,6,324,54]
# k=2
# import heapq
# print(heapq.nsmallest(1, nums)[-1])

# n=15
# Prime=[]
# list=range(2,n+1)
#
# for value in list:
#     for j in range(2,int(value**0.5) + 1):
#         if value % j==0:
#             break
#     else:
#             Prime.append(value)
# print(Prime)

# s="abcdef"
# k=2
# print(s[k:]+s[:k])

# def fib_gen():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
#
# a=fib_gen()
# for _ in range(10):
#     print(next(a))

# data=['apple','banana','mango','apple','pomogranate']
# freq={}
# for i in data:
#     freq[i]=freq.get(i,0)+1
# print(freq)
# rev=""
# string="suresh"
# for char in string:
#     rev=char+rev
# print(rev)

import heapq
from math import factorial

# nums=[15,20,25,30,55,1,5,35,35]
# # sortednums=list(sorted(nums, reverse=True))
# # print(sortednums[2])
# print(heapq.nlargest(3, nums)[-1])

# non_duplicate=[]
# duplicate=[]
# a=set()
# nums=[15,20,25,30,55,1,5,35,35,15,15,20,15,15]
# for i in nums:
#     if nums.count(i)>1 and i not in duplicate:
#         duplicate.append(i)
#         a.add(i)
# for i in nums:
#     if i not in non_duplicate:
#         non_duplicate.append(i)
# print(non_duplicate,"Non-duplicate")
# print(duplicate,"Duplicate")
# print(a)

# out=[]
# data=[1,2,[5,6],[7,8,9],5,[8,9,7]]
# for value in data:
#     if isinstance(value, list):
#         out.extend(value)
#     else:
#         out.append(value)
# print(sorted(out))

# countries=['India','Pakistan', 'Afghanistan','Bangladesh','Srilanka','NewZealand','Australia']
# for i in range(len(countries)):
#     for j in range(i+1,len(countries)):
#         print(f"{countries[i]} vs {countries[j]}")

# students=[{"name":"Prasad", "age":32, "Grade":"A"},
# {"name":"PDKD", "age":28, "Grade":"B"},{"name":"Karthik","age":30, "Grade":"C"}]
#
# sorted_students = sorted(students, key=lambda x:x["Grade"]) #key signifies it is sorting key not dict key, so we place the col name which name to be sorted
# print(sorted_students)

# word="dskjdn"
# if word==word[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# freq={}
# vowels=['a','e','i','o','u']
# string="hello world"
# for char in string:
#     if char in vowels:
#         freq[char]=freq.get(char,0)+1
# print("freq:",freq)

# numbers=[1,2,3,4,5,6]
# even=[num for num in numbers if num%2==0]
# odd=[num for num in numbers if num%2!=0]
# print("even",even)
# print("odd",odd)

# data=[1,2,3,1,1,5,6]
# print(list(set(data)))

# a,b=2,4
# a,b=b,a
# print(a,b)

# To find the common elements in the list
# list1=[1,2,3,4]
# list2=[3,4,5,6]
# compare=list(set(list1) & set(list2))
# # compare=list(set(list1) & set(list2))
# print(compare)

# factorial=1
# num=int(input("enter a number"))
# for i in range(1,num+1):
#     factorial *=i
# print(factorial)

# s="PrasadSHiremath"
# freq={}
# for char in s:
#     freq[char]=freq.get(char,0)+1
# print(freq)

# Merge two dictionary
# Dict1={'a':10,'b':20,'c':30}
# Dict2={'d':40,'e':50,'f':60}
# print({**Dict1,**Dict2})

# Sentence="lkds dcsslk mcs;mcs ldma ad;l"
# freq={}
# for word in Sentence.split(" "):
#     freq[word]=freq.get(word,0)+1
# print(freq)

# List=[10,5,2,63,4,89,23,1,5,2,3,4,8,9,6,9]
# unique=sorted(list(set(List)), reverse=True)[1]
# print(unique)

# Students=[{'Name':'Prasad','Age':26,'Qualification':'B.E','Place':'Belagavi'},
#           {'Name':'Karthik','Age':25,'Qualification':'B.E','Place':'Sankeshwar'},
#           {'Name':'Mahesh','Age':27,'Qualification':'PhD','Place':'Hubballi'},
#           {'Name':'Jeevan','Age':24,'Qualification':'B.E','Place':'Dharwad'}]
#
# sorted=sorted(Students, key= lambda x:x['Age'], reverse=True)
# print(sorted)

# Fruits={'Banana':12,"Mango":24,"Apple":6,"Pomogranite":3,"Guava":12}
# sorted_fruits=dict(sorted(Fruits.items(), key=lambda x:x[1]))
# print(sorted_fruits)

# Students={'Name':'Prasad',"Age":26, "Qualification":"BE"}
# Merge={**Fruits,**Students}
# print(Merge)

# Prime=[]
# for i in range(2,51):
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             break
#     else:
# 	     Prime.append(i)

# print(Prime)

# d1={'a':1,'b':2,'c':3}
# d2={'b':3,'c':3,'d':5}
# common_pair=dict(d1.items() & d2.items())
# print(common_pair)
#
# compare_key=sorted(d1.keys() & d2.keys())
# print(compare_key)

# import string
# sentence ="Hey, There Good Morning!"
# Clean_sentence="".join(ch for ch in sentence if ch not in string.punctuation)
# print(Clean_sentence)

# To find number divisible by bot 3 and 5
# nums=[i for i in range(1,51) if i%3==0 and i%5==0]
# print(nums)

# Find maximum occuring character in a string
# sentence="Hey, there hello honey bunney, where are you?"
# freq={}
# for char in sentence.upper():
#     freq[char]=freq.get(char,0)+1
# print(freq)
# maximum=max(freq.items(),key=lambda x:x[1])
# print(maximum)

# missing=[]
# nums=[1,2,4,6,8]
# for i in range(1,10):
#     if i not in nums:
#         missing.append(i)
# print(missing)

# summation=0
# Number=152
# for digit in str(Number):
#     summation+=int(digit)
# print(summation)

# sentence="Hey, there hello honey bunney, where are you?"
# upper=sum(1 for ch in sentence if ch.isupper())
# lower=sum(1 for ch in sentence if ch.islower())
# print(upper)
# print(lower)

# set1={1,2,3,4,5,6,7,8,9}
# set2={5,10,5,8}
# compare=set1 & set2
# print(compare)

# sentence="Hey, there hello honey bunney, where are you?"
# words=sentence.split()
# longest=max(words, key=len)
# print(longest)

# import json
# json_data='{"name":"Raghavendra","Occupation":"Tester","Company":"DxC"}'
# data=json.loads(json_data)
# print(data)

# data=["dsa\n","dsde\n","ook\n","wqe\n"]
# with open(r"G:\Test.txt",'a') as Prasad_S_Hiremath_resume:
#     Prasad_S_Hiremath_resume.writelines(data)
# print("Printed lines in Test.txt file")

# with open(r"G:\Test.txt","r") as file:
#     line=file.readlines()
# print(line)

# employees= [{"Name":"Rishikesh","age":25,"Department":"Data Engineering"},
#             {"Name":"Jaiganesh","age":24,"Department":"Python developer"},
#             {"Name":"Vikram","age":45,"Department":"Management"}]
# print(sorted(employees, key= lambda x:x['age'], reverse=True))
# print(sorted(employees, key= lambda x:x['Name'], reverse=False))
# print(sorted(employees, key= lambda x:x['Department'], reverse=True))

# Filtering records based on Lambda and filter()
# list1=[10,25,36,40,156,110,156,190]
# Divisible_by_10=list(filter(lambda x:x % 10==0, list1))
# print(Divisible_by_10)

# Handling of file not found exception
# try:
#     with open(r"G:\Test.txt",'r') as file:
#         print(file.readlines()) # if I use readline() it only reads first line, If I use readlines() it reads all the lines
# except FileNotFoundError:
#     print("File not found, please check the file name and file path correctly")

# freq={}
# with open(r"G:/Test.txt","r") as file:
#     for word in file:
#         freq[word]=freq.get(word,0)+1
# print(freq)

# from collections import Counter
# with open(r"G:/Test.txt", "r") as file:
#     word=file.read().split()
# word_count=Counter(word)
# print(word_count)

# a=[]
# data=["apple","","banana","","","sfdsw"]
# for items in data:
#     if items!="":
#         a.append(items)
# print(a)

# cleaned=list(filter(None, data))
# print(cleaned)

# employees=[{"Name":"Vikram", "Salary":200000},{"Name":"Nagasiva","Salary":100000},{"Name":"Prasad","Salary":31000}]
# highest_salaried_emp=list(sorted(employees, key=lambda x:x["Salary"],reverse=True))[0]
# print(highest_salaried_emp["Name"])

# highest_salaried_emp=max(employees, key= lambda x:x["Salary"])
# print(highest_salaried_emp["Name"])

# import csv
# with open(r"G:/Test2.csv","r") as csv_file:
#     csv_reader=csv.DictReader(csv_file)
#     print(csv_reader.fieldnames)
#     for row in csv_reader:
#         print(row)

# Sentence="Python is easiest language engine developed by a developer d a d f a dwsdlkw"
# print(set(Sentence.lower().split()))

# import heapq
# nums=[10,50,20,80,30,90]
# top_N=heapq.nlargest(3,nums)
# print(top_N)
# N=3
# sorted_nums=sorted(nums, reverse=True)[:N]
# print("Top N elements from a list",sorted_nums)

# def gen():
#     for i in range(10):
#         yield i
# for i in gen():
#     print(i)

# Reverse an integer
# num=121365346456135
# rev=0
# while num>0:
#     rev=rev*10+num%10
#     num=num//10
# print(rev)

# s="interview"
# vowels="aeiou"
# count=sum(1 for char in s if char.lower() in vowels)
# print(count)

# factorial=1
# Number=int(input("Enter a number: "))
# for i in range(1,Number+1):
#     factorial=factorial*i
# print(factorial)

# Fibonacci series
# num=int(input("Enter a number: "))
# a,b=0,1
# for _ in range(num):
#     a,b=b,a+b
#     print(a, end="") #If I don't use end="" then the result comes in steps

# Check Prime Number
# a=[]
# num=int(input("Enter a number: "))
# for i in range(2,int(num**0.5)+1):
#     if num%i==0:
#         print(f"{num} is not a prime number")
#         break
# else:
#     print(f"{num} is a Prime Number")

# Largest element in a list
# nums=[10,25,5,80,50]
# print(max(nums))

# freq={}
# s="banana"
# for char in s:
#     freq[char]=freq.get(char,0)+1
# print(freq)

# dict1={"sad":"dad","dasdw":"grtgr",1:4}
# dict2={"we":"rf","vb":"pplo",1:4}
# Merge= {**dict1,**dict2}
# print(Merge)

# n=153
# sum_=sum(int(i)**3 for i in str(n))
# print("Armstrong" if n==sum_ else "Not armstrong")

# Swap two numbers without using temp
# a,b=5,6
# b,a=a,b
# print(a,b)

# num=[1,6,100,56]
# import heapq
# print(heapq.nlargest(2, num)[1]) #1st method
# largest=list(sorted(num, reverse=True))[1] #2nd method
# print(largest)
#
# s1="listen"
# s2="silent"
# print("Anagram" if sorted(s1)==sorted(s2) else "Not Anagram")

# missing=[]
# nums=[1,2,5,6]
# for i in range(min(nums),max(nums)):
#     if i not in nums:
#         missing.append(i)
# print(missing)

# s=("Python interview practice")
# print(len(s.split()))

# nums=[1,2,3,4,5,6,7,8,9]
# even=[i for i in nums if i%2==0]
# odd=[i for i in nums if i%2!=0]
# print(even, odd)

# Sum if digits of a number
# num=646354654
# summ=sum(int(i) for i in str(num))
# print(summ)

# s="12345"
# print(s.isdigit())

# Star pyramid
# row=int(input("Enter a number: "))
# for i in range(1,row+1):
#     print('*'*i)

# Remove duplicates from the list
# nums=[1,1,1,1,2,3,4,5,5,6,6,7,8,9]
# print(list(set(nums)))

# Largest of three numbers
# a,b,c=10,80,50
# print(max(a,b,c))

# Sort a list without using sort()
# import heapq
# number_list=[5,2,9,1,13]
# print(heapq.nsmallest(len(number_list),number_list))

# Find all Prime numbers up to N
# n=20
# for i in range(2,n+1):
#     for j in range(2,int(n**0.5)+1):
#         if i%j==0:
#             break
#     else:
#         print(i)

# Common elements in two list
# listA=[1,2,6,8]
# listB=[4,5,6,7]
# common=list(set(listA) & set(listB))
# print(common)

# nums=[1,2,3,4,5,6,7,8,9]
# even_sum=sum(i for i in nums if i%2==0)
# print(even_sum)

# Duplicate elements from a list
# nums=[1,1,2,3,4,5,5,6]
# dup=[i for i in set(nums) if nums.count(i)>1]
# print(dup)

# Perfect number is = sum of divisor = Number itself
# n=27
# sum_=sum(i for i in range(1,n+1) if n%i==0)
# print("Perfect Number" if sum_==n else "Not perfect number")

# To find greatest common divisor
# import math
# print(math.gcd(12,18))

# Least common multiple
# import math
# a,b=12,18
# LCM=a*b//math.gcd(12,18)
# print(LCM)

# Remove special character from a string
import re
from string import punctuation

from pandas.conftest import ordered

# s="Hello@World#2$%^&*()025!"
# The below piece of cleanse the non-alphanumeric data
# re.sub(pattern, replacement, string)
# The symbol ^ signifies anything which is not in this set
# A-Za-z09 All upper case, lowercase letters and numbers
# Plus sign signifies one or more occurrence
# '' The non-alphanumeric data is replaced by an empty string
# import re
# s="Hello@World#2$%^&*()025!"
# print(re.sub(r'[^A-Za-z0-9]+','',s))

# s='abc'
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         print(s[i:j])

# import heapq
# list1=[10,5,8,20,3]
# print(sorted(list1, reverse=False)[1], "dgdf")
# print(heapq.nsmallest(2,list1)[1])

# Merge two dictionary
# d1={'a':1,'b':2,'c':3}
# d2={'d':4,'e':5,'f':6,'g':7}
# Merge={**d1,**d2}
# print(Merge)

# s='aabbcde'
# for char in s:
#     if s.count(char)==1:
#         print(char)
#         break

# year=2024
# if(year%4==0 and year%100!=0 or year%400==0):
#     print("Leap year")
# else:
#     print("Not leap year")

# flat=[]
# nested_list=[[1,2],[3,4],6,[5,6],8,[10,12],15]
# for i in nested_list:
#     if isinstance(i,list):
#         flat.extend(i)
#     else:
#         flat.append(i)
# print(flat)

# upper=lower=special=0
# s="HeLLo123@"
# for ch in s:
#     if ch.isupper():
#         upper+=1
#     elif ch.islower():
#         lower+=1
#     else:
#         special+=1
#
# print(upper,lower,special)

# nums=[10,20,5,30,6,79]
# largest=sorted(set(nums),reverse=True)
# print(largest[1])

# Move all zeros to the end
# a=[0.1,2,859,0,0,65,0,2,3,0]
# new=[x for x in a if x!=0]+[0]* (a.count(0))
# print(new)

# Print characters that appear more than once
# s="programming"
# a=[ch for ch in set(s) if s.count(ch)>1]
# print(a)

# Sentence="Python is very easy codeing language"
# Longest= max(Sentence.split(), key=len)
# print(Longest)

# Sum of digits in a number
# number=647964
# Summation=sum(int(i) for i in str(number))
# print(Summation)

# Remove all vowels from a string
# s="beautiful"
# a=""
# vowels='aeiou'
# print("".join(char for char in s if char not in vowels))

# Replace a with empty string
# s="banana"
# print(s.replace('a',''))

# Convert list of strings to integer
# st=['1','2','3']
# print(list(map(int,st)))

# n=5
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# To check if the list is sorted
# list1=[1,2,3,4]
# if list1==sorted(list1):
#     print(True)
# else:
#     print(False)

# To convert list to a string
# list1=['a','b','c']
# print(",".join(list1))
# print(",".join(value for value in list1))

# Find Index of element(manual search)
# Target=20
# array=[10,20,30]
# for i in range(0,len(array)):
#     if array[i]==Target:
#         print(i)
#         break

# # Reverse words but keep order
# s="I love python"
# Reverse=(" ".join(word[::-1] for word in s.split()))
# print(Reverse)

# Find character with highest frequency
# s='mississippi'
# freq={}
# for char in s:
#     freq[char]= freq.get(char,0)+1
# print(max(freq,key=freq.get))

# # Remove all the duplicate characters
# w="s/ldnhswij;dhqewiuldhwliuhd;iwuehduliWHDLIUWEBFLYUVFLYUADGCPWADJ,HSA CMZDH;COWBCLJD"
# non_dup="".join(char for char in w if w.count(char)==1)
# print(non_dup)

# Replace spaces with hyphens
# s="a b c d"
# print(s.replace(" ","-"))

# To find unique elements from list
# lst=[1,3,2,6,5,8,2,2,2,9,651,6,65,4,64,64,64,6]
# unique=[i for i in set(lst) if lst.count(i)==1]
# print(unique)

# # To find sum of even numbers in the list
# lst=[1,3,2,6,5,8,2,2,2,9,651,6,65,4,64,64,64,6]
# even=sum(i for i in lst if i%2==0)
# print(even)

# Count the freq of the words in a sentence (case insensitive)
# s="Hello hello HELLO world"
# freq={}
# for i in s.split():
#     freq[i]= freq.get(i,0)+1
# print(freq)

# Remove punctuation from a string
# s="kjdnwskjdnwjdfn!@#$nk.jilkbi^&*(()"
# import string
# new="".join(char for char in s if char not in string.punctuation)
# print(new)
import re
# print(re.sub(r"[^A-Za-z0-9]+",'',s))

# s1='apple'
# s2='banana'
# commonn=list(set(s1) & set(s2))
# print(commonn)

# To check Armstrong number
# cube=0
# num=153
# for i in str(num):
#     cube+=int(i)**3
# if cube==num:
#     print(f"{num} is Armstrong Number")
# else:
#     print(f"{num} is not Armstrong Number")

# Merge dictionaries (add values if keys repeat):
# d1={"a":5,"b":2}
# d2={"c":3,"d":4,"a":86}
# merge=d1.copy()
# for key, value in d2.items():
#     merge[key]= merge.get(key,0)+value
# print(merge)

# Print only digits from a string
# a="ajcnaj12kjndksj92"
# b="".join(i for i in a if i.isdigit())
# print(b)

# # Sort dictionary by values
# dict1={"d":5,"r":2,"v":56}
# print(sorted(dict1.items(), key= lambda x:x[1]))

# # Find the missing number in list
# lst=[1,2,4,5]
# miss=[]
# for i in range(min(lst),max(lst)+1):
#     if i not in lst:
#         miss.append(i)
# print(miss)

# # Remove None from the list
# list2=[1,None,2,3,None]
# clean=[i for i in list2 if i is not None]
# print(clean)

# Reverse an integer
# rev=0
# inte=654663416
# for i in str(inte):
#     rev=rev*10+int(inte)%10
#     inte=inte//10
# print("rev=",rev)

# reverse=str(inte)[::-1]
# print(reverse)

# # To check if two list are identical
# a=[1,2,3]
# b=[1,2,3]
# print("Identical" if a==b else "Not identical")

# # To find duplicate data
# list3=[4,5,6,2,231,65,6,5,654,54,646,4,5,1,31,31,3,13564685,6468,46,2,6,2,3]
# dup=[x for x in set(list3) if list3.count(x)>1]
# print(dup, "Duplicates")

# To find min, max without built in python fn
# list4=[3,1,4,2]
# max=min=list4[0]
# for i in list4:Q.
# You are given two tables: orders and customers in an e-commerce platform.
# orders table schema:
# Column	Type
# order_id 	INT
# customer_id 	INT
# order_date	DATE
# total_amount	DECIMAL(10, 2)
# customers table schema:
# Column	Type
# customer_id	INT
# name	VARCHAR(100)
# country	VARCHAR(50)
# Write a query  to retrieve the top 5 customers who have placed the highest number of orders and spent the most money in the last 6 months.
# The result should include:
# Customer name
# Total number of orders placed in the last 6 months
# Total amount spent in the last 6 months
# The list should be sorted by the total amount spent, in descending order.Q.
# You are given two tables: orders and customers in an e-commerce platform.
# orders table schema:
# Column	Type
# order_id 	INT
# customer_id 	INT
# order_date	DATE
# total_amount	DECIMAL(10, 2)
# customers table schema:
# Column	Type
# customer_id	INT
# name	VARCHAR(100)
# country	VARCHAR(50)
# Write a query  to retrieve the top 5 customers who have placed the highest number of orders and spent the most money in the last 6 months.
# The result should include:
# Customer name
# Total number of orders placed in the last 6 months
# Total amount spent in the last 6 months
# The list should be sorted by the total amount spent, in descending order.
#     if i>max:
#         max=i
#     elif i<min:
#         min=i
# print(min,max)

s="apple is an awesome fruit"
vowels="aeiou"
print(sum(1 for i in s.split() if s[0].lower() in vowels))