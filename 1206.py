# #每天吃一半多一个桃子，第十天还剩一个桃子，原来有几个桃子
# x = 1
# for i in range (9):
#     x = (x+1)*2
#     print(x)


# #1，2，3，4，四个数字能组成哪些三位数
# nums = [1,2,3,4]
# for i in nums:#for循环嵌套
#     for j in nums:
#         for k in nums:
#             print(i,j,k)


# #1，2，3，4，四个数字能组成哪些各位上互不相同的三位数
# nums = [1,2,3,4]
# for i in nums:#for循环嵌套
#     for j in nums:
#         for k in nums:
#             if (i != j) and (i != k) and (j != k):
#                 print(i,j,k)


# #水仙花数是一种三位数，其百位，十位，个位上的三位数，每个数三次方之和，是其本身，找出所有的水仙花数
# for i in range (1,10):
#     for j in range (0,10):
#         for k in range (0,10):
#             if 100*int(i)+ 10*int(j) +int(k) == i**3 + j**3 + k**3:
#                 print(100*int(i)+ 10*int(j) +int(k))


# #玫瑰花数是一种四位数，其每一位数的四次方之和，是其本身，找出所有的玫瑰花数
# for i in range (1,10):
#     for j in range (0,10):
#         for k in range (0,10):
#             for m in range (0,10):
#                 if 1000*int(i)+ 100*int(j) +10*int(k) + int(m) == i**4 + j**4 + k**4 + m**4:
#                     print(1000*int(i)+ 100*int(j) +10*int(k) + int(m))


# #两个乒乓球队进行比赛，各出三人，每个人只比一场，甲队有a，b，c三人 乙队有x，y，z三人 已知：a不和x比，c不和x，z比 编程找出三次比赛名单
# #b-x a-z c-y
# #a b c 1 2 3
# #z x y 3 1 2
for i in range (0,3):# 0x,1y,2z
    for j in range (0,3):
        for k in range (0,3):# ia,jb,kc
            if (i!=j) and (i!=k) and (j!=k):
                if (i!=0) and (k!=0) and (k!=2):#固定abc，把xyz作为012，去匹配
                    print(i,j,k)


# #有n个人围成一圈，从第一个开始报数（从1到3报数），只要是报到3的人，退出圈子 问最后留下来的是第几号位


