# coding:utf-8
# 题目描述：
# 一个土豪拥有的硬币面额及数量如下（注意每个面额只有两个）
# 1 1 2 2 4 4 8 8... 
# 求给定一个正整数n，能够获得的总额为n的硬币组合数
# solution:
# 将N转化为二进制，通过移动末尾的0,移动得到的新的二进制距离N的差距通过
# 另外一个二进制得到补偿，然后将这两个互补的二进制转化为十进制即可。
# 14 = 1110->1101->1011->0111
#      0000->0001->0011->0111

from collections import defaultdict

def getpermutation(n):
    if n <= 0:
       return 0
    res = 0
    
    binary_n = bin(n)
    binary_n = list(str(binary_n[2:]))
    binary_len = len(binary_n)
    new_bin = ['0' for i in range(binary_len)]

    
    flag = True

    while flag:
        flag = False
        for i in range(binary_len-1):
            if binary_n[i+1] == '0' and new_bin[i+1] == '0':
                
                if binary_n[i] == '1':
                    binary_n[i] = '0'
                    binary_n[i+1] = new_bin[i+1] = '1'
                    flag = True 
                    print(binary_n,new_bin)
                    res += 1
                elif new_bin[i] == '1':
                    new_bin[i] = '0'
                    binary_n[i+1] = new_bin[i+1] = '1'
                    flag = True 
                    print(binary_n,new_bin)
                    res += 1

    return res + 1

                        
print(getpermutation(14))                        
