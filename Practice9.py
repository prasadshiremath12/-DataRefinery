input=[1,1,1,1,1,1,1,1,1,2,2,2,2,6,3,3,54,26,4,8,7,4,65,1,6,1,6,1,865,9,2,6,9]
output={}

# from collections import Counter
# # It is Python's built in fn
# A=Counter(input)
# print(A)

# def counting(input):
#     # Works only when the list is sorted
#     input=sorted(input)
#     count=1
#     output={}
#     for i in range(len(input)):
#         if i<len(input)-1 and input[i]==input[i+1]:
#             count+=1
#         else:
#             output[input[i]]=count
#             count=1
#     return output
#
# A=counting(input)
# print(A)

# def count_freq(input):
# # Works even if the input is not sorted
#     output={}
#     for i in input:
#         output[i]=output.get(i,0)+1
#     return output
#
# B= count_freq(input)
# print(B)

# input1=[1,1,2,2,2,2,2,2,3,4,4]
# def freq_of_input1(input1):
#     count=1
#     output={}
#     for i in range (len(input1)):
#         if i<len(input1)-1 and input1[i]==input1[i+1]:
#             count+=1
#         else:
#             output[input1[i]]=count
#             count=1
#     return output
#
# C=freq_of_input1(input1)
# print(C)