"""
The world-known gangster Vito Deadstone is moving to New York. He has a very big family there, all
of them living in Lamafia Avenue. Since he will visit all his relatives very often, he is trying to find a
house close to them.

Vito wants to minimize the total distance to all of them and has blackmailed you to write a program
that solves his problem.

Input
The input consists of several test cases. The first line contains the number of test cases.
For each test case you will be given the integer number of relatives r (0 < r < 500) and the street
numbers (also integers) s1, s2, . . . , si, . . . , sr where they live (0 < si < 30000 ). Note that several
relatives could live in the same street number.

Output
For each test case your program must write the minimal sum of distances from the optimal Vito's house
to each one of his relatives. The distance between two street numbers si and sj is dij = |si − sj |.

Sample Input
2
2 2 4
3 2 4 6

Sample Output
2
4
"""

T = int(input()) # 讀取輸入：第一行是測資數量 T

# 對每一筆測資做處理
for _ in range(T):
    # 讀取這一筆資料：第一個數是親戚人數 r，接下來是 r 個地址
    address = list(map(int, input().split())) 
    r = address[0]  # 第 0 個數是親戚人數
    s = address[1:] # 剩下的是街道編號 list
    
    s.sort() # 排序，因為要找中位數
    mid = s[(len(s)-1)//2] # 找中位數位置
    
    # 計算每個親戚與中位數的距離總和
    total_distance = 0
    for addr in s:
        total_distance += abs(addr - mid)
    
    print(total_distance)
