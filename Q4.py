#반복문
# a = [10,20,30,10,20,30,10,20,30]
# 디버그

#for 변수(i) in range(start,stop(step)):
#len(a)=리스트의 길이
#range(0.len(a)) 0,1,2
#0 <="i" < 3
# i index 
# el element

# a=[5,8,7,9,10]
# print(list(range(0,len(a),2)))
# # for i in range(0,len(a)):
# for el in a:
#     if el % 2 ==0:
#         print(f"{el}은 짝수")
#     else :
#         print(f"{el}은 홀수")
# a = [10,20,30,10,20,30,10,20,30]
# # for 변수 in 리스트 :
# # for i in a:
# #     print(i)
# # 20<= <30
# # a=[20, 21 ,22 ]
# print(list(range(20,2,-2)))
# for i in range(20,2,-2):
#   print(i)
#   print(list(range(1,6)))
# for i in range(5,0,-1):
#     print("*"*i)
# person ={"name":"kim","age" :"13"}
# person2 ={"name":"park","age" :"15"}
# person3 ={"name":"lee","age" :"16"}
# a = [person,person2,person3]
from pickle import PERSID


person_excel =  [["name","age"],["kim",13],["park",15],["lee",16]]
keys=person_excel[0] #["name","age"]
datas=person_excel[1:] #["kim",13],["park",15],["lee",16]
save = []
for data in datas:
    tmp={}
    for i in range(0,len(keys)):
        tmp[keys[i]] = data[i]
    save.append(tmp)
print(save)
    #     tmp[key]=""
    # for el in data:
    #     tmp[key]=el
# range(0,len(keys))=[0.1]
